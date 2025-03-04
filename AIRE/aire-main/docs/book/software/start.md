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
