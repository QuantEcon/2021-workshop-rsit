(session3/review-session3)=
# Questions & Answers

I have updated the {download}`exercise notebook with solutions <../../../notebooks/session3/exercises.ipynb>`
from the tutorial. 

You can [launch the notebook](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession3%2Fexercises.ipynb)

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

## Q: How do you combine `pd.DataFrame`

There are a number of ways of doing this. After brushing up on `pandas` docs here are some methods that will be useful. 

In the exercise notebook we saved data for `usa` and `others` which can be combined:

```python
combined = usa.append(others)
combined.T.plot()
```

This `appends` additional rows. Given the columns are the same in each dataframe this a simple option. 

We had a discussion focused around combining dataframes and had a look at:

1. `pd.concat` (works to append `rows` by default)
2. `pd.join` (works to append `columns` by default)

but they can be used on differenct `axis` by specifing `axis=1` etc.

so we could have used

```python
pd.concat([usa, others])
```

or with the usa.T, others.T data which is a format more convenient for `plotting` with `countries` as columns.

```python
pd.join([usa.T, others.T])
```

or by alterning the `axis`

```python
pd.concat([usa.T, others.T], axis=1)
```



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

