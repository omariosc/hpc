# Data Transfer

You should make sure any input data required is on your scratch directory before the job starts. If you need to transfer data elsewhere after a job completes, the job should save the data in the scratch directory, and then you can transfer it as a separate task after the job finishes.

:::{warning}
You should not transfer data in and out of Aire from running jobs. This ties up the compute nodes waiting for the network and is inefficient.
:::

The login nodes on Aire are powerful and have fast connections to the campus network and onward to the JANET network and other universities. The standard Linux tools are available on the login nodes to transfer data to and from the HPC system. Useful commands are `scp` and `rsync`. You can transfer single files or sets of files, while directories can be copied, it can be better to compress files into a single file and transfer that file. This can be achieved using the `zip` command. The login nodes also accept inbound connections for these utilities from other machines on campus (wired connection), such as your desktop or workstation or departmental servers and storage.

For detailed instructions on data transfer, please refer to the following KB article:

+ <a href="https://leeds.service-now.com/it?id=kb_article_view&table=kb_knowledge&sys_kb_id=dfcc76a9fb3b16909eaffefbaeefdc09&searchTerm=KB0018323" target="_blank">KB0018323 - How to transfer data to and from Aire</a>

Note that the above articles require you to log in with your University account to view.