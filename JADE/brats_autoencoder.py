
import os
from glob import glob
from datetime import datetime
import torch
from monai.metrics import PSNRMetric
from monai.networks.nets import AutoEncoder
from monai.config import print_config
from monai.data import Dataset, DataLoader, partition_dataset, CacheDataset, PersistentDataset, SmartCacheDataset
from monai.utils import set_determinism
from monai.transforms import (
    Compose,
    LoadImage,
    ScaleIntensityd,
    Lambda,
    SpatialPadd,
)
import gc

torch.multiprocessing.set_sharing_strategy('file_system')
print_config()
set_determinism(0)

# generate synthetic gadolinium-enhanced T1w brain image from FLAIR, T1w and T2w images.

device = "cuda:0" if torch.cuda.is_available() else "cpu"

root_dir = os.environ["TEMPSTORE"]

all_images = sorted(glob(f"{root_dir}/Task01_BrainTumour/images*/*.nii*"))
train_images, eval_images = partition_dataset(all_images, (4, 1), shuffle=True,seed=42)

IN_KEY = "in_images"
OUT_KEY = "ge_image"
keys = (IN_KEY, OUT_KEY)
pad_size = (256, 256, 160)

max_epochs = 2 # 60
batch_size = 2 # 8/10
num_workers = 8 # 10
learning_rate = 1e-3
valid_interval = 1


def _rearrange_images(img):
    img = img.permute(3, 0, 1, 2)
    return {IN_KEY: img[:3], OUT_KEY: img[3:]}
    

train_transforms = Compose([
    LoadImage(),
    Lambda(_rearrange_images),
    ScaleIntensityd(keys,channel_wise=True),
    SpatialPadd(keys, spatial_size=pad_size)
])

val_transforms = Compose([
    LoadImage(),
    Lambda(_rearrange_images),
    ScaleIntensityd(keys,channel_wise=True),
    SpatialPadd(keys, spatial_size=pad_size)
])

train_ds = SmartCacheDataset(train_images, train_transforms)
train_dl = DataLoader(train_ds, num_workers=num_workers, batch_size=batch_size, shuffle=True)
# , cache_dir=root_dir
val_ds = SmartCacheDataset(eval_images, val_transforms)
val_dl = DataLoader(val_ds, num_workers=num_workers, batch_size=batch_size, shuffle=True)

model = AutoEncoder(
    spatial_dims=3,
    in_channels=3,
    out_channels=1,
    num_res_units=2,
    channels=(16, 32, 64, 128),
    strides=(2, 2, 2, 2),
).to(device)

# Create loss fn and optimiser
loss_function = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), learning_rate)
metric = PSNRMetric(1)
epoch_losses = []

for epoch in range(1, 1 + max_epochs):
    model.train()
    epoch_loss = 0
    step = 0
    for batch in train_dl:
        step += 1
        inputs, outputs_gt = batch[IN_KEY].to(device), batch[OUT_KEY].to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_function(outputs, outputs_gt)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    epoch_loss /= step
    epoch_losses.append(epoch_loss)

    print(datetime.now().strftime(f"%H:%M:%S Epoch {epoch}, loss: {epoch_loss}"))
    
    gc.collect()
    gc.collect()
    torch.cuda.empty_cache()
    
    if epoch % valid_interval == 0:  # validation
        valid_values = []
        model.eval()
        for batch in val_dl:
            inputs, outputs_gt = batch[IN_KEY].to(device), batch[OUT_KEY].to(device)
            outputs = model(inputs)
            valid_values.append(metric(outputs, outputs_gt))

        mval = torch.cat(valid_values).mean().item()
        print(datetime.now().strftime(f"%H:%M:%S Epoch {epoch}, mean validation: {mval}"))
        

torch.save(model.cpu().state_dict(), "ge_autoencoder.pt")
