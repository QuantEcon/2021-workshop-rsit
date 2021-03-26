(session3/statsmodels)=
# statsmodels

```{admonition} Aims & Outcomes:
1. Run a Gravity Model
2. Use NumPy to verify statsmodels
```

:::{margin}
There is another package [linearmodels](https://github.com/bashtage/linearmodels/) that extends `statsmodels` with
Panel regressions, instrumental variable estimators, system estimators, etc. and is actively maintained
:::

[statsmodels](https://www.statsmodels.org/stable/index.html) is the package for `econometric` type statistics in `python`.

```{admonition} Resources
The [statsmodels getting started guide](https://www.statsmodels.org/stable/gettingstarted.html) and the
[user guide](https://www.statsmodels.org/stable/user-guide.html) are good places to learn more about
what `statsmodels` can do.
```

We will work through the following `statsmodels` demo notebook.

## Local Option

You can download the {download}`notebook from here <../../../notebooks/session3/intro-to-statsmodels.ipynb>`

You will also need to download the
{download}`supplementary data file <../../../notebooks/session3/data/gravity_dataset_2013.csv>`

and save this file in a folder called `data` where you have saved the notebook such as:

```bash
intro-to-statsmodels.ipynb
data/gravity_dataset_2013.csv
```

then browse to this `folder` and load **jupyter**:

```bash
jupyter notebook intro-to-statsmodels.ipynb
```

## Cloud Based Option

You can [launch the notebook](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession3%2Fintro-to-statsmodels.ipynb)