# Getting Setup for the Workshop

## Step 1: Installing Python (Anaconda)

The Python ecosystem consists of a lot of software packages that
bring extended functionality and high productivity straight away.
To manage these packages it is **strongly** recommended that you
install the [Anaconda Python Distribution](https://www.anaconda.com/products/individual)

This enables you to get access to the majority of packages you
will need to do your work without any configuration etc.

You can [download the latest from here](https://www.anaconda.com/products/individual#windows)

Please follow the following Installation Guides to install `Python 3.8`
on your platform:

1. [macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
2. [Windows](https://docs.anaconda.com/anaconda/install/windows/)
3. [linux](https://docs.anaconda.com/anaconda/install/linux/)

```{note}
If you have an `M1` based mac you will need to install using Rosetta2 emulation. A handy [blog post](https://vineethbharadwaj.medium.com/setting-up-anaconda-navigator-spyder-jupyter-python-environments-on-macbook-with-m1-chip-for-2a4b9849c1ec) details some additional steps
to sort out any possible issues using `terminal`. Please let me know if you have any issues.
```

```{note}
If you are a `windows` user and would like access to the broader `linux`
based tools we have had a lot of success using [windows subsystem for linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
which gives you to a `lot` of powerful tools via `terminal` based workflows.
```

## Step 2: Running a `Jupyter` Notebook

[Jupyter Notebooks](https://jupyter.org) have become a standard tool in the datascience community that marries up:

1. writing code, and
2. writing pros

They are often described as `computational narratives`.

We will be using `jupyter notebooks` in this workshop, and `jupyter` comes packaged with `anaconda` so if you have
completed `Step 1` you have `jupyter` on your system.

### Launching Jupyter Notebooks

Jupyter is a server that runs on your computer that connects the front-end `html` based interface with programming
language kernels (such as `python`) to execute code and get results.

```{tip}
`Jupyter Lab` is also available as an option to use. It provides a more comprehensive Integrated Development
Environment (IDE). We tend to use `jupyter notebooks` as they are a simpler interface.
```


#### Terminal based Workflow

Terminal based workflows can be a very convenient way to launch applications (like `jupyter`) and run programs.

````{tabbed} macOS

You can open `terminal` using:

1. `Finder` to open `Applications/Utilities/Terminal`, or
2. `Spotlight` to search for `terminal`

```{figure} /_assets/resources/osx-terminal1.png
```

then you can type `jupyter notebook` to launch a jupyter notebook server:

```{figure} /_assets/resources/osx-terminal2.png
```

A browser will then open with a running `jupyter notebook` home page
as shown in the [next section](getting-setup/notebooks)

````

````{tabbed} Windows
TBD
````

````{tabbed} Linux
The `linux` setup is the same as `OS X` once you open the default `terminal` application
for your `linux` distribution.
````


#### GUI based Workflow

There is a Graphical User Interface (GUI) available for launching `Jupyter Notebook` or `Jupyter Lab` provided by Anaconda.

````{tabbed} macOS
TBD
````

````{tabbed} Windows
TBD
````

````{tabbed} Linux
TBD
````

(getting-setup/notebooks)=
### Creating / Opening an `ipynb` file

Once you have the `jupyter` server running you will see the following in your browser:

```{figure} /_assets/resources/notebook1.png
```

and you can click on `New` and select `Python` as your language

```{figure} /_assets/resources/notebook2.png
```


## Step 5: Exercises

````{exercise} 
Replicate the `code` in this lecture in your own Jupyter Notebook:

https://python-programming.quantecon.org/python_by_example.html

by stepping through each `code block` and copying it into your own notebook.

Alternatively, you can also download an `ipynb` version of the page:

```{figure} /_assets/resources/exercise-getting-started-nb-link.png
```

and/or run this lecture in the cloud using the `play` button

````