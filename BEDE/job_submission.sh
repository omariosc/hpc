#!/bin/bash

# Generic options:

#SBATCH --account=<project>  # Run job under project <project>
#SBATCH --time=1:0:0         # Run for a max of 1 hour

# Node resources:
# (choose between 1-4 gpus per node)

#SBATCH --partition=gpu    # Choose either "gpu" or "infer" node type
#SBATCH --nodes=1          # Resources from a single node
#SBATCH --gres=gpu:1       # One GPU per node (plus 25% of node CPU and RAM per GPU)

# Run commands:

conda activate example

ARG1=value1
ARG2=value2
ARG3=value3
ARG4=value4

python file.py args.txt
# or
python file.py \
  arg1 $ARG1 \
  arg2 $ARG2 \
  arg3 $ARG3 \
  arg4 $ARG4 
# Place other commands here

echo "end of job"
