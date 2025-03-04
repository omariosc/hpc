# Aire User Documentation

This site documents information relevant to users of Aire, the High Performance Computing (HPC) facility at the [University of Leeds](https://www.leeds.ac.uk). It is oriented towards researchers with basic experience using a Unix-like command line interface (CLI).

Launched on the 6th of February 2025, Aire is the University of Leeds' latest HPC system, bringing cutting-edge computational power to support research across disciplines. With major upgrades in computing power, memory, and storage, Aire is set to enhance data processing and streamline research workflows.

```{admonition} Upgrading from ARC3 and ARC4
Aire is the new HPC system replacing the ARC3 and ARC4 systems. The new system significantly increases compute capacity for the community while delivering a modern, maintainable software and programming environment.

Please be aware that:

- New login and management nodes have been installed, meaning **users of the old systems need to [get a new account](getting_started/get_account.md) on Aire.**
- Storage is not shared between different systems, so **if you need to retain data from the old systems, you must transfer it yourself.**
```

```{admonition} ARC3 System Retirement Notice
The ARC3 system is now retired from service.
- 1st November 2024: ARC3 account registration period closed.
- 2nd December 2024: Batch and interactive access to all compute resources will be withdrawn.
- 1st March 2025: All access to the service will be withdrawn and physical decommissioning of the system will commence. Note that all data on this system will be lost at this point.
```

```{admonition} ARC4 System Retirement Notice
ARC4 will be completely shut down by June 2025. Note that all data on this system will be lost at that point. For more information about this decision, please see our [blog post](https://arc.leeds.ac.uk/supporting-teaching/). The decommissioning timeline will be published shortly.
```

:::{seealso}
To expand your expertise, you might be interested in exploring the [training courses](https://arc.leeds.ac.uk/courses/) offered by the [Research Computing](https://arc.leeds.ac.uk/) team. Also, check out the [HPC Architecture](system/hpc_architecture.md) section for a basic introduction to the system.
:::
# Expectations

When using Aire, please adhere to these guidelines to ensure optimal system performance and fair resource allocation for all users.

## Storage Usage

- **Do not use scratch space as permanent storage.**
- **Output files must be saved to scratch.**
- Regularly clean up unnecessary files.
- Back up important data to appropriate permanent storage.

## Job Submission

- **Request only the resources your job actually needs.**
- Set appropriate time limits for your jobs.
- Use job arrays for multiple similar tasks.
- Clean up or transfer your job outputs promptly.
- Test your jobs with small datasets first.

## Login Node Usage

- **Do not run computationally intensive tasks on login nodes.**
- Use login nodes only for:
  - Job submission
  - File management
  - Light file editing
  - Job monitoring
- Submit intensive tasks through the job scheduler.

## Communication

- **Do not auto-archive system notifications.**
- Read and respond to critical system announcements.
- Keep contact information up to date.

## Software and Modules

- Load only the modules you need.
- Unload modules when no longer needed.
- Request software installations through proper channels.

## Security

- **Do not share your login credentials.**
- Use strong passwords.
- Report suspicious activities.
- Keep your SSH keys secure.

## Resource Sharing

- Release resources when jobs complete.
- Be mindful of storage quotas.
- Respect fair-share scheduling policies.
- Report system issues to help maintain service quality.

```{note}
Following these guidelines helps ensure a smooth and efficient experience for all users of the Aire HPC service.
```


# Frequently Asked Questions

<!-- TODO: add questions/answers -->

# Requesting an account

## Prerequisites

The HPC systems run the Linux operating system. You should be familiar with using Linux at the command line level in order to run tasks. We provide periodic training sessions on "Introduction to Linux for HPC" to help you get started; you can find the link to the HPC0 training below. Much of the work done on HPC systems is scripted to automate many tasks, so understanding the basics is important and highly beneficial.

[HPC0: Introduction to Linux for HPC](https://arc.leeds.ac.uk/courses/hpc0-introduction-to-linux-for-hpc/)

## User Accounts

Each user of the system has their own separate user account, which is linked to your University account. You must not share your accounts or passwords under any circumstances. There are data-sharing mechanisms to facilitate collaborative work, which are described in the file and data management section.

```{admonition} Postgraduate Researchers
All Postgraduate Researchers (academics, post-doctoral researchers and postgraduate students) are entitled
to HPC accounts.
```

```{admonition} Taught Course Students
Taught course students should speak to their supervisor before submitting an application request as they will be required to
sponsor your application.
```

You can request an Aire account via the <a href="https://it.leeds.ac.uk/it?id=sc_cat_item&sys_id=4c002dd70f235f00a82247ece1050ebc" target="_blank">IT service form</a>


# Logging-on

To connect to the Aire platform, the steps vary depending on whether you are on the wired campus network or offsite/using Eduroam. If you are offsite, you must connect through the University's SSH gateway or use the University VPN. However, if you are on the campus network, no additional steps are required. The instructions below are organized based on whether you are connecting from on-campus or off-campus.

:::{note}
Connecting via Eduroam or from the NHS network in St James's University Hospital are considered off-site connections. 
:::

## Connecting from campus

You can connect to Aire and log in using SSH (Secure Shell) from within the University network.
Please see the following Knowledge Base articles for more information:

+ <a href="https://it.leeds.ac.uk/it?id=kb_article_view&sysparm_article=KB0018276" target="_blank">KB0018276 - How do I connect to Aire from a Windows machine on campus?</a>
+ <a href="https://it.leeds.ac.uk/it?id=kb_article_view&sysparm_article=KB0018275" target="_blank">KB0018275 - How do I log in to Aire on Linux or Mac OS from on Campus?</a>

Note that the above articles require you to log in with your University account to view.

## Connecting when off-site

To access Aire from outside the University, you will need to connect through the University's general SSH gateway or use the University VPN, whereas access from the campus network does not require this additional step.
Please see the following Knowledge Base articles for more information:

+ <a href="https://it.leeds.ac.uk/it?id=kb_article_view&sysparm_article=KB0018286" target="_blank">KB0018286 - How do I connect to Aire from a Windows machine off campus?</a>
+ <a href="https://it.leeds.ac.uk/it?id=kb_article_view&sysparm_article=KB0018284" target="_blank">KB0018284 - How do I log in to Aire on Linux or Mac OS from off Campus?</a>

For more general guidance on using SSH and the VPN for remote access, please see the following Knowledge Base articles:

+ <a href="https://it.leeds.ac.uk/it?id=kb_article_view&sysparm_article=KB0014674" target="_blank">KB0014674 - SSH remote access at the University of Leeds</a>
+ <a href="https://it.leeds.ac.uk/it?id=kb_article_view&sysparm_article=KB0014410" target="_blank">KB0014410 - Connecting to the University VPN</a>

Note that the above articles require you to log in with your University account to view.


# Rules and Regulations for using Aire

HPC systems are shared systems and support many users simultaneously. There are tools and protocols in place which allow the different tasks  from different users to co-exist on the one system, but they aren’t 100% bullet proof. You are required to use the appropriate tools and protocols we offer on the system and to ensure that your programs don’t misbehave by interfering with other work. You are also required to ensure that your runs are efficient and make good use of the resources. **We will terminate, without warning, runs which do not meet these criteria.**

Occasionally we will ask you to modify your usage, or to not run certain tasks which cause issues. We appreciate your co-operation in this and will try to help you find ways to avoid the issues. If you find a colleague causing issues, please advise them and contact us so we can help. Please be considerate to your fellow users and the community as a whole.
We reserve the right to disable your access to Aire without warning if we perceive you are causing problems. We will normally try to contact you beforehand.

:::{Note}
In exceptional circumstances when required, we reserve the right to access and/or modify any of your files on the system. While this is not usual , it may be necessary to do this for example to resolve a system issue.
:::

Ensure that you have a valid e-mail address and that you monitor it when you are running work. This will be the normal way we, and the system itself, will communicate with you, especially of there are problems or errors occurring.

:::{warning}
The HPC service is not intended for processing sensitive or personal data. In general data which has been de-identified (eg the names have been removed, so that an individual cannot be identified from the data) can be used on the system. If in doubt, you should seek advice.

Personal or sensitive data must not be stored on the system.
:::

## HPC Acknowledgement

When you publish research papers, or make posters or presentations at conferences and the like, we ask that you give credit for use of the service. The following sentence is appropriate in your acknowledgements:

> This work was undertaken on the Aire HPC system at the University of Leeds, UK.

## Fair share/priority

As well as managing resources, the scheduler also looks after job priorities.

On Aire a **fair share algorithm** is used to manage job priorities. The basis of fair share is that as you use more and more resources over time, your priority reduces in proportion to your usage. This happens to all users. The net effect is that less usage gives you higher priority, and heavier usage decreases your priority. This is applied to all users, in proportion to your usage. Thus, when you submit a job, a job submitted by another user later on may run before yours, if your usage is higher than the second user.

Your usage value is periodically aged, so that with time your priority goes up again. This helps smooth the usage pattern over longer periods of time, so you don’t suffer from lower priority forever.

The purpose of fair share is to give users equitable and reasonable access to the HPC resources. The HPC systems are shared by many users. Fair share prevents one, or a small group of users from dominating the system and using up large proportions of the available resources. Additionally it does not prevent any users from running work if there are spare/idle resources that can run that work.

For example, if you are a heavy user, you may find that a large job submitted at lunchtime does not start quickly, as lots of other users are also running work and your priority is quite low, as you’ve consumed lots of resources in the preceding days. However, by late evening or nighttime, the system will have completed a lot of work, and you may find that your job starts overnight. If you go on holiday for a couple of weeks and don’t run work, your priority will have improved, and when you return, your jobs may start running sooner.
In practice this means everyone gets a fair amount of work run and the system is fully utilised as much as possible.

:::{note}
Note that **short test jobs**, such as debugging runs are treated separately by the scheduler and you should be able to run small numbers of such jobs alongside your other work without undue delays.
:::


# Getting Started

## What is HPC?

A High Performance Computing system, often called a Cluster or SuperComputer is a specially constructed computing system which is designed to allow multiple processors to work on the same problem at the same time and to thus speed up the rate of work above the speed of a single computer. This is very attractive to researchers as problems which might take years to run on a single processor might run 10 or 100 times faster using 10 or 100 processors in parallel, thus reducing the time to results for the researcher. Over many years, hardware and software has been developed to enhance this and to enable faster and faster supercomputers, to the extent that HPC simulations and modelling are now seen as the 3rd pillar of modern scientific research alongside theory and experiment.
While this is all well and good, it’s not magic, there is no fairy dust that can just make code run on hundreds of processors. So a lot of work and effort has to be put into using these system effectively and to get the most out of them. There are special programming models and techniques which are used to program the systems which might require you to totally rewrite your code. Nevertheless many algorithms have been implemented to run in parallel and take advantage of HPC, bringing significant benefits to research.
If you are a researcher and find that your current computational work running on your workstation is taking a long time to run, for example longer than overnight, or you find yourself trying to grab your colleagues machines and run your work on them at night or over weekends, then you might like to start to explore how HPC might help you.

## What type of work do we support?

Aire supports a number of different categories of work. These include:

**Serial jobs**, running on a single processor. We can accommodate large numbers of these, and the system provides tools to automatically manage these and co-ordinate the workflow. It is capable of running **many jobs at the same time**, without it interfering with other work on the system. There are **job arrays**, which help to automate tasks such as parameter sweeps and the processing of large numbers of datasets, using a single command to initiate the runs.
**Parallel jobs**, running on a few CPUs or more, up to the size of a single compute node. These jobs often use techniques such as OpenMP, pthreads, or tasking to spread the work for a particular run over several cores, thus reducing the overall run time.
**Multi-node parallel jobs**, these usually use the MPI programming model, which allows the user program to co-ordinate its work across large numbers of processors and nodes, and is the de facto standard for large simulations. Some codes can scale up to thousands of processors using this technique. Aire and many other HPC systems have a special hardware feature linking the nodes together, called a low latency interconnect, (an example is Infiniband) which improves the performance of these types of code, especially at larger scale.

In general we can support most areas where there are long runs that take hours, and/or there are a lot of them. The system uses the Linux OS, so if your code is Windows based, you’ll need to port it to the Linux environment, or find an existing Linux code that does the job you want. It’s well worth the small effort to learn a bit of Linux and get the benefits of running work on the HPC and the tools you can use.

## How to get started with HPC?

Before diving into HPC, it's beneficial to have discussions with your colleagues and supervisor to understand how HPC can best support your research. They can provide valuable insights and advice based on their experience. If you're new to HPC, consider taking introductory training courses such as [HPC0: Introduction to Linux for HPC](https://arc.leeds.ac.uk/courses/hpc0-introduction-to-linux-for-hpc/) and [HPC1: Introduction to High Performance Computing](https://arc.leeds.ac.uk/courses/hpc1-introduction-to-high-performance-computing/) to build a solid foundation. Additionally, explore self-help resources and join relevant teams or forums where you can ask questions and share knowledge with other HPC users. These steps will help you make the most of the HPC resources available to you.

<!-- ## Table of Contents

```{tableofcontents}
``` -->


# Compute node types

The Aire HPC cluster is composed of various types of compute nodes, each designed to handle specific computational tasks and workloads. This section provides an overview of the different compute node types available, including standard compute nodes, high-memory nodes, and GPU nodes. Each type offers unique capabilities to meet the diverse needs of users.

## Standard compute node

- 52 systems
- Dell R6625 servers
- AMD Dual 84 core 2.2GHz (9634 Genoa-X)
- 768GB DDR5-4800 Memory
- Dual 480GB M2 drives
- **9,072 cores** total

## High-memory node

- 2 systems
- Dell R6625 servers
- AMD Dual 84 core 2.2GHz (9634 Genoa-X)
- Dual 480GB M2 drives
- 2.3TB DDR5-4800 Memory

## GPU node

- 28 systems
- Dell R7615 servers
- 3 x NVIDIA L40S 48GB GPUs (PCIe)
- AMD 24 core 2.9GHz (9254 Genoa-X)
- 256GB DDR5-4800 Memory
- Dual 480GB M2 drives
- **84 GPU cards** total

```{admonition} Purchasing Additional Aire Nodes
If your project requires additional resources, you can purchase nodes for priority access within the Aire HPC system. More details can be found at [Aire - Advanced Research Computing](https://arc.leeds.ac.uk/platforms/aire/).


# Contact Us

There are number of resources available to get help with using the HPC system.
Firstly this documentation area, and the FAQ. Please consult these before contacting us.

<!-- - You can contact the Research Computing team via [TEAM - HPC Upgrade - ARC to AIRE](https://teams.microsoft.com/l/team/19%3ASTr5OAmdRtIZDouZIGHsk6oH4XWmyHPU6a1lgtQffRI1%40thread.tacv2/conversations?groupId=94592ead-d37d-42b5-abc8-ca508bf21159&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb)
- The Research Computing team have a [shared e-mail box](mailto:rcteam@leeds.ac.uk). -->

You can open a [Research IT support ticket](https://leeds.service-now.com/it?id=sc_cat_item&sys_id=7587b2530f675f00a82247ece1050eda) in the IT ServiceNow system.

## RSE

The Research Software Engineering (RSE) team is an important and essential part of the HPC and Research Computing ecosystem at the University. Their primary role is to provide support for research projects where there is a large computational component. They are able to give advice about planning your project and its computational requirements. But more importantly they can collaborate with you to perform major software and workflow development, including programming reviews, performance analysis, code modernisation and refactoring. The RSE team has its own website [here](https://arc.leeds.ac.uk/).

The RSE team also hosts a [Research Computing Community](https://teams.microsoft.com/l/team/19%3ADhcafsOyYnWotrwqTZkjDpRhSp7Cemz4qQpZfk7G5v01%40thread.tacv2/conversations?groupId=1ff8cb55-a479-4202-9dc4-a97891c03f42&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb), bringing together a broader network of individuals using HPC and engaging in research software development. If you're interested in HPC or research software development, we warmly invite you to join this community on Microsoft Teams.

## RIE

The Research Infrastructure Engineering (RIE) team also contributes to the HPC and Research Computing ecosystem at the University.

<!-- TODO: What does the RIE team do? -->
<!-- TODO: How to contact the RIE team? -->


# Data lifecycle management

:::{warning}
This page is still being updated. If you have any feedback regarding this section, please contact the RSE team.
:::

## Storage Tiers and Policies

- Scratch Storage

  * Purpose: Temporary storage for data generated during active job execution.
  * Location: `/mnt/scratch/users/`
  * Retention: Data in scratch storage is not automatically deleted and is not backed up. Users are responsible for managing their scratch data.
  * Quota: A storage quota is applied to scratch directories. Exceeding your quota may prevent you from saving or moving additional data. Ensure that your data usage stays within the allocated limit.
  * Best Use: Store intermediate files and large datasets during active computations. Data should be moved to a more permanent storage location once it is no longer required in scratch storage.

- Home Directories

  * Purpose: Personal storage for code, configurations, and small datasets.
  * Location: `/users/<username>`
  * Retention: Data in home directories is occasionally backed up by the system. However, backups can only be restored within 7 days of the backup date.
  * Quota: A default quota of 15GB is applied to home directories. Users who require more space can request an increase to their storage quota.
  * Best Use: Store essential files, scripts, and results that need to be preserved long-term.

- Shared Project/Research Storage

  * Purpose: Collaborative storage for teams or research groups to share large datasets and results.
  * Location: TBC
  * Retention: Managed based on project needs and user policies.
  * Best Use: Store large datasets shared between team members or across projects.

## Best Practices for Data Management

- Organising Data: Use a consistent and logical folder structure to manage your files. For example:

  ```
  /home/username/project_name/
      ├── code/       # Store your code and scripts here
      ├── data/       # Place your input data and large datasets here
      ├── results/    # Store the output files and results here
      └── README.txt  # Key details about the project, data, and any relevant information
  ```
  * README.txt Example

  > Project: HPC Data Analysis
  >
  > This directory contains the data and scripts for the analysis of computational fluid dynamics results.
  >
  > /code/ contains all the scripts and programmes used for data processing and simulation.
  > /data/ contains raw input data and intermediate files.
  > /results/ contains the final output, including analysis and visualisation.
  >
  > Important Notes:
  > 1. Make sure to regularly back up the data in /data and /results.
  > 2. For any questions, contact [Your Name] at [Your Email].

- Efficient Storage Usage: 

  * Regularly clean up your scratch storage to ensure you don't exceed your quota.
  * Compress large datasets using tools like `tar` or `gzip` to reduce storage consumption.
  * Remove any obsolete data from scratch storage to free up space for new work.

- Data Transfer

  * Use `rsync` and `scp` for transferring data securely and efficiently.
  * For large datasets, consider using parallel data transfer tools like Globus for faster, multi-threaded transfers.

- Data Backup
- Version Control

## Temporary vs Long-term Data

- Temporary Data: Scratch storage is intended for temporary data that can be removed after job completion. As it is not backed up, make sure to transfer any important data to home directories or permanent storage before it's deleted or overwritten.

- Long-term Data: For files that need to be kept beyond the lifetime of a job, use home directories for small files, and shared project/research storage or other permanent storage for large files.

## Monitoring Storage Usage

- Check Usage: Monitor your scratch directory storage to ensure you stay within your quota:

```bash
du -hs /mnt/scratch/users/<username>/
```

- Check Quotas: To verify your current storage quota and limits, use:

```bash
quota -s
```

If you are nearing your quota, consider cleaning up or transferring data to home or project storage. If more space is required, contact HPC support for assistance.

## Data Security and Compliance

- Access Control: Set appropriate file permissions using `chmod` and `chown` to ensure that sensitive data is only accessible to authorised users.
- Secure Data Transfers: Always use secure methods (e.g., `scp`, `rsync`, or Globus) when transferring data, especially for sensitive or confidential files.
- Compliance: Ensure your data management practices align with legal and regulatory requirements, such as General Data Protection Regulation (GDPR) and NHS Privacy Enhancing Technology (PET), if applicable.

## End-of-Project Data Archival

- Archiving or Deletion: At the end of a project, move relevant data to an archive storage (for example, OneDrive) for future access. Ensure that any necessary backups are taken before the project is completed.
- Cleanup: Clean up scratch and home directories to free up space for future users and projects.
- Documentation: Include clear documentation about archived data, including directory structures and any important details in `README.txt` files.


# Data Sharing
<!-- Original title: File permissions and access control -->

It is important that you understand how the Linux system for controlling access to files works and if you need to share files with another user, how to do this safely and not open up access to people you don’t want to. This area is one of the most common areas which people have problems with in Linux, so we have a guide to this area.

There are 3 permissions: read (r), write (w) and execute (x). There are 3 levels of permission: owner, group and all. The default permissions on ARC3 are different to ARC4: On ARC3 group and all have read and execute permissions on new files, whereas on ARC4 group and all have no permissions. Permissions, group and ownership can be changed with `chmod`, `chgrp` and `chown` commands.

Users belong to groups, the `groups` command can be used to check what groups a user is in. File/directory permissions can be organised for groups. Only system administrators can create new groups and add users to groups.

Users can share files and directories with other users and specify permissions using the `setfacl` command.

The `getfacl` command can be used to report the access controls for specific files/directories.

The `setfacl` command can be run to recurse through subdirectories and can be used to set default access controls on directories created.

If you want other users to read and execute files in your scratch directory, you can use the following commands:

```bash
cd /mnt/scratch/<username>
setfacl -m u:<target-username>:r-x .
```

(Replace `<target-username>` with the USERNAME of the user that you want to share the directory with.)

You can check what access controls there are using:

```bash
cd /mnt/scratch/<username>
getfacl .
```

If there is an existing directory with subdirectories and you want to set the access control to recurse and provide also write permissions in subdirectories, use the following:

```bash
cd /mnt/scratch/<username>
setfacl --recursive -m u:<target-username>:rwx .
```

To change the default so that any new files and directories also have these permissions, use the following:

```bash
cd /mnt/scratch/<username>
setfacl --recursive -m u:<target-username>:rwx,d:u:<target-username>:rwx .
```

For more detailed examples and explanations of Linux file permissions, you can refer to this [Linux File Permissions Guide](https://www.redhat.com/en/blog/linux-file-permissions-explained).


# Data transfer

<!-- For security reasons, this section has been taken offline as it contains hostnames that could pose a cybersecurity risk. We need to identify an appropriate method for securely transferring data in and out of Aire. -->

<!-- TODO: >>>>>>Asked Pasquale what utilities (scp, rsync) etc can be used with University Research data storage eg Isilon<<<<<<< -->

You should make sure any input data required is on your scratch directory before the job starts. And if you need to transfer data elsewhere after a job completes, then the job should save the data in the scratch directory and then you can transfer it as a separate task after the job finishes.

:::{warning}
You should not transfer data in and out of Aire from running jobs. This ties up the compute nodes waiting for the network and is inefficient.
:::

The login nodes on Aire are powerful and have fast connections to the campus network and onward to the JANET network and other universities.
The standard Linux tools are available on the login nodes to transfer data to and from the HPC system. Useful commands are `scp` and `rsync`. You can transfer single files or sets of files, whilst directories can be copied, it can be better to compress files into a single file and transfer that file. This can be achieved using the `zip` command.
The login nodes also accept inbound connections for these utilities from other machines on campus (wired connection), such as your desktop or workstation or departmental servers and storage.

## Using a Terminal

### scp

To transfer data to or from your local machine, `scp` must be run on your local machine, such as in a local terminal, as Aire cannot directly access your machine.

The general format of an `scp` command is `scp /path/to/file/to/copy /path/to/location/to/copy/to` where; "/path/to/file/to/copy" is the path of the file to copy, and "/path/to/copy/to" is the path to copy to. To specify a remote path add `username@remote:` at the start of the path - where `username` is the user USERNAME and `remote` is the address of the remote machine. For example, to copy a files to/from `$SCRATCH` on Aire specify `username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username` (where `username` is your USERNAME and the name of the directory on `/mnt/scratch/users/`). Some example `scp` commands are shown below.

:::{Note}
Currently, you have to connect through the jumphost, rash.leeds.ac.uk, to transfer files to Aire from a local machine that is not on a wired campus network (off-campus connection).
:::

1. Copy from your off-campus local machine to your scratch directory on Aire

```bash
# Copy the file test.dat to a file with the same name in your scratch directory
$ scp -J username@rash.leeds.ac.uk test.dat username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username
```

Directories can be copied in the same way but requires the addition of the `-r` option, which copies recursively.

```bash
# Copy the directory test_dir to a directory with the same name in your scratch directory
$ scp -r -J username@rash.leeds.ac.uk test_dir username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username
```

2. Copy from your scratch directory on Aire to your off-compus local machine

```bash
$ scp -J username@rash.leeds.ac.uk username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username/test.dat .

```

Again directories can be copied using the `-r` option.

```bash
$ scp -r -J username@rash.leeds.ac.uk username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username/test_dir/ .
```

3. Copy data from /nobackup on ARC4 to your scratch directory on Aire

This can be done either remotely, by running a command on your local machine, or the `scp` command can be run on the login node of ARC4 (example below). You will prompted for your Aire password.

```bash
# Copy a file, test.dat, from ARC4 to your scratch directory on Aire
$ scp username@arc4.leeds.ac.uk:/nobackup/username/test.dat username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username/
```

```bash
# Copy a directory, test_dir, from ARC4 to your scratch directory on Aire
$ scp -r username@arc4.leeds.ac.uk:/nobackup/username/test_dir username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username/
```

4. Copy a file, `test.dat`, from your scratch directory on Aire to to the `/home/mydirectory/` directory on a local workstation on campus, from the login node:

```bash
$ scp /mnt/scratch/users/username/test.dat <machine_name>.leeds.ac.uk:/home/mydirectory/
```

Note:

1. you maybe prompted for your workstation password
2. if your login name is different on the workstation and Aire, you will need to add it explicitly:

```bash
$ scp /mnt/scratch/users/username/test.dat <login_name>@<machine_name>.leeds.ac.uk:/home/mydirectory/
```

There are many tools on Windows and MacOS which can provide you with a more GUI-style interface to the HPC system to transfer files. They use the same underlying commands like `scp`, and some users may be more comfortable using them rather than the command line.

### rsync

The `rsync` command is another file transfer command. It is more suitable than `scp` for large file transfers as it enables for interrupted transfers to be continued rather than starting them from the beginning.

There are also a number of additional options that can be used with the `rsync` command, inuding `-v` for verbose, `-a` for archive, and `-n` for a "dry run" which allows `rsync` to do a trial run with no changes made (which is useful for testing things will work).

1. Copy from your off-campus local machine to your scratch directory on Aire

```bash
# Copy a file, test.dat, from a local machine to your scratch directory on Aire
rsync -av -e "ssh -J username@rash.leeds.ac.uk" test.dat username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username/
```

Copying directories works in the same way but requires a trailing `/` after the directory you wish to transfer:

```bash
# Copy a directory, test_dir, from a local machine to your scratch directory on Aire
rsync -av -e 'ssh -J username@rash.leeds.ac.uk' test_dir/ username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username/
```

2. Copying from your scratch directory on Aire to your off-campus local machine

```bash
# Copy a file, test.dat, from your scratch directory on Aire to a local machine
$ rsync -e "ssh -J username@rash.leeds.ac.uk" username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username/test.dat /path/to/local/directory/
```

```bash
# Copy a directory, test_dir, from your scratch directory on Aire to a local machine
$ rsync -av -e "ssh -J username@rash.leeds.ac.uk" username@login1.aire.leeds.ac.uk:/mnt/scratch/users/username/test_dir/ /path/to/local/directory/
```

<!-- TODO: add rclone and other data transfer tools -->


# Data Transfer

You should make sure any input data required is on your scratch directory before the job starts. If you need to transfer data elsewhere after a job completes, the job should save the data in the scratch directory, and then you can transfer it as a separate task after the job finishes.

:::{warning}
You should not transfer data in and out of Aire from running jobs. This ties up the compute nodes waiting for the network and is inefficient.
:::

The login nodes on Aire are powerful and have fast connections to the campus network and onward to the JANET network and other universities. The standard Linux tools are available on the login nodes to transfer data to and from the HPC system. Useful commands are `scp` and `rsync`. You can transfer single files or sets of files, while directories can be copied, it can be better to compress files into a single file and transfer that file. This can be achieved using the `zip` command. The login nodes also accept inbound connections for these utilities from other machines on campus (wired connection), such as your desktop or workstation or departmental servers and storage.

For detailed instructions on data transfer, please refer to the following KB article:

+ <a href="https://leeds.service-now.com/it?id=kb_article_view&table=kb_knowledge&sys_kb_id=dfcc76a9fb3b16909eaffefbaeefdc09&searchTerm=KB0018323" target="_blank">KB0018323 - How to transfer data to and from Aire</a>

Note that the above articles require you to log in with your University account to view.

# Dependency Management

```{note}
This guidance specifically discusses Conda dependency management, which can be used for a range of languages/projects, including Python, R, C/C++, and Rust amongst others.

This does not cover alternative package management and virtual environment solutions like `renv`, `pixi`, or `uv pip`.
```

Good dependency management makes your research computing:

- More reproducible (by recording the exact environment used to generate any set of results);
- More reusable (both by you and by other researchers, by providing a "recipe" to use your code on other systems);
- More robust and unlikely to break due to an update in an imported library.

```{warning}
Please read through this guide even if you use `conda` locally on your machine, or have used it previously on ARC3 or ARC4.

Our guidance has changed: help us to help you make your research more efficient, reproducible, and robust by ensuring you follow the steps below.
```

While there are many options for dependency management for Python, we offer [`miniforge`](https://github.com/conda-forge/miniforge) on Aire as a fast, open-source replacement for Anaconda. The same `conda` commands you are used to using will work, but the default channel for miniforge environments is [`conda-forge`](https://conda-forge.org/docs/), the open source repository, as opposed to the commercial Anaconda repository. The guidance we provide below is specifically for using conda; however, the general principles will also be applicable to other package management systems.

For some packages, you may also need to use `pip`; we detail how this can be done if needed within a conda environment.

## General approach

- **In general, environments should be treated as disposable and rebuildable**: you should be able to tear down and rebuild your environment quickly and easily (of course, some larger environments with complex installations will be an exception to this rule). This means that your `environment.yaml` file should be up-to-date and match your working environment, and should be version-controlled and backed up. We will explain how to effectively use the `.yaml` file below.
- **Export your exact environment as metadata for analysis results**: it is useful to save a snapshot of your environment (into a `.yaml` file) to store along any results or outputs produced in that specific environment. We will show you how to do this below.
- **Environments must be stored in your `home` directory and all research output must be stored in `/mnt/scratch/users`**: misuse of the system can affect performance for **all users** and will lead to your jobs being stopped.

## Create a new environment

In order to create a new conda environment, you need to create an environment YAML file, with the file ending `.yaml`.
A conda `env.yaml` or `environment.yaml` file will look something like this:

```yaml
name: my-env-name

dependencies:
  - python=3.12
  - pytest
  - setuptools
  - blackd
  - isort
  - numpy
  - matplotlib
  - pandas
```

Note that we have pinned `python` in this example, and left the other dependencies free. You can pin as many libraries as you want/need: we will discuss pinned vs. flexible libraries below.

```{admonition} R environment creation
When using conda to install R packages, add r- before the R package name. For instance, to install rbokeh, use `r-rbokeh`. To install rJava, use conda `r-rjava`.
```

If you are creating an R environment, your  file might look like this:

```
name: my-env-name

dependencies:
  - r-base
  - r-tidyverse
```

This is then turned into a conda environment with all the listed dependencies installed by calling the following (from the folder containing the `.yaml` file):

```bash
conda env create -f environment.yaml
```

You can then activate this environment (or use it in a job submission script):

```bash
conda activate my-env-name
```

### `pip` dependencies

If you need to include `pip` dependencies in your conda environment, you can add these to your environment YAML file as follows:

```yaml

name: env-with-pip-dependencies

dependencies:
  - python=3.12
  - numpy
  - matplotlib
  - pandas
  - pip
  - pip:
    - black

```

## Updating an environment or adding new packages

If you want to add a new package that you didn't include in your original `environment.yaml` file, or pin a package to a specific version, you can go and do so within the `environment.yaml` file. Just add any new packages to the list of dependencies, and pin libraries with the `=` notation as in the first example.

Once your `environment.yaml` file is up to date, you can apply the changes to your conda environment:

```bash
conda env update --file environment.yaml --prune
```

The `--prune` argument here clears out old unused libraries and is key to keeping your `.conda` folder a reasonable size. **Please ensure you use the prune command to prevent environment bloat**.

Whereas running `conda install package-name` from within your environment can lead to dependency conflicts (say your env has an older version of `numpy` and you've tried to `conda install` another package that can't support this), updating the environment from the `.yaml` file allows the solver to work through the dependencies at the same time. There may still be conflicts, but many easily avoidable issues will disappear. It also ensures you can rebuild your conda env easily from the file, instead of trying to remember what you installed.

## Exporting a snapshot of your conda environment

Recording dependencies is crucial for reproducibility.
In order to record the exact versions of all dependencies used in your project, from inside your active conda environment, you can run the following export command:

```bash
conda env export > env-record.yaml
```

This can be run as part of a batch job and included in your submission script; please ensure your output files are being saved to `mnt/scratch/users/<your-user-name>/` alongside your other output data files:

```bash
conda env export > /mnt/scratch/users/your-user-name/env-record.yaml
```

**This exported environment file is mainly useful as a record for the sake of reproducibility, not for *reusability*. Your `environment.yaml` file is a far better basis for rebuilding or sharing environments.**

This record will include background library dependencies (libraries you did not explicitly install, that were loaded automatically) and details of builds. This file, while technically an `environment.yaml` file, will likely not be able to rebuild your environment on a machine other than the machine it was created on.

## Exporting your environment for sharing

**If you follow the above steps for building your conda environment from a YAML file, this step should not be necessary. However, if you want to salvage a poorly-maintained environment that you built using repeated `conda install package-name` commands, this allows you to create an `environment.yaml` file.**

From inside your activated environment, you can run the following:

```bash
conda env export --from-history > environment_export.yaml
```

This will export a list of only the libraries that you explicitly installed (and not all the background dependencies), and only the pinned versions you requested. This is not useful as a record of your exact environment, but is a good backup for rebuilding or sharing your environment. **Note that this will not add any pip dependencies.**

To export pip libraries, we need to add some lines of code. Modified from this [conversation on GitHub](https://github.com/conda/conda/issues/9628#issuecomment-1608913117), this code snippet will export your conda and pip dependencies without version numbers (so that the `environment.yaml` file can be used to build a new environment):

```bash
# Extract installed pip packages
pip_packages=$(conda env export | grep -A9999 ".*- pip:" | grep -v "^prefix: " | cut -f1 -d"=")

# Export conda environment without builds, and append pip packages
conda env export --from-history | grep -v "^prefix: " > new-environment.yaml
echo "$pip_packages" >> new-environment.yaml
```

This *should* export a list of your pip dependencies, without pinned version numbers, and add them on to your `--from-history` conda dependencies.
But remember: it is better to keep your `environment.yaml` file current, and update your conda env *from* this file, as opposed to adding packages using `conda install` and then trying to export details to your environment file to track these changes. All of this section can be avoided if you correctly use your `environment.yaml` file to create and update your conda environments.

## Quick conda FAQs

#### Are conda `environment.yaml` files an overly prescriptive approach?

Not unless you are misusing them, and have only ever encountered an `environment.yaml` file produced with the `export` function.

Environment YAML files are exactly as prescriptive as you want them to be: you can pin versions of certain libraries, and leave others flexible.

#### Why can't I just use `conda install` to add packages? Why use a YAML file?

You *can*, but there are a few reasons why you *shouldn't*.

1. Things you install later will be pinned by the versions of libraries installed at an earlier stage, which can lead to dependency conflicts.
2. You can end up with a lot of crud and old unneeded libraries that you no longer use bloating your environment.
3. It is that much harder to rebuild your conda environment, and your `environment.yaml` isn't a true record of the environment. You have to remember to export a flexible `--from-history` version of it any time you make a change.

#### Updating from my YAML file with the `--prune` flag might change versions of packages in my library - isn't this bad for reproducibility?

Yes, updating the entire environment with your `.yaml` file absolutely can update all the libraries, not just the ones you are adding. A few points to this:

1. You should pin any libraries that *can't* change, for example if there is a breaking change or change in behaviour in a newer/older version of one of the libraries.
2. Reproducibility absolutely does not mean repeatedly using the exact same environment pinned to a specific version in perpetuity. Recording a snapshot of your environment along with any results produced by the environment in that state, along with robust tests, ensure reproducibility without trapping you with stale and potentially insecure packages, which leads us to point three...
3. A robust test suite is **essential** for any computational research work, and lets you update packages safely while ensuring your code still produces robust and accurate results.

#### Conda environments are big, what do I do if I run out of space in my home directory?

Conda environments can become big quickly. On ARC3 and ARC4, due to limitations in home directory size, we advised you to move your `.conda` directory over to `/nobackup` if you ran out of room; however, this is an inefficient use of HPC storage and can lead to performance issues. **On Aire, it is essentially that your conda environments live in your home directory, and that *all* research output files are stored on `/mnt/scratch/users` and not in the home directory. Misuse of the home directory for storing job output can cause sluggish behaviour and affect other users, and could lead to your account being suspended.**

There are three steps to solving your conda environment overtaking your home directory storage space:

1. Ensure you are using `--prune` when you update your conda environments to shrink them and remove unnecessary content.
2. Delete environments that are not in active or current use: if you have followed our guidance on building from an `environment.yaml` file, rebuilding at a later point should not be difficult.
3. Request more space: you can ask us to increase your home directory quota. Note however that we will audit your conda usage, and you will not be granted extra space if you haven't followed the guidelines presented here.


# Filesystem Quotas

We use quotas on the filesystems to manage the usage of the space fairly among the users and to try to avoid or reduce situations where a filesystem becomes full. Users have individual quotas on the filesystems, a default quota is set which should work for most users. However, if you feel you need more, then please [submit a Research IT support ticket](https://bit.ly/arc-help) providing reasons why you need extra space.

There are two quantities which the quota system manages, these are the amount of data space and the number of files.

The **space quota** is the number of disk blocks you can use and this is limited to ensure equitable division of the total space amongst the users. The **number of files quota** is to prevent users creating vast numbers of files. Having lots of very small files is very inefficient and greatly slows down workflows. It can also make it impossible to manage the files as commands like `ls` and shell file operations become slower and slower. So to prevent these situations occurring, there is a limit to the number of files you can have (albeit it quite large!).

Default quotas are as follows:

```bash
$HOME=30GB and 1,000,000 files
$SCRATCH=1,000GB and 500,000 files
```

You can request increases to these, but you will need to justify your request.

```bash
$TMP_SHARED=1,000GB and 1,000,000 files
$TMP_LOCAL=500GB, 500,000 files
```

:::{warning}
**Filesystem full situations**

While the quota system does effectively manage the space on the filesystems, most people don’t actually use their full quota all the time, so in order to give as much usable space for everyone, we oversubscribe the quotas. Most of the time this isn’t a problem, but it is possible that the filesystem will become full occasionally.
:::

Note that an HPC filesystem is considered full when the block allocation reaches **90%**. Above this level performance can be severely impacted and your work will run slower and your files may become fragmented.  

If this happens we will take action to relieve the situation, including:

1. Job scheduling will be suspended, new jobs will not start running until the situation is resolved.
2. We will e-mail all users requiring them to urgently review their file holdings and remove older/unwanted files.
3. We will proactively remove files to relieve the space shortage, without warning.

:::{note}
If a filesystem does actually fill up completely, this has a serious impact on any work which is currently running and processes which try to write data to a file are likely to receive a `no space left on device message`. This means that the file you are writing to has been truncated and some data has been lost at the end of the file. Since linux writes data in whole blocks, and also buffers these blocks in memory, the amount of data written to the file may well less than you expected at the time of the error. In general, you should expect the file affected to be invalid, and re-running the job once the space situation is rectified or reverting to an older version of the file will be required.

**This also applies to situations where you exceed your disk space quota, the same warning applies.**
:::

We strongly urge you to periodically review your data holdings and remove unwanted and old files.
You can see what your usage is using the `quota` command:

```bash
quota -s
```

This shows you the number of blocks of disk space you are using and the number of files, for all the filesystems.

To view the amount of data in specific directories, the `du` command can be useful, but note that this can be quite slow as it must scan the directories in question.

```bash
du -hs *
```

This will display a summary of your usage in your current directory, in human readable format.


# HPC architecture

This page covers the basic things you need to know about the cluster architecture.

<!-- ```{contents}
:local:
``` -->

## Overview of an HPC cluster

HPC cluster systems are constructed from a large number of separate computers called nodes. Each node is about equivalent to a high-end workstation or server. They are linked together by HPC interconnect - a technology which allows very rapid communications between the nodes.

![HPC Cluster Architecture](../assets/img/figs/cluster_architecture.jpg)

## Node types explained

There are **5 types of node** in the Aire HPC cluster:

Compute nodes
: Compute nodes are physical systems containing CPU and memory. Each compute node on Aire has 168 cores, which are the physical processing units within a CPU that execute instructions and perform calculations. Having many cores allows many instructions to be executed in parallel. There are also high-memory nodes separate from standard compute nodes for jobs that require a significant amount of memory.

GPU nodes
: A GPU node is simply a compute node that has one or more Graphical Processing Units (or GPUs) installed on it. GPUs can be very powerful and allow certain programs to run faster than they do on CPUs (such as some Machine Learning and Deep Learning tools for AI applications). Programs have to be specially written to run on GPUs.

Login nodes
: These are similar to compute nodes, but they do not run jobs and they are connected directly to the University network. You can connect to a login node via ssh and login to it. You can then create and edit files and programs and run scripts and manage your data. You can also upload and download data from login nodes. You don't use the login node to run your work, just to prepare it and to view the results. However, the login nodes are quite powerful and can be used for data manipulation, pre- and post-processing and for visualisation.

Storage nodes
: These nodes have large disk arrays attached to them, to deal with vast amount of data HPC systems can generate. Often there are multiple nodes and disk arrays which are linked together in to a large parallel filesystem. These parallel filesystems are geared for the very large amounts of I/O which some runs can generate. Storage nodes are not directly accessible by users. The data directories from the storage nodes are mounted on the login and compute nodes.

Admin nodes
: These aren't accessible or visible to users, but they provide the resources and services needed to manage the cluster. For example, they allow system administrators to automatically install and configure the OS on all the nodes and access monitoring features. The [job scheduling system](job_scheduler.md) is hosted on one of the admin nodes.

For more detailed information on the different types of compute nodes, please refer to the [Compute Node Types](../system/compute_node_types.md) section.

## How work is executed on an HPC cluster

While the compute nodes do the heavy computational work, they are not directly accessible by the users. Instead they are under the control of a workload management or [job scheduling system](job_scheduler.md) called [Slurm](https://slurm.schedmd.com/overview.html). The job scheduling system allocates the work to the compute nodes so as to maximise the utilisation of the system.

![HPC Cluster Architecture](../assets/img/figs/job_scheduler.jpg)

Users submit work to the system in the form of jobs, which are simply scripts containing the necessary commands to run the required program(s). A job may be held in a queue until the job scheduler decides to execute it. The running of the work is therefore largely automated and users don't need to stay logged in once they have submitted a job to the scheduling system.

## Optimised for fair-sharing

HPC systems run 24 hours a day, 365 days a year, and must meet the diverse computing needs of many users. Most HPC systems are very popular and run fully loaded most of the time. When you submit a job, it might sit in the queue for a while before it is executed, as other jobs complete and sufficient resources become available. The job scheduling system helps to manage this efficiently and fairly.


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


# Job Scheduler

This page offers a more in-depth overview of the job scheduling system. It is recommended that you familiarise yourself with this content before [getting started](../getting_started/start.md) using Aire.

<!-- ```{contents}
:local:
``` -->

## What is a job scheduler?

A job scheduler - also known as a queueing system or workload manager - is a software tool that implements a batch system on an HPC cluster, allowing many users to submit jobs simultaneously.

The two most popular schedulers in HPC are [PBSPro](https://altair.com/pbs-professional) and [Slurm](https://slurm.schedmd.com/), though there are others, such as [LSF](https://www.ibm.com/docs/en/spectrum-lsf/10.1.0?topic=scheduler-about-lsf-session) and [Grid Engine](https://altair.com/grid-engine/).

## Benefits of a job scheduler

Efficient use of resources
: HPC systems are very powerful and have a huge capacity for work. They are expensive to run too, and consume lot of energy. It is important for us to run the systems as efficiently as possible and to maximise the amount of work they can do. Job scheduling systems can help us optimise for energy consumption, as well as throughput.

Saving users time
: Some user tasks take a long time to run - even more than a day. You might want to run a long connected sequence of runs, or run the same task many times with lots of different parameters. Doing this directly from a PC by hand can become very tedious and error prone. A job scheduling system allows us to automate the running of work so that you don't have to monitor your terminal for hours on end, and can set up complex workflows, leaving it to the job scheduling system to keep things moving.

Fair-sharing
: A job scheduler can be configured to allocate compute resources fairly to different users and groups. For example, a user who has recently submitted a large job may need to wait longer for their job to run than another user who has not recently run a job.

## Which job scheduler does Aire use?

Aire uses the Slurm system, which is used in many other UK University HPC centres. The old ARC3 and ARC4 HPC systems used Grid Engine. Fortunately, it is quite easy for users who are familiar with Grid Engine to transition to Slurm.

```{admonition} Used Slurm before?
Slurm is configured differently at different HPC centres, to meet the differing requirements of their users. However, most of the commands and parameters you use on your jobs will be the same or similar.
```

## Submitting a job to the scheduler

To submit a job to the scheduler, you must first create a job script to run your program. In the script, you will specify any particular data or parameters needed to run your program. You can then submit the script to the job scheduling system using Slurm's [`sbatch`](https://slurm.schedmd.com/sbatch.html) command for batch mode or [`srun`](https://slurm.schedmd.com/srun.html) command for interactive jobs. In your script or run command, you will include some information for the scheduling system to inform it about the size and shape of the job, and the resources it will need to run.

Some commonly used parameters are:

```{list-table}
:header-rows: 1
* - Parameter
  - Function
* - `--job-name=<name>`
  - Specifies the job name to be displayed. Use a meaningful name to distinguish between different jobs.
* - `--time=<T>` where `<T>` has format `hh:mm:ss`
  - Specifies the walltime (the amount of time you expect the run to take). Add a small safety margin (e.g., 20% extra) to account for variation. Over-estimating walltime may delay the start of your job.
* - `--cpus-per-task=<ncpus>`
  - Specifies the number of CPUs your job will use. Serial jobs use only 1 CPU, while parallel jobs can use more. It is important to specify this correctly. Slurm defaults to a single CPU if this parameter is omitted.
* - `--mem=<size>[units]`
  - Specifies the total amount of memory required for the job. Avoid over-estimating as it may delay your job and/or deprive other jobs of memory.
* - `--gpus=[type:]<number>`
  - Specifies the number of GPUs required. If your code uses GPUs, you will need to request this.
```

For the full list of options, please refer to the [Slurm documentation](https://slurm.schedmd.com/sbatch.html)

```{seealso}
To learn more about writing job scripts for different types of job, and to see examples, check out [Job Types](../usage/job_type.md) and [Job Examples](../usage/job_example.md).
```

## After a job is submitted

Once it is submitted, Slurm looks for a space to fit your job into, and if space is free, will start the job running immediately. However as many other users will often be using the system too, the job is likely to be placed in a queue, waiting to run when resource become available as other jobs finish.

```{tip}
Check the status of your job using the [`squeue`](https://slurm.schedmd.com/squeue.html) command.
```

The time you wait can vary, depending on how much work there is on the system and how much is waiting to run. Your jobs will be assigned to a partition, which is part of the apparatus used by the scheduler to manage the work. Which partition your job goes into is not important in terms of how quickly the job may run.

When resources become free, Slurm will run your job and when it completes, it will return the output file to your directory.


# Job Types

## Batch jobs

The vast majority of jobs that run on Aire will be batch jobs. These are submitted via a job script, which is a shell script (file ending `.sh`), containing the commands to run your job, alongside instructions for the job scheduler (Slurm), detailing the resources required. Slurm will then allocate that job in a position in the job queue, depending on a fair share policy. This policy is not first-come-first-served; resources are allocated fairly between different faculties and users. At a bare minimum, the job script must specify how long the job needs to run for. Unless otherwise directed, Slurm will default to the following settings:

- 1 CPU core
- 1GB memory
- Use of standard compute node pool (No GPU access)

### Writing job scripts

We encourage users to write their job submission scripts using text editor tools available on Aire such as:

- `nano` (recommended for beginners)
- `vim`
- `emacs`

The basic approach to create a new job submission file on HPC would be ```nano job_submit.sh``` or `vim job_submit.sh`. This opens the new empty file in the text editor ready for you to write its contents.

:::{warning}
Job scripts written on Windows computers contain different invisible line ending characters that lead to job submission failures such as `/bin/bash^M: bad interpreter: No such file or directory`.
You can use the command `dos2unix job_script.sh` on Aire to convert your script to the correct line endings.
:::

The [Job Examples](../usage/job_example.md) section contains a collection of job scripts for a range of uses, but a simple demonstration script is provided below. In this example named `job_script1.sh` we are requesting an hour of time, 1GB of memory, and a single CPU core to run an example binary file `example.bin` in the current directory.

```bash
#!/bin/bash
#SBATCH --job-name=simple_job   # Job name
#SBATCH --time=01:00:00         # Request runtime (hh:mm:ss)
#SBATCH --mem=1G                # Request memory
#SBATCH --ntasks=1              # Number of tasks
#SBATCH --cpus-per-task=1       # Number of cores per task

# Load any necessary modules
module load <module_name>

# Execute your application
./example.bin
```

The job script specified above includes a number of lines that request some amount of compute resource for our job. This is defined by the syntax `#SBATCH <option>`. These lines are commented out of the shell script but are read by the scheduler to determine how much compute resource is required and thus how to fit the job into the queue. A {ref}`submission-options` is available below, and at the [Job Examples](../usage/job_example.md) page.

### Using the queue

To submit the job script, we use the command `sbatch`:

```bash
$ sbatch job_script1.sh
Submitted batch job 42
```

This returns some text to confirm our job has been submitted and provides us with the job's unique ID number (in this case 42). Arguments can be submitted to Slurm upon job submission, for example:

```bash
$ sbatch -t 1:00:00 job_script1.sh
Submitted batch job 42
```

Commands passed to Slurm in this way will override those in the job script.

We can view the queue status using `squeue`:

```bash
$ squeue
JOBID   PARTITION   NAME        USER     ST  TIME NODES  NODELIST(REASON)
42      nodes       simple_job  exuser   R   0:25 10     node[01-10]
43      nodes       other_job   exuser   PD  0:00 16     (resources)
```

Currently running jobs are identified with an `R`; jobs still in the queue show `PD`.

Jobs can be cancelled using `scancel <JOBID>` (in our case, `scancel 42`). Users are only able to cancel their own jobs.

## Task arrays

### When to use task arrays

Situations often arise when you want to run many almost identical jobs simultaneously, perhaps running the same program many times but changing the input data or some argument or parameter. One possible solution is to write a Python or Perl script to create all the job scripts, and then write a BASH script to execute them. This is very time consuming and might end up submitting many more jobs to the queue than you actually need to. Thankfully, this problem is made much easier via Slurm's task array feature:

- Only a single `sbatch` command is issued, and only a single `scancel` command would be required to cancel all jobs
- Only a single entry appears after checking `squeue`
- It is much easier for the user to keep track of their jobs

### How to use task arrays

The easiest way to think of a task array is as a job script with a built-in FOR loop. It makes use of an environment variable created by Slurm - `$SLURM_ARRAY_TASK_ID`. Consider the following job submission script (task_array_script.sh) using a Conda environment:

```bash
#!/bin/bash 
# Request 1 hour runtime
#SBATCH --time=01:00:00

# Tell Slurm that this is an array job, with tasks numbered from 1 to 100
#SBATCH --array=1-100

# Load any necessary modules
# e.g. using a conda environment
module load miniforge
conda activate my_environment

# Run the job, passing in the input and output filenames
python –i ~/input/input.$SLURM_ARRAY_TASK_ID –o ~/results/out.$SLURM_ARRAY_TASK_ID
```

This array job would be submitted as normal using `sbatch task_array_script.sh`.

In this example, input files would be read from the `input` directory, and take the form input.1, input.2, input.3 etc. The program would create output files out.1, out.2, out.3 etc in the `results` directory.

## Interactive jobs

It is also possible to runs jobs in interactive mode on Aire. This means rather than queueing for your job to run on the batch system you request resource for an interactive sessions via the shell.

:::{warning}
We strongly discourage users from using interactive sessions for interactive code development using platforms like jupyter, spyder or Rstudio. Code development should be done before deploying code on the HPC.
:::

Interactive jobs can be started using the `srun` command, as follows:

```bash
[username@login1[aire] ~]$ srun -t 01:00:00 --pty /bin/bash
[username@node016[aire] ~]$
```

Note that it is required to specify a requested runtime, but the scheduler will otherwise adopt the same default resources as for batch jobs. If the requested resources are available, the session will start immediately. If not, the session will immediately exit. Note that once the session has started the prompt changes to show that the interactive session is now running on a specific compute node (in this case, `node016`).

:::{note}
If you have made changes to your environment on the login nodes these will not be preserved when connecting to an interactive session and you will be required to rerun `module load` commands. Connecting to an interactive session creates a new login shell, which means any commands in your .bashrc are executed when you connect.
:::

## GPU

Aire includes general-purpose GPU facilities for GPU-accelerated code. Aire has 17 dedicated GPU nodes, each with 3 NVIDIA L40S GPUs. Login nodes are equipped with entry-level NVIDIA A2 GPUs, which is useful for configuration purposes - note that login nodes should not be used to run jobs in order to skip the queue or work around restrictions for interactive jobs.

### Requesting use of GPU nodes

GPUs can be requested with: `--partition=gpu` and `--gres=gpu:<number>`. For example, a basic submission script requesting a single GPU might look like:

```bash
#!/bin/bash 
#SBATCH --time=01:00:00     # Request runtime (hh:mm:ss)             
#SBATCH --partition=gpu     # Request the GPU partition
#SBATCH --gres=gpu:1        # Request a single GPU

# Load any necessary modules
# module load <module_name>

# Run the job
./example.bin
```

GPUs are also available in interactive mode. For example, requesting an interactive session with two GPUs:

```bash
[username@login1[aire] ~]$ srun -t 01:00:00 -p gpu --gres=gpu:2 --pty /bin/bash
[username@gpu007[aire] ~]$
```

Here, note again that the prompt has changed to tell us that we are now running on a dedicated GPU node.

To use the GPU hardware you will need to ensure the NVIDIA CUDA toolkit module is loaded into your environment, *before* compiling or running code. This can be done explicitly with `module load cuda`, or via an environment manager such as conda (via miniforge on Aire). Again note that changes made to the environment on login nodes will not carry over to compute nodes, so this will be need to be done in the job submission script or after starting an interactive session.

## Large-memory jobs

In extreme cases, it may be required to use more memory than is available on the standard compute nodes (4601 MB per core, or around 773GB total across 168 cores). Aire is equipped with two high-memory nodes for such situations; each node is equipped with 2.32 TB of memory across 168 cores (13.8GB per core).

High-memory nodes are requested in a similar manner to GPU nodes, by using: `--partition=himem`. For example:

```bash
#!/bin/bash
#SBATCH --time=01:00:00       # Request runtime (hh:mm:ss)          
#SBATCH --partition=himem     # Request high-memory node

# Load any necessary modules
module load <module_name>

# Run the job
./example.bin                 
```

(submission-options)=

## List of Slurm submission options

Below is a list of currently available options for submissions to Slurm on Aire. This list is likely to grow as we add and update functionality. Please see the [Job Examples](../usage/job_example.md) page for demonstrations of these options in use.

| Option | Description | Default |
| :---- | :--- | :---- |
| `--time=d-hr:min:s`<br>`-t d-hr:min:s` | The requested wall clock time (amount of real time needed by the job). Failure to include this parameter will result in an error message. | Required |
| `--mem-per-cpu=<size>[units]` | Amount of memory requested **per CPU**. Units are specified with K, M, G, i.e., request 1GB with `--mem=1G`. | 1GB |
| `--mem=<size>[units]` | Total amount of memory allocated for the **entire job**, regardless of the number of CPUs. | |
| `--cpus-per-task=<number>`<br>`-c <number>` | Request a number of CPU cores per task, for threaded applications. By default, Slurm will allocate a single processor per task. | 1 |
| `--nodes=<number>`<br>`-N <number>` | Number of nodes requested (for MPI jobs) | 1 |
| `--ntasks=<number>`<br>`-n <number>` | Advises Slurm on how many tasks the job script is expected to try to start. Default is a single task per node, but changing the `--cpus-per-task` option will change this default. | 1 |
| `--ntasks-per-node=<number>` | Requests a number of tasks to be executed on each node. If used with `--ntasks`, `--ntasks` will take precedence, and `--ntasks-per-node` will be treated as a *maximum* count of tasks per node. | Must be specified for MPI jobs |
| `--job-name=<jobname>`<br>`-J <jobname>` | Specify a job name. | Name of the submission script. |
| `--partition=<name>`<br>`-p <name>` | Requests use specific partitions, for example, `gpu` and `himem`. | |
| `--gres=gpu:<num-gpus>` | Requests the use of GPU nodes and specifies the number of requested GPUs. Aire has 14 GPU nodes, each with 3 cards. This needs to be used with the GPU partition. | |
| `--array=<start>-<stop>`<br>`-a <start>-<stop>` | Produce an array of sub-tasks (loop) from `<start>` to `<stop>`, using the `$SLURM_ARRAY_TASK_ID` variable to identify the individual sub-tasks.  | |
| `--mail-type=BEGIN,END` | Request an email to be sent at the beginning and end of a job to the owner. | |
| `--mail-user=username@leeds.ac.uk` | Specify user email for `--mail-type` option. | User's email address |
| `--help`<br>`-h`| Display a list of help information, then exit. | |


# Linux User Environment

This page covers some basic information about the user environment on Aire.

```{admonition} New to Linux?
To use Aire successfully, you should have some experience using a Linux-based command line interface (CLI). If you are new to Linux systems, check out [Training](https://arc.leeds.ac.uk/courses/) for courses and other learning resources offered by the [Research Computing](https://arc.leeds.ac.uk) team. 
```

## Environment variables

Aire is built on Linux. The user environment on Linux systems makes heavy use of environment variables. For example this is how the [module system](modules_and_applications.md) works. The modules set up or modify environment variables which affect the environment of your jobs.

In addition to the standard Linux variables, Aire provide some additional ones:

```{list-table}
:header-rows: 1
* - Variable
  - Description
* - `$HOME`
  - User's home directory, a permanent storage location. Equivalent to `~/`.
* - `$SCRATCH`
  - Shared scratch directory, high-performance storage ideal for large files or datasets actively being processed.
* - `$TMP_SHARED`
  - Flash on Lustre, high-performance NVMe storage for temporary data during job execution.
* - `$TMP_LOCAL`
  - User's local storage on compute nodes, for temporary files accessible only during job execution. Equivalent to `$TMPDIR`.
```

:::{note}
When you load a [module](modules_and_applications.md), additional variables are added to your environment.
:::

:::{seealso}
Check out [Storage and Filesystems](storage_filesystem.md) for an overview of the storage system on Aire, or, for more comprehensive user information, check out [File and Data Management](../usage/start.md).
:::

## Tailoring your environment

There are two Linux files which you can use to tailor your environment:

`.bashrc`
: Used exclusively for defining shell functions and sourced for every new shell which is spawned. It should not be used for updates to your environment, or for executing any commands.

`.bash_profile`
: Executed at the start of each new login session, and at the start of each batch job. If you wish to set up a tailored environment just for yourself, this is where you should do it. Any path and environment variable settings in `.bash_profile` will be automatically exported to all the child processes in that particular  job or session.

:::{warning}
**DO NOT** include module load commands in `.bash_profile`. Doing so can cause unintentional conflicts with modules you load in your run scripts.

If you do this and then request support from the [Research Computing](https://arc.leeds.ac.uk/) team, you will be asked to remove them first.
:::


# Modules and Applications

This page provides an overview of how software applications are managed on Aire.

## Module system explained

Aire uses a *module* system for managing software applications - a common practice in HPC clusters. A module system simplifies the use of different software and different *versions* of the software, which can quickly become complicated and lead to a loss of performance. With a module system, many users can access multiple different versions of a software application safely and conveniently.

## Installing and managing modules

Popular and common software applications are installed and managed centrally by the [Research Computing](https://arc.leeds.ac.uk/) team. This approach not only saves users time and effort, but also makes sure that the installed applications have the correct optimisation for the hardware of the system and do not interfere with each other (different applications often have files or libraries with the same name, for example). It also allows the Research Computing team to limit the availability of some modules to specific user groups - groups using licenced software, for example.

```{admonition} Requesting new modules
:class: note
You can request new modules by submitting a [Research Computing Query](https://bit.ly/arc-help) giving details about your requirements. Requests will be assessed for suitability to be a shared application. Most open source applications can be incorporated, and commercial applications can be supported with appropriate licenses.
```

## Using modules

Users can list, load and unload modules using the `module` command:

List currently available modules:

        $ module avail

Load a specific module:

        $ module load <module>

Unload a module (useful for avoiding module conflicts and for workflow separation):

        $ module unload <module>

:::{seealso}
For a more complete guide to using modules and managing reproducible environments on Aire, check out [Software on Aire](../software/start.md).
:::


# How to get support

There are number of resources available to get help with using the HPC system.
Firstly this documentation area, and the FAQ. Please consult these before contacting us.

<!-- - You can contact the Research Computing team via [TEAM - HPC Upgrade - ARC to AIRE](https://teams.microsoft.com/l/team/19%3ASTr5OAmdRtIZDouZIGHsk6oH4XWmyHPU6a1lgtQffRI1%40thread.tacv2/conversations?groupId=94592ead-d37d-42b5-abc8-ca508bf21159&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb)
- The Research Computing team have a [shared e-mail box](mailto:rcteam@leeds.ac.uk). -->

You can open a [Research IT support ticket](https://leeds.service-now.com/it?id=sc_cat_item&sys_id=7587b2530f675f00a82247ece1050eda) in the IT ServiceNow system.

## RSE

The Research Software Engineering (RSE) team is an important and essential part of the HPC and Research Computing ecosystem at the University. Their primary role is to provide support for research projects where there is a large computational component. They are able to give advice about planning your project and its computational requirements. But more importantly they can collaborate with you to perform major software and workflow development, including programming reviews, performance analysis, code modernisation and refactoring. The RSE team has its own website [here](https://arc.leeds.ac.uk/).

The RSE team also hosts a [Research Computing Community](https://teams.microsoft.com/l/team/19%3ADhcafsOyYnWotrwqTZkjDpRhSp7Cemz4qQpZfk7G5v01%40thread.tacv2/conversations?groupId=1ff8cb55-a479-4202-9dc4-a97891c03f42&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb), bringing together a broader network of individuals using HPC and engaging in research software development. If you're interested in HPC or research software development, we warmly invite you to join this community on Microsoft Teams.

## RIE

The Research Infrastructure Engineering (RIE) team also contributes to the HPC and Research Computing ecosystem at the University.

<!-- TODO: What does the RIE team do? -->
<!-- TODO: How to contact the RIE team? -->



# System Overview

The Aire HPC system has been designed with a scalable architecture capable of supporting a wide variety of research applications. As of February 2025, the system consists of 52 standard compute nodes and 2 high-memory compute nodes, each equipped with 168 cores, providing a total of 9,072 cores. It also includes 28 GPU nodes, each containing three NVIDIA L40S GPUs, offering a total of 84 GPUs. Aire provides a generous amount of local storage to support the demands of large-scale HPC workloads.

:::{note}
Before diving into the Aire HPC system, it's important to have a basic understanding of its architecture and capabilities. This will help you make the most of the resources available and ensure efficient use of the system.

Explore the sections below to learn more about Aire:

```{tableofcontents}


# Using Aire

Aire is the University of Leeds HPC facility designed to support research computing needs. This guide covers the essential aspects of using Aire effectively.

This section contains detailed information about:

- **Job Types**: Understanding different types of jobs and how to submit them on Aire
- **Job Examples**: Practical examples and templates for common job submission scenarios
- **File and Data Management**: Guidelines for storing, transferring, and managing your research data
- **Dependency Management**: How to handle software dependencies and environment modules
- **Containers**: Using containerisation technologies like Singularity/Apptainer for reproducible research

Each topic has its own dedicated section with detailed instructions and examples. Use the navigation menu to explore specific topics or follow the sections sequentially for a comprehensive understanding of Aire's capabilities.


# File and Data Management

Managing your files and data effectively is crucial for successful work on Aire. This section covers the essential aspects of data handling on the HPC system:

- **Storage Overview**: Understanding the different storage locations and their purposes
- **File System Quotas**: Managing your allocated storage space
- **Data Transfer**: Methods for moving data to and from Aire
- **Data Sharing**: Options for collaborating and sharing data with other users

For detailed information about each topic, please refer to their respective sections.


# Software on Aire

## Modules

Popular and common application programs are installed centrally by us. These are managed by the module system.
By installing centrally we save (many) users the time and effort of doing it themselves. We also make sure that the applications we install have the correct optimisation for the hardware of our system, giving the best possible performance.
We use the module system because it allows many different applications to be available for use, without them interfering with each other (often different applications may have files or libraries with the same name for example). It also allows us to have different versions of the same application installed at the same time. This is very important a it allows users to move to new versions of applications at their own pace and at a convenient time for their work. You can even use different versions on different projects at the same time.

You see see the applications we currently have installed by using the `module avail` command. To use a centrally installed application, use the `module load <modulename>`  command.  eg. `module load eclipse`. This makes the `eclipse` application and libraries available to the job or session by setting up appropriate paths and environment variables. You need to include the appropriate module command for every job that needs it. The settings do not persist between jobs or sessions, or from an interactive session to a batch job.

:::{note}
You should not include module commands in your `.profile` or `.bashrc` files. You need to put the module command in your job script. There are good reasons for this, firstly to avoid conflicts between what might be in your `.profile` and your jobs script and secondly to allow you to choose different applications and different versions of applications in different jobs you might run.

We are not be able to support queries from users where modules are loaded in this way.
:::

Example of using module and running an application:

```bash
 module load eclipse
 cp $HOME/myeclipseruns/trial3/eclipsedata .
 eclipseprog < eclipsedata
```

Each module can have several versions for a given application. One of them will be the default version. We recommend you use the default version in general. This will be a current version and if bug fix versions of the application come out, we will often switch the default version to be the bug fix version so that you avoid running using buggy versions. The default version of the module is usually named simply as the application name, eg `module load eclipse`. Other versions can be accessed explicitly, for example if we make a new version available for users to try out. Eg module `load/eclipse/version2`.

You can usually use the same job script for the new version as the old version, simply  by updating the module load command in the script. The name of the application itself and its associated files doesn’t usually change between versions. Eg.

```bash
 module load eclipse/version2
 cp $HOME/myeclipseruns/trial3/eclipsedata .
 eclipseprog < eclipsedata
```

<!-- Documentation for centrally installed modules should be put here -->
<!-- It's already here! (above) -->

<!-- 4 categories, applicationa, compilers, libraries, tools -->
<!-- 1 section per category -->

<!-- For each category. one page per module -->
<!-- Please try to include a simple example of how to run the application. -->
<!-- TODO: add list of modules - one page per module -->

Many users of HPC systems have their own code, or they work with code which is created and managed by their research group. We provide all the programming tools and environments that you need in order easily work with your own code. We use the `module` system for this in a similar way to the way we do for standalone applications. The different programming environments are provided in different modules, which you load according to your needs. We support multiple versions of each so that you can choose which version to use as appropriate. For example

```bash
module load fortran
```

will load the fortran compiler and its associated libraries, to enable you to compile fortran code and to run fortran binaries.
Sometimes you may need to load more than one module, for example if you need additional libraries as well. Eg:

```bash
module load fortran scilib
```

You should check that the combinations you use are appropriate, but checking in the application specific section of this documentation.
Note that you should load the same modules in your run script and you did when you compiled your code. This makes sure that you don’t have any version conflicts.

:::{warning}
Again, as with applications modules, you must not load modules for programming environments in your .profile or .bashrc files - this is a recipe for disaster.
:::


# Storage and Filesystems

Aire has a large amount of local storage to support the demanding I/O characteristics and data volumes needed by HPC workloads. There are several different storage areas which are tuned for different I/O characteristics and usage patterns. By having different areas we can support the different types of I/O required for various parts of HPC workloads.

:::{seealso}
For more information about the different storage areas and when to use them, check out [File and Data Management](../usage/file_data_management/start.md).
:::


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

# Training courses

To effectively use an HPC system like Aire, you’ll need certain skills, starting with a basic understanding of the Linux command line (the shell). This knowledge is essential for preparing and manipulating data, code, and scripts, as well as managing your work on the system. Familiarity with the Linux shell is a prerequisite for accessing Aire. If you’ve used other HPC systems before, you likely already have most of the necessary skills.

As you progress in your use of HPC, more advanced Linux skills may become necessary, including scripting and tools like `grep`, `awk`, and `sed`. If your work involves developing or maintaining code, proficiency in relevant programming languages will also be beneficial.

We offer regular training courses at the University, as well as access to courses hosted online or at other institutions. The curriculum and current course schedule are available [here](https://arc.leeds.ac.uk/courses/).

For additional learning, we recommend the following external training resources:

[Software Carpentry - The Unix Shell](https://swcarpentry.github.io/shell-novice/)

<!-- TODO: Add more external training links -->
