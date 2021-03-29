(session5/stata-and-python-files)=
# File based Workflows

In many cases it can be convenient to keep `stata` and `python`
workflows largely independent of each other and use files to
transfer data back and forth:

1. Dataset Construction (Python)
2. Statistical Modelling (Stata)

```{note}
If `data` needs to be computed regularly due to updates. The
`python script` interface in `stata` is useful here as it can
be used to update `data` using a `python script` before running
any `regressions`.
```

Support for using a file based workflow is provided by `pandas`
as it has an interface for reading and writing dta files.

## Pandas: Reading `dta` files

Let's fetch the `auto` dataset provided by `stata` and save it as
a `dta` file.

```stata
sysuse auto
save "auto.dta"
```

You can view this dataset in the `data reader`

```{figure} img/stata-dataeditor-auto.png
```

In `stata` this dataset consists of the following types:

```{list-table}
:widths: 15 25 15
:header-rows: 1

* - Variables
  - Data Type
  - Label
* - make
  - str18
  - Make and Model
* - price
  - int
  - Price
* - mpg
  - int
  - Mileage (mpg)
* - rep78
  - int
  - Repair Record 1978
* - headroom
  - float
  - Headroom (in)
* - trunk
  - int
  - Trunk space (cu. ft.)
* - weight
  - int
  - Weight (lbs)
* - length
  - int
  - Length (in.)
* - turn
  - int
  - Turn Circle (ft.)
* - displacement
  - int
  - Displacement (cu. in.)
* - gear_ratio
  - float
  - Gear Ratio
* - foreign
  - byte
  - Car Type
```

Let us now read this `dta` file into `python` using [pd.read_stata()](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html)

```python
import pandas
auto = pd.read_stata("auto.dta")
auto
```

```{figure} img/python-pandas-read-auto.png
```

The `data types` reported by `auto.dtypes` show that `pandas` has done a good job of fetching
the data faithfully from the `stata` dta file.

```python
auto.dtypes
```

produces the following list:

```
make              object
price              int16
mpg                int16
rep78            float64
headroom         float32
trunk              int16
weight             int16
length             int16
turn               int16
displacement       int16
gear_ratio       float32
foreign         category
dtype: object
```

## Pandas: Writing `dta` files

```{note}
You can also write other `data` file formats if you have trouble
with the `dta` writer, such as `csv`, `xlsx`. However you often loose
information and you need to think about `dtypes` during this
translation process between formats.
```

You can write to `dta` file format using [pd.DataFrame.to_stata()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html) method associated with `pd.DataFrame`.

```python
import yfinance as yf
dowjones = yf.Ticker("^DJI")
data = dowjones.history(start="2010-01-01", end="2020-12-31")[['Close', 'Volume']]
data.to_stata("yfinance-dji.dta")
```

This will generate a `dta` file that can be opened with `stata` such as the following
in the `data editor`

```{figure} img/python-pandas-yfinance-data-tostata-dataeditor1.png
```

You can then format these dates in stata using

```stata
format %tcCCYY-NN-DD Date
```

:::{note}
It is also possible to write these `dta` files from within a stata python program
such as:

```stata
python:
import yfinance as yf
dowjones = yf.Ticker("^DJI")
data = dowjones.history(start="2010-01-01", end="2020-12-31")[['Close', 'Volume']]
data.to_stata("yfinance-dji.dta")
end
use yfinance-dji.dta, clear
```
:::

You may notice the default `datetime` object has been translated nicely but `pandas`
has used stata `tc` format (by default) as [per the documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html).
We can specify `td` dates using the `convert_dates=` keyword argument and specifying the `column`
and which `datetime` conversion to use such as:

```stata
python:
data = data.reset_index()
data.to_stata("yfinance-dji2.dta", convert_dates={'Date' : 'td'})
end
```

### Errors writing `dta` files

The `pandas` object is more general than the stata `dta` format so there are cases where
the data can't be written to `dta`.

In this case you will get a:

`NotImplementedError` if the `pandas` datetime objects contain `time zone` information,
or a `column` data type is not able to be represented in the `dta` file format

or a `ValueError`.
