![Repo URL](./qr-code.png)

# MONAI/JADE Event
These are the resources for the MONAI/JADE event on 24th June 2024 at LIHE, London.

## Install Miniconda

To install Miniconda and setup a `monai` environment, use the following in the login nodes:

```bash
wget 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh'
bash Miniconda3-latest-Linux-x86_64.sh -b -u -p ~/miniconda3
./miniconda3/bin/conda create -n monai numpy\<2 python\<3.12
./miniconda3/envs/monai/bin/pip install monai[nibabel,pillow,ignite,fire]
```

NB: important to install Numpy 1.* and not 2.0.

To download the MONAI Apptainer image: 

```bash
wget 'https://emckclac-my.sharepoint.com/:u:/g/personal/k1077505_kcl_ac_uk/EVKPVgenB0xDof_PmufBBT0B1yzpz528PYLJx0H6uC5OBQ?download=1' -O monai.sif
```

You may have to download the file locally through your browser first by following that URL, then upload to JADE.

## Accessing JADE Files

The easiest way is to send files back and forth with `scp`. An alternative is to use `sshfs` to mount one's home directory locally and move files around this way. Other GUI programs for various operating systems may help with this as well. On Windows, `sshfs` can be had here: https://github.com/winfsp/sshfs-win This requires installing a number of things per the README file but it does work. 

## Jupyter on JADE

You can run Jupyter(lab) on JADE, however you have to choose a port that's unique (which is trial-and-error) and forward that port to your local machine. To install Jupyterlab through Miniconda:

```bash
./miniconda3/envs/monai/bin/pip install jupyterlab
```

Next choose that port no one else is using (eg. 8881). When you log into JADE through ssh you would include `-L 8881:8881` to forward that port to your local machine. You can then access Jupyterlab through the `localhost` link provided in its output when started.

When you launch Jupyterlab you'll specify your port (eg. 8881):

```bash
./miniconda3/envs/monai/bin/jupyter-lab --port 8881
```

You'll get output when running this, eventually links will be given for logging in after "Or copy and paste one of these URLs:".

## Servers on JADE

It's recommended not to use VSCode or PyCharm ssh connections to JADE which run servers on the head nodes. These track changes constantly and slow down the file system. Experiment tracking tools like wandb do the same and should also be avoided.
