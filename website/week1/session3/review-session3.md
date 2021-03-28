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
[on stackoverflow](https://stackoverflow.com/questions/1704823/create-numpy-matrix-filled-with-nans)

including performance comparisons!

## Q: Will we cover more of `statsmodels`

Yes, we will do more `statsmodels` today.

There is also a package called [linearmodels](https://bashtage.github.io/linearmodels/) that will
be used.

## Q: Parsing data and constructing Age Categories

I have put together {download}`a notebook <../../../notebooks/session5/solution-age-categories.ipynb>`
discussing some possible options in `pure python` using a dictionary to store the results and a 
comparison with `pandas`.

I have recieved some sample data from a participant so we can use that on `Tuesday`/`Thursday` to review using
real world data.

