#! /bin/bash
#SBATCH --nodes=1
#SBATCH -J brats_autoencoder
#SBATCH -c 8
#SBATCH --gres=gpu:1
#SBATCH --mem=10000
#SBATCH --time=1:00:00
#SBATCH -p small

export TEMPSTORE="/raid/local_scratch/$USER/$SLURM_JOBID"
# cd "$TEMPSTORE"
# tar -xf $HOME/Task01_BrainTumour.tar # assumes everything is in your home directory
cd $HOME  

$HOME/miniconda3/envs/monai/bin/python brats_autoencoder.py
