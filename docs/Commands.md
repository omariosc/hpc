# HPC Commands

## SSH Key

```bash
ssh-keygen -t ed25519 -f ~/.ssh/sshKey -q -N ""
cat ~/.ssh/sshKey.pub
```

## SSH into Jade2

```bash
ssh -o \"IdentitiesOnly=yes\" -i ~/.ssh/hartree -l oxc35-mtc11 jade2.hartree.stfc.ac.uk

ssh -l oxc35-mtc11 -i /users/scsoc/.ssh/hartree jade2.hartree.stfc.ac.uk
```

## MONAI JADE Workshop 24.06.2024

```bash
./miniconda3/envs/monai/bin/jupyter-lab --port 8881

./miniconda3/envs/monai/bin/pip install

srun -p devel -c 8 --gres=gpu:1 --pty /bin/bash
./miniconda3/envs/monai/bin/python
import monai

sbatch .
sacct
```

## ARC

```bash
ssh sc20osc@arc4.leeds.ac.uk
qsub file.sh
qstat
qdel jobID
```

## AIRE

```bash
#!/bin/bash

#SBATCH --job-name=primes
#SBATCH --time=5:00:00
#SBATCH --export=NONE
#SBATCH -n 168

module add miniforge/24.7.1
conda activate parallel-series

python primes.py
```

## SCP

```bash
scp -o "IdentitiesOnly=yes" -i ~/.ssh/hartree -r oxc35-mtc11@jade2.hartree.stfc.ac.uk:/jmain02/home/J2AD014/mtc11/oxc35-mtc11/monai_jade monai_jade
```
