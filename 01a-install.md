# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Command | Result
====== | ====
python | Python 3.6.3 |Anaconda, Inc.| (default, Oct 13 2017, 12:02:49) 
ipython | IPython 6.1.0 -- An enhanced Interactive Python.
ipython notebook | [I 16:19:43.360 NotebookApp] The Jupyter Notebook is running 
spyder | Spyder started... IPython 6.1.0 -- An enhanced Interactive Python.


Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

**Confirmed**

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

---

### Q1. Python Version 2 or 3

**Course material for the bootcamp is compatible with Python versions 2.7 and 3.0. All HackerRank Python pre-work is configured for Python 3 only.  Therefore, Python 3 is the recommended version.**  

Did you install Python 2 or 3? Why?  

To prepare for the bootcamp, I installed Anaconda for Python 3 in a Linux VM, because of the recommendation from Metis that I received prior to the recent One-Day workshop on Python.  For that workshop, I installed Anaconda for Python 3 on Windows (older laptop).  Prior to that most of my prep work via HackerRank was done with a Miniconda installation I'd put on my linux box at home.  That was Python 2.  I chose Python 2 because my first reason to install Anaconda was to get Jupyter support to copy and modify someone else's notebook built for Python 2.

### Q2. Which Python Version Installed   

How can you check the version of Python installed if you happen to be on an unfamiliar computer?

''' bash
$ python -V
'''

Or sometimes just
''' bash
$ ls `which python`
'''
 
The above is probably the fastest way.  But it assumes a system with both Python 2 and Python 3 with symbolic links set up to handle things.  This IS common practice at the moment.  Indeed, it even works for the Anaconda installation.  But it wasn't the case a few years ago... and one has to imagine that EVENTUALLY Python 2 will fade.

