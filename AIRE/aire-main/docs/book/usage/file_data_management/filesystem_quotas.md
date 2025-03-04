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
