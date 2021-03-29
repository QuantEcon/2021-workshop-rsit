(session7/stata-and-jupyter)=
# Stata and Jupyter

## Setup

There are two primary approaches to using `stata` with `jupyter`:

## Stata Jupyter Kernel

The [Stata Jupyter Kernel](https://github.com/kylebarron/stata_kernel)
enables using stata directly in `jupyter` notebooks. 

It is effectively an alternative interface to use stata if you like
`jupyter` as an interface. 

There is [excellent documentation](https://kylebarron.dev/stata_kernel/)
available.

To install using `anaconda` tools you can use the following commands
in a `jupyter notebook`:

:::{margin}
```{tip}
It is important to specify `-y` when issuing install requests via
jupyter as there is no way to accept the user requested `y` input
to proceed with install.
:::

```bash
!conda install -y -c conda-forge stata_kernel
```

once the software is installed you need to install the `kernel`:

```bash
!python -m stata_kernel.install
```

:::{warning}
**[macOS]** When I ran the kernel install step I got the following `error`:

```bash
Cannot import kernel
Installing Jupyter kernel spec
WARNING: Could not find Stata path.
Refer to the documentation to see how to set it manually:

https://kylebarron.dev/stata_kernel/using_stata_kernel/configuration
```

and had to manually set the `stata` path in the `.stata_kernel.conf` file located
in your home directory to the following:

```bash
# Path to stata executable. If you type this in your terminal, it should
# start the Stata console
stata_path = /Applications/Stata/StataIC.app/Contents/MacOS/StataIC

# **macOS only**
# The manner in which the kernel connects to Stata. Either 'console' or
# 'automation'. 'console' is the default because it allows multiple
# independent sessions of Stata at the same time.
execution_mode = automation
```

Unfortunately `StataIC` is limited on `mac os` so had to use `automation`
instead of `console` as per
[this issue in the docs](https://kylebarron.dev/stata_kernel/using_stata_kernel/configuration/)
:::

## IPyStata

```{warning}
For `macOS` it appears that `stataIC` does not come with the console tools
needed to make this work. This requires `stataSE` and above
```

This package provides an alternative approach which provides support
for running `stata` commands using `ipython magics`. So you remain in a
`python` powered notebook and interface with stata when needed.

[IPyStata](https://github.com/TiesdeKok/ipystata)

There is a [nice presentation](http://fmwww.bc.edu/repec/chic2016/chicago16_dekok.pdf)
that runs through this integration. 

To install you can use `pip`:

```bash
pip install ipystata
```

:::{margin}
This is a bit of a red flag in my view as releases are best distributed via PyPI.
However for tired open-source contributors this can be one short-cut taken to reduce workload.
:::

however the `released version` via `PyPI` is a lot older than the `master` branch of the code repository
so to get the latest you could install using:

```bash
pip install git+https://github.com/TiesdeKok/ipystata
```

The [documentation](https://nbviewer.jupyter.org/github/TiesdeKok/ipystata/blob/master/ipystata/Example.ipynb)
largely consists of a demo notebook.

To setup the package you then need to configure the package to know where `Stata` is on your computer.

```python
import ipystata
from ipystata.config import config_stata
config_stata("<path>")
```
as documented [here](https://github.com/TiesdeKok/ipystata#set-installation-directory-for-stata)