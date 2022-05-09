Title: Getting started with Computational Research with Python (for researchers, or generally)
Date: 2022-5-4
Category: Coding
Tags: virtualenv, python
Slug: setup-python
Authors: Adam Li
Summary: A short walkthrough of setting up for Python development.

# Why Python?

Python is easy to use, easy to read and does not require the user to actually "type" all variables beforehand. "Typing" all variables means explicitly writing in your program that a variable is an "integer", or a "character", or something more exotic. This makes Python technically "slower" than something like C++, but nowadays that's not a huge concern for most applications.

Python is also super easy to install and work with assuming you have a setup correctly. That is what this blog post is devoted to!

# Basic Command-Line Actions

Some people find programming overwhelming because sometimes you need to use the [terminal](https://www.makeuseof.com/tag/beginners-guide-mac-terminal/). In reality, one only needs to know a few basic commands to get started! You can google everything else along the way. Open up your terminal and you can play around with the following commands:

## Querying the current directory
To see what directory you are in:
```
pwd

# example output says I'm in the Documents folder
> /Users/adam2392/Documents/
```

If you want to list all the files in your current directory:
```
ls 

# For example, I have two things in my current directory
> Zoom
> test_data.txt
```

## Moving around your computer

To go into a folder within your current directory:
``` 
cd <directory name>
```
For example, I might do `cd Zoom` to go into the ``Zoom/`` folder inside my Documents directory.

To change directories and move one directory up.
```
cd ..

# now if you run pwd again...
pwd

# you should be one directory level higher
> /Users/adam2392/
```

In some cases, you want to get back to your root directory, so this is useful:
```
cd ~
pwd

# this is my root directory
> /Users/adam2392
```

And... that's probably all you need to know to move around your file system! The rest you can google and search stackoverflow.com

# Installing Python (I recommend Conda for first-time users)

Okay, now you're convinced that Python is a great tool to program in and do research with. When you use a Mac, or Ubuntu system, a basic Python version comes pre-installed usually! You can use your terminal to do basic command-line actions.

```
which python

# example output you might see on your terminal
> /Users/adam2392/bin/python
```

## Virtual Environments (aka Managing Python packages for different projects)
Now, in projects, you generally will want to use what's known as a "virtual environment". This is just a fancy term for installing Python separately for different projects. The reason you want to do so is because there are many 3rd party libraries that you might want to install, which can possibly clash. This helps keep a separately managed set of Python packages per project. You can do this by installing [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Conda is a package-manager that handles all this for you and provides some command-line tools for you to install things!

You can follow the above link to install conda. If you have Mac, you can easily install it using [Homebrew](https://formulae.brew.sh/cask/miniconda).

Once you've install conda, you should be able to restart your terminal and type in the following:

```
conda --version

# for example, I have installed version 4.12.0
> conda 4.12.0
```

## Setting up your virtual environment
When setting up a virtual environment, you can use the command-line terminal again, now with the `conda` software installed, you can use `conda` commands.

You will first create a new environment as follows:

```
# conda create -n <name of the environment you want to create> python=<optionally specify the python version>
conda create -n my_project_name python=3.9
```

Once you follow the prompt and the environment is created, you can "activate" it, so that way all Python commands occur through this virtual environment.

```
conda activate my_project_name

# this command should now show you where the python is called from
which python
# for example, my output is, incdicating I'm using python
# from the virtual environment named "causalx64"
> /Users/adam2392/miniconda3/envs/causalx64/bin/python
```

You can install additional packages now! For example, most scientists using Python
will need `numpy` and `scipy` for crunching linear algebra.

```
# you should be within your virtual environment if not already
conda activate my_project_name

# installs numpy and scipy within your virtual environment
conda install numpy scipy
```

Congrats! Now you can create virtual environments, activate it, and then install packages for the sake of managing software for your Python projects!

# Setting up where you code (VSCode)
Now that you've worked on the terminal, you're probably tired of reading and copying and pasting commands. Well, the next step is the last one before you get coding!

I advocate for the usage of a code-editor application that is solely designed and built to help people write and test code. It's 2022 and I think [Visual Studio Code (VSCode)](https://code.visualstudio.com/download) is the best free code editor on the market. Follow the link to download VSCode.

Once you have installed VSCode, you can link the "Python interpreter" to your earlier setup Python virtual environment (managed by conda). This allows VSCode to "run Python" through your specific Python virtual environment. You can then run Python files directly inside VSCode and install packages separately using your conda environment!

Follow this [link](https://code.visualstudio.com/docs/python/environments) to see how.

Now that you have VSCode setup, you can start coding!

# Extra Notes

I highly suggest you also start learning how to perform version control. See [version control post]() to see a good framework on how.