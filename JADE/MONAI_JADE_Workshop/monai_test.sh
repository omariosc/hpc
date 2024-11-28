#! /bin/bash
#SBATCH --nodes=1
#SBATCH -J monai_test
#SBATCH -c 2
#SBATCH --gres=gpu:1
#SBATCH --time=0:10:00
#SBATCH -p devel

$HOME/miniconda3/envs/monai/bin/python -c 'import monai;monai.config.print_config()'