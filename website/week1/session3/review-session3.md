(session3/review-session3)=
# Questions & Answers

## Q: How to create a numpy array with np.nan

```python
import numpy as np
a = np.zeros(4)
a[:] = np.nan
```

The `a[:]` broadcasts across all elements of the array `a` and assigns the value `np.nan`

There does not seem to be a separate method for setting up these arrays automatically.

But one other option is to use `full` method for `numpy >= 1.8+`

```python
import numpy as np
a = np.full(4, np.nan)
```

There is an excellent discussion of this
[on stackoverflow](https://stackoverflow.com/questions/1704823/create-numpy-matrix-filled-with-nans) including performance comparisons!

## Q: Will we cover more of `statsmodels`

Yes, we can do more `statsmodels` in `Session 7`.

There is also a package called [linearmodels](https://bashtage.github.io/linearmodels/) that we can take a look at as well that
includes support for Panels etc.

Still doing some research around `high dimensional fixed effects`
models in `python`.

There is [linearmodels.iv.absorbing.AbsorbingLS](https://bashtage.github.io/linearmodels/iv/absorbing/linearmodels.iv.absorbing.AbsorbingLS.html#linearmodels.iv.absorbing.AbsorbingLS) in the `IV` family of models where $z$ may be high-dimension.

## Q: Parsing data and constructing Age Categories

I have put together {download}`a notebook <../../../notebooks/session5/solution-age-categories.ipynb>`
discussing some possible options in `pure python` using a
dictionary to store the results and a comparison with `pandas`
using `categoricals`.

You can [run this notebook here](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession5%2Fsolution-age-categories.ipynb)

I have received some sample data from a participant so we can use
that in this weeks `Tutorial` to review using real world data.

