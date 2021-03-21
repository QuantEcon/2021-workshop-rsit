(session3/numba)=
# Numba

[numba](https://numba.pydata.org) is the foundational package for accelerating numerical
`python` code by translating a subset of `python` and `numpy` code into fast machine code using
`just in time compilation (JIT)`.

```{admonition} Personal Note:
This package saved me days of work during my PhD. I was able to speed up my `python` code to
the point you could interact with the analysis in `real time`. My work went from overnight runs that
took 8 hours to getting the results straight away. It can be a hugely useful tool.
```

Here is [the QuantEcon lecture on numba](https://python-programming.quantecon.org/numba.html)

We will work through the following `numba` demo notebook.

## Local Option

You can download the {download}`notebook from here <../../../notebooks/session3/intro-to-numba.ipynb>`

Then browse to your download location and load **jupyter**:

```bash
cd ~/Downloads
jupyter notebook intro-to-numba.ipynb
```

## Cloud Based Option

You can [launch the notebook](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession3%2Fintro-to-numba.ipynb)