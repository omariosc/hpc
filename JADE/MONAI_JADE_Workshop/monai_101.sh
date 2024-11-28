#! /bin/bash
#SBATCH --nodes=1
#SBATCH -J monai_101
#SBATCH -c 4
#SBATCH --gres=gpu:1
#SBATCH --time=1:00:00
#SBATCH -p small
```
```bash
cd $HOME
export TEMPSTORE="/raid/local_scratch/$USER/$SLURM_JOBID"
cp MedNIST.tar.gz "$TEMPSTORE"

$HOME/miniconda3/envs/monai/bin/python monai_101.py