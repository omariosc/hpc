# Job Examples

By default, jobs are automatically assgned default resources:

- 1 CPU core
- 1GB memory
- Execution on the standard compute node pool

Users must always specify a time limit, either at submission or in their job script.

In the following examples, we demonstrate job scripts for running jobs on various configurations of resource.

## Serial jobs

The following script requests 1 CPU, 1 hour runtime, and 1GB memory, specifying the job name as ```simple_serial_job```. Here we explicitly set the number of tasks & number of cores to 1, but this is not strictly necessary as they are the default settings.

```bash
#!/bin/bash
#SBATCH --job-name=simple_serial_job
#SBATCH --time=01:00:00
#SBATCH --mem=1G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

# Load any necessary modules
module load <module_name>

# Run the job
./example.bin
```

This script requests 1 CPU, 1 day runtime, and 2GB memory. In this case, we also explicitly specify the location of the output file. The variable ```%j``` is automatically set to the job ID number.

```bash
#!/bin/bash
#SBATCH --job-name=simple_serial_job
#SBATCH --time=1-00:00:00
#SBATCH --mem=2G
#SBATCH --output=/path/to/output/file.%j

# Load any necessary modules
module load <module_name>

# Run the job
./example.bin
```

## Parallel jobs

Parallel jobs include those run over multiple cores within the same node (SMP, typically via OpenMP) or across multiple nodes via a message passing interface (MPI) such as Open MPI.

:::{warning}
Note that in order to use more than one CPU (or core) your program must be specifically written to use a parallel programming model. Just requesting more CPUs in Slurm will not make the program use more than 1 CPU; the extra CPUs you reserved will sit idle.
:::

### Threaded

Here we request 16 cores within a single node for 5 hours. Note that jobs will need to be compiled for execution on multiple threads (eg via OpenMP) or run on multithreading-capable software; the below example is for a binary compiled for OpenMP.

```bash
#!/bin/bash
#SBATCH --job-name=simple_threaded_job
#SBATCH --time=05:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1          # Number of tasks for OpenMP
#SBATCH --cpus-per-task=16  # Number of CPU cores per task

# Load any necessary modules
# module load <module_name>

# Tell OpenMP how much resource it has been given
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK 

# Run the job
./example.bin
```

### MPI

These are jobs which run across multiple nodes, via a Message Passing Interface (MPI). Aire currently offers Open MPI 5.0.5. Here we request 256 cores across 8 nodes:

```bash
#!/bin/bash
#SBATCH --job-name=openmpi-job
#SBATCH --time=05:00:00
#SBATCH --ntasks=256            # Number of MPI processes
#SBATCH –-nodes=8               # Number of nodes   
#SBATCH --ntasks-per-node=32    # Number of tasks per node

# Load any necessary modules, e.g. MPI
module load openmpi

# Run the job
mpirun ./example.bin
```

Note that multiple node jobs must use all the CPUs (cores) on the requested nodes.

## AI/ML jobs on GPU

This example shows how to run a PyTorch job in a Conda environment on Aire, which uses Miniforge as the Conda installer. To request GPUs, make sure to specify the gpu partition in your Slurm script with `#SBATCH --partition=gpu`. Then, request the number of GPUs you need using `#SBATCH --gres=gpu:N`, where `N` is the number of GPUs; for instance, `#SBATCH --gres=gpu:1` for one GPU or `#SBATCH --gres=gpu:2` for two GPUs.

```bash
#!/bin/bash
#SBATCH --job-name=ml-job          # Job name
#SBATCH --time=01:00:00            # Request runtime (hh:mm:ss)
#SBATCH --partition=gpu            # Request GPU partition
#SBATCH --gres=gpu:1               # Request 1 GPU

# Load any necessary modules, e.g. Miniforge
# Activate conda environment
module load miniforge
conda activate my_ML_environment

# Run the job
python my_ML_script.py
```

```{tip}
Requesting 1 GPU defaults to using 1 CPU core and 1GB memory for your job. If you need more CPU cores and memory, you need to request them separately using additional SBATCH directives. On one GPU node, there are 24 CPU cores and 256GB memory total, with resources divided among 3 GPUs (approximately 8 cores and 85GB memory available per GPU). For example, to request 8 CPU cores with 8GB memory per core (32GB total):

    #SBATCH --cpus-per-task=4          # Request 4 CPU cores
    #SBATCH --mem-per-cpu=8G           # Request 8GB memory per CPU core
```

```{admonition} Using the Flash storage
Aire provides temporary Flash storage ($TMP_SHARED) for high I/O performance during job execution. This NVMe storage has a quota of 1TB and 1.5M files per job, making it ideal for I/O-intensive workloads like ML/AI. Data is automatically purged when the job ends. Request Flash storage in your job script:

    #!/bin/bash
    #SBATCH --job-name=gpu-flash       # Job name
    #SBATCH --time=01:00:00            # Request runtime (hh:mm:ss)
    #SBATCH --partition=gpu            # Request GPU partition
    #SBATCH --gres=gpu:1               # Request 1 GPU
    #SBATCH --cpus-per-task=4          # Request 4 CPU cores
    #SBATCH --mem-per-cpu=8G           # Request 8GB memory per CPU core

    # Flash storage path is automatically set as $TMP_SHARED
    echo "Flash storage path: $TMP_SHARED"

    # Copy input data to Flash storage
    cp -r /path/to/input/data $TMP_SHARED/

    # Load GPU environment
    module load miniforge
    conda activate my_ML_environment

    # Run GPU job using local data
    python my_ML_script.py --data $TMP_SHARED/data

    # Copy results back to permanent storage
    cp -r $TMP_SHARED/results /path/to/permanent/storage/

    # Flash storage ($TMP_SHARED) is automatically cleaned after job ends
```

## Large-memory jobs

Here we request use of a high-memory node to run threaded application via OpenMP. Note that the option `--mem` applies to the amount of memory requested *per node*.

```bash
#!/bin/bash
#SBATCH ---job-name=large_memory_job
#SBATCH --time=01:00:00
#SBATCH --partition=himem   # Request high-memory node
#SBATCH --mem=160G          # Request 160GB memory (10GB per core)
#SBATCH --nodes=1
#SBATCH --ntasks=1          # Number of tasks for OpenMP
#SBATCH --cpus-per-task=16  # Number of CPU cores per task

# Tell OpenMP how much resource it has been given
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK 

# Run the job
./example.bin
```

## Task arrays

Array jobs let you run a set of serial jobs with a single submission. Slurm runs multiple instances of the job simultaneously, and each job can use different parameters or data. The example script below runs 100 instances in a Conda environment, with input and output files determined by the array index `$SLURM_ARRAY_TASK_ID`. Task arrays are also compatible with other software, making them flexible for a variety of workflows.

```bash
#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --array=1-100

# Load any necessary modules
# e.g. using a conda environment
module load miniforge
conda activate my_environment

# Run the job, passing in the input and output filenames
python –i ~/input/input.$SLURM_ARRAY_TASK_ID –o ~/results/out.$SLURM_ARRAY_TASK_ID
```
