(session5/stata-and-python-example)=
# Example: Product Level Gravity Model (International Trade)

```{warning} In Work
This Session is in Work
```

For this demo you will need to fetch the data from [The Atlas of Complexity](https://atlas.cid.harvard.edu/data-downloads)
data downloads page. This will redirect you to the Harvard Dataverse Page from where you can download the
file `country_partner_sitcproduct4digit_year_2013.tab` (284Mb)

```{note}
You can also fetch a `dta` of this file if working with stata
```

These days it is convenient to get access to datasets that are already well prepared. Just a few years ago
we had to spend a long time combining data from lots of sources to construct an equivalent dataset. This
dataset already includes `ISO3C` codes for example for easier representation of country codes. Let's take a
look at the data:

Let's use `python` to combine this dataset and then we will run regressions in `stata`

```python
import pandas as pd
data = pd.read_table("country_partner_sitcproduct4digit_year_2013.tab", nrows=10)
```

```{tip}
When working with larger datasets it is very useful to use the `nrows=` argument to get a preview
of what is in the file.

Specifying `nrows=10` means you only import the first 10 rows of `data` contained in the file.
```

You can see the dataframe contains:

```{figure} img/python-pandas-atlas2013-datapreview.png
```

This allows you to specify which columns you really need to import from the file

```python
columns = [ 'year','location_code', 'partner_code', 'sitc_product_code', 'export_value']
data = pd.read_table("country_partner_sitcproduct4digit_year_2013.tab",
                     usecols=columns)
```

now we have a subset of the data that we are interested in and loaded into a `pd.DataFrame`

```{figure} img/python-pandas-atlas2013-datapreview2.png
```

We will also need to get `distance` and `gdp` information to add to our dataset. For this we
will use [CEPII](http://www.cepii.fr/cepii/en/bdd_modele/bdd.asp) and `World Bank Data`

You will need to download:

1. [Gravity Dataset](http://www.cepii.fr/cepii/en/bdd_modele/presentation.asp?id=8)





