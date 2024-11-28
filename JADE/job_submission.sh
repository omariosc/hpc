#!/bin/bash

# set the number of nodes
#SBATCH --nodes=1

# set max wallclock time
#SBATCH --time=10:00:00

# set name of job
#SBATCH --job-name=name

# set number of GPUs
#SBATCH --gres=gpu:1
#SBATCH --partition=big

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=username@leeds.ac.uk

# run the application
ROOTFOLDER=/path/to/rootfolder

python $ROOTFOLDER/file.py \
  --arg1 value1 \
  --arg2 value2 \
  --arg3 value3
