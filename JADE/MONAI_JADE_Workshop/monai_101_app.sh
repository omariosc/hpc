#! /bin/bash
#SBATCH --nodes=1
#SBATCH -J monai_101_app
#SBATCH -c 4
#SBATCH --gres=gpu:1
#SBATCH --time=1:00:00
#SBATCH -p small

module load apptainer

cd $HOME
export TEMPSTORE="/raid/local_scratch/$USER/$SLURM_JOBID"
cp MedNIST.tar.gz "$TEMPSTORE"

apptainer run --nv \
  --bind $TEMPSTORE:/local_scratch \
  --env TEMPSTORE=/local_scratch \
  monai.sif python monai_101.py