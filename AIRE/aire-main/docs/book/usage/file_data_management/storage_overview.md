# Storage Overview

Aire has a large amount of local storage to support the demanding I/O characteristics and data volumes needed by HPC workloads.
There are several different storage areas which are tuned for different I/O characteristics and usage patterns.
By having different areas we can support the different types of I/O required for various parts of HPC workloads.
The list below shows the different areas, where they are located in the directory tree and the kind of usage they are suited for.
It also indicates how we manage them and the limits they have. All of the filesystems have user quotas, which help to protect them from filling
up and to help ensure fair usage by the users of the system. Larger individual quotas can be requested according to individual need, subject to overall capacity.
Filesystem quotas are explained in detail in the next section.

## Home directories

Each user has a home directory, `/users/<username>`, owned by the user and not accessible by others by default.
The environment variable `$HOME` contains the name of your home directory. It is also contained in the shell symbol `~` (the tilde character).

The home filesystem is used to store things like:

- Program code (source trees and binaries) and your makefiles
- scripts
- parameter files
- notes and documents
- run scripts and batch job files
- listings and log files from runs
- plot files

The home directory is relatively small. It is optimised for small files and your space quota is quite small compared to your scratch directory. You should not use your home directory for I/O from actively running jobs. You have a permanent directory on this filesystem.

We plan to *occasionally* back up this filesystem to mitigate against accidental deletions and hardware failure. However you are recommended to archive any important files onto another system from time to time for double reassurance.

## Scratch directories

Each user has a scratch directory created automatically, i.e., `/mnt/scratch/<username>`, owned by the user and not accessible by others by default. The environment variable `$SCRATCH` contains the name of your scratch directory.

In order to access your scratch directory, simply use `cd $SCRATCH`, or print the path to your scratch directory with `echo $SCRATCH`.

<!-- Note: I have no idea about the following statement. -->
<!-- For compatibility with older systems, `/nobackup` is linked to `/scratch`. -->

<!-- :::{note}
`$SCRATCH` has not been configured for Aire's testing phase. If you'd like to use this environment variable, please create a scratch directory, then:

`export SCRATCH=/mnt/scratch/users/<username>`
::: -->

This is a large parallel filesystem geared for large block I/O from HPC runs. You can use it for active I/O for running jobs. Your space quota is quite large and allows you to retain large data files from runs until you no longer need them. Once your sequence of runs are completed you are expected to delete the data to free up space for others and yourself. Your directory on this filesystem is permanent. However, please note that your data stored here is not backed up.

:::{note}
This is a lustre parallel filesystem, geared for HPC workloads, you should avoid using large numbers of very small files in this area, as it’s not very efficient.
:::

The filesystem is substantial, with approximately 3.8PB of storage, providing ample capacity to store all or a significant portion of your project’s intermediate data. You should be able to maintain multiple generations of intermediate files (at least three generations), allowing you to backtrack and restart from earlier versions if a run fails for any reason.

If the default quota does not meet your needs, you may request an increase. Please include detailed information about your requirements on the request form to help us track demand and plan for future capacity needs effectively.

:::{warning}
Scratch directories are not backed up. We cannot recover any files accidentally deleted from Scratch directories.
:::

### NVMe Lustre

Aire features 138TB of NVMe-based storage optimised for fast I/O-intensive tasks, offering significantly higher performance than standard Lustre storage. This is separate from the 3.6PB of general disk-based Lustre storage.

While general purpose scratch (`$SCRATCH`) is available at `/mnt/scratch/users/<username>`,  this fast storage is mounted at `/mnt/flash`. Unlike the general purpose Lustre storage, this fast NVMe-based storage does not have an automatically-created directory for your use. 

We are currently configuring this for usage and will add detailed instructions here.
:::{note}
We will soon provide detailed instructions on how to utilise the fast Lustre storage system.
:::

<!-- To switch between Lustre and NVMe Lustre in `$SCRATCH`, follow these steps:

```bash
# To use Lustre
cd /mnt/scratch/users
mkdir -p <username>
cd <username>
 
# For a Lustre based directory:
mkdir disc
lfs getstripe disc
 
# For a NVMe Lustre based directory:
mkdir flash
lfs setstripe -p flash flash
lfs getstripe flash
``` -->

## TMP_SHARED

:::{note}
`TMP_SHARED` has not been configured for Aire's testing phase.
:::

Mounted at `/tmp_shared`, the directories on this filesystem are transient and exist only for the lifetime of your batch job. Each job has its own separate unique directory.
The environment variables `$TMP_SHARED` and `$TMPDIR` contain the name of the directory for the current job.
This filesystem is of medium size (150 TBytes) and each user has quota of space. The quota on this filesystem is designed to help prevent run away jobs from using up all the space. This filesystem is strictly for transient data, it shouldn’t be used to store data for any length of time.

:::{warning}
We will delete any non-transient files from this space without warning.
:::

This filesystem is a lustre filesystem, built on SSD devices. SSDs have no seek time, so programs which are doing smaller I/Os or have many files can benefit from the low latency.
This is why we assign this filesystem to `$TMPDIR`, so by default, all temporary I/O will be done in this area. The default current directory for batch jobs is `$TMPDIR`, so you don’t need to do anything special to take advantage of the extra performance.

## TMP_LOCAL

:::{note}
`TMP_LOCALD` has not been configured for Aire's testing phase.
:::

Mounted at `/tmp` the directories on this filesystem are transient and exist only for the lifetime of your batch job. Each job has its own separate directory. `/tmp_local` is linked to `/tmp` for convenience.  The environment variable `$TMP_LOCAL` contains the name of the directory for the current job.

`TMP_LOCAL` exists on the local storage of each compute node. It is not shared with other compute nodes. The filesystem is quite small, but is based on SSD devices. So it is fast and low latency. `TMP_LOCAL` is recommended for local transient storage for runs which run on a single node, including serial (single processor) jobs.
With many applications you can set a tmp parameter to direct its I/O to the local disk (eg. Matlab, Java, R, Abaqus, Gaussian) and it is recommended to use this.
<!-- Some of our centrally installed modules will set this for you automatically, please see the -->
<!-- TODO: review list of applications that set tmp_local automatically and add here -->
<!-- TODO: Gaussian, Abaqus, etc. -->