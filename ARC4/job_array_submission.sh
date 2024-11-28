#!/bin/bash
#$ -V -cwd
#$ -l h_rt=24:00:00
#$ -l h_vmem=12G
#$ -l coproc_v100=1
#$ -m be
#$ -N Name
#$ -t 1-2

module load cuda/11.1.1

CONFIGS=(CONFIG1 CONFIG2)

task_id=1

ROOTFOLDER=/resstore/b0211/Users

for config in "${CONFIGS[@]}"
do
  if [ $((task_id)) == $SGE_TASK_ID ]; then
    echo ${CONFIGS[task_id-1]}
    python $ROOTFOLDER/path/to/file.py  \
      --arg1 $config \
      --arg2 value2 \
      --arg3 value3
  fi
  task_id=$((task_id+1))
done
