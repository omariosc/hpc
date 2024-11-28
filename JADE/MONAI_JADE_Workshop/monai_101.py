import os
import torch
from monai.apps import MedNISTDataset
from monai.data import DataLoader
from monai.engines import SupervisedTrainer
from monai.inferers import SimpleInferer
from monai.networks import eval_mode
from monai.networks.nets import densenet121
import monai.transforms as mt

# assumes tarball is in this temp directory
root_dir = os.environ["TEMPSTORE"]

max_epochs = 25
device = torch.device("cuda:0")
net = densenet121(spatial_dims=2, in_channels=1, out_channels=6).to(device)

transform = mt.Compose([
    mt.LoadImaged(keys="image", image_only=True),
    mt.EnsureChannelFirstd(keys="image"),
    mt.ScaleIntensityd(keys="image"),
])

dataset = MedNISTDataset(root_dir=root_dir,transform=transform,
                         section="training", progress=False)

train_dl = DataLoader(dataset, batch_size=512, shuffle=True, num_workers=4)

trainer = SupervisedTrainer(
    device=device,
    max_epochs=max_epochs,
    train_data_loader=train_dl,
    network=net,
    optimizer=torch.optim.Adam(net.parameters(), lr=1e-5),
    loss_function=torch.nn.CrossEntropyLoss()
)
trainer.run()
torch.jit.script(net).save("mednist.ts")

class_names = ("AbdomenCT", "BreastMRI", "CXR", "ChestCT", "Hand", "HeadCT")
testdata = MedNISTDataset(root_dir=root_dir, transform=transform, 
    section="test", download=False, progress=False, runtime_cache=True)

max_items_to_print = 10
eval_dl = DataLoader(testdata, batch_size=1, num_workers=0)

with eval_mode(net):
    for _, item in zip(range(max_items_to_print),eval_dl):
        result = net(item["image"].to(device))
        prob = result.detach().to("cpu")[0]
        pred = class_names[prob.argmax()]
        gt = item["class_name"][0]
        print(f"Prediction: {pred}. Ground-truth: {gt}")