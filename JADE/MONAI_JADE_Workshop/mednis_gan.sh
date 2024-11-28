#! /bin/bash
#SBATCH --nodes=1
#SBATCH -J mednist_gan
#SBATCH -c 12
#SBATCH --gres=gpu:1
#SBATCH --time=1:00:00
#SBATCH -p small

export TEMPSTORE="/raid/local_scratch/$USER/$SLURM_JOBID"
cd "$TEMPSTORE"
tar xzf $HOME/MedNIST.tar.gz
cd $HOME

DATASETDIR=$TEMPSTORE/MedNIST/Hand
CKPT=none
BUNDLE="$HOME/mednist_gan"
export PYTHONPATH="$BUNDLE"

$HOME/miniconda3/envs/monai/bin/python \
    -m monai.bundle run training \
    --meta_file "$BUNDLE/configs/metadata.json" \
    --config_file "$BUNDLE/configs/train.json" \
    --bundle_root "$BUNDLE" \
    --dataset_dir "$DATASETDIR" \
    --trainer::max_epochs 5 \
    --ckpt_path "$CKPT"

# module load apptainer

# apptainer run --nv \
#     --bind $DATASETDIR:/data \
#     monai.sif python -m monai.bundle run training \
#     --meta_file "$BUNDLE/configs/metadata.json" \
#     --config_file "$BUNDLE/configs/train.json" \
#     --bundle_root "$BUNDLE" \
#     --dataset_dir /data \
#     --trainer::max_epochs 5 \
#     --ckpt_path "$CKPT"