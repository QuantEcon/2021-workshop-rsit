(session3/others)=
# Other Packages

There are lots of `other` packages in the `python` ecosystem.

This is an `opinionated` list with packages sorted in order of `preference`, and/or
the best order for `learning`.

```{note}
If the research group has a particular interest in any of the following
packages. Please add a comment to [this issue](https://github.com/QuantEcon/2021-workshop-rsit/issues/3) on the workshop
repository Issues list and let me know as a comment
```

## Plotting and Visualisation

```{list-table}
:widths: 5 25
:header-rows: 1

* - Package
  - Description
* - [matplotlib](http://matplotlib.org)
  - The core library for generating plots
* - [seaborn](http://seaborn.pydata.org)
  - A plotting library with a focus on statistical graphics
* - [bokeh](http://bokeh.pydata.org)
  - build plots for the web through javascript powered visualisations
* - [Plotly](https://plot.ly)
  - a `python` interface to [Plotly](https://plotly.com/python/) for interactive plots
```

## Statistical Modelling & Machine Learning

```{list-table}
:widths: 5 25
:header-rows: 1

* - Package
  - Description
* - [statsmodels](http://statsmodels.sourceforge.net)
  - Statistical modelling (Econometrics focus)
* - [scikit-learn](http://http://scikit-learn.org)
  - The standard machine learning library
* - [Stan](http://mc-stan.org)
  - Bayesian Statistical modeling, data analysis, and prediction
* - [PyMC3](https://pymc-devs.github.io/pymc3/)
  - Alternative package for Bayesian statistical modeling
* - [scikit-survival](https://github.com/sebp/scikit-survival/)
  - Survival analysis based on top of scikit-learn
* - [lifelines](https://lifelines.readthedocs.io)
  - Survival analysis in Python
```

## Performance & Scale

```{list-table}
:widths: 5 25
:header-rows: 1

* - Package
  - Description
* - [Numba](http://numba.pydata.org)
  - Generates optimised code using a `just-in-time` compiler
* - [Dask](https://dask.org)
  - Infrastructure for building parallel workloads across `cpu cores` or `machines`
* - [Cython](http://cython.org)
  - Translates Python-style code to C

```

## Scientific Computing & Mathematics

```{list-table}
:widths: 5 25
:header-rows: 1

* - Package
  - Description
* - [scipy](https://www.scipy.org)
  - The core library for `scientific computing`
* - [scipy](https://scipy.org/scipylib/index.html)
  - statistics, linear algebra, numerical integration and optimisation
* - [cvxpy](http://www.cvxpy.org)
  - Convex optimisation
* - [FEniCS](https://fenicsproject.org)
  - Platform for partial differential equations (PDE
```

## Networks

```{list-table}
:widths: 5 25
:header-rows: 1

* - Package
  - Description
* - [networkx](https://networkx.org)
  - NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks
* - [networkit](https://networkit.github.io)
  - A toolkit for large-scale network analysis
* - [graph-tool](https://graph-tool.skewed.de)
  - Network library designed to be fast and largely implemented in C/C++
* - [Snap.py](https://snap.stanford.edu/snappy/)
  - A python interface for SNAP (a general purpose, high performance library for analysis and manipulation of large networks)
* - [DeepGraph](https://deepgraph.readthedocs.io/en/latest/index.html)
  - A `pandas` based entry point into defining networks
```

The article `Python Packages for Networks` is a good reference {cite}`Batagelj2018`.

**Others:**

- [igraph](https://igraph.org),
- [tulip](https://tulip.labri.fr/Documentation/current/tulip-python/html/index.html)


## Natural Language Processing (NLP)

| Package | Description |
| ------- | ----------- |
| [SpaCy](https://spacy.io) | Library with lots of NLP algorithms | 
| [gensim](https://radimrehurek.com/gensim/index.html) | Topic modelling |


## Online Courses

```{list-table}
:widths: 5 25
:header-rows: 1

* - Course
  - Description
* - [Python Programming for Economics and Finance](https://python-programming.quantecon.org/intro.html)
  - Introduction to the `python` language
* - [Quantitative Economics with Python](https://python.quantecon.org)
  - A series of lectures on quantitative economic modelling
* - [Software Carpentry](https://software-carpentry.org/lessons/)
  - Introduction to various programming topics
* - [Data carpentry](http://www.datacarpentry.org/lessons/)
  - Hands-on, interactive lessons on various data analysis topics

```

```{bibliography}
:filter: docname in docnames
:style: plain
```