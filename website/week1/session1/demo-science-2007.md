(session1/demo)=
# (Demo) Replicating the ProductSpace

## Running Locally

You can {download}`download the demo notebook here <../../../notebooks/session1/demo-data-analysis-python-hidalgo2007.ipynb>`

This notebook uses `The Product Space Conditions the Development of Nations` {cite}`Hidalgo2007` as motivation to demonstrate a number of tools that are available in the `python` ecosystem that can be used for data analysis.

To run this notebook there are some `supplementary data` files that you need to download as well:

1. The {download}`data directory <../../../notebooks/session1/data.zip>` containing the needed data files
2. The {download}`img directory <../../../notebooks/session1/img.zip>` containing the supporting image files

These will download as `zip` files that you will need to decompress in the same directory as where you have saved the notebook.

## Running in the Cloud

This repository is also configured to use `mybinder`

You can [launch this demo notebook](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession1%2Fdemo-data-analysis-python-hidalgo2007.ipynb) without having to setup the files on your local machine.

:::{note}
The `mybinder` instance only has 1 x CPU Core so the `dask` section doesn't work on the cloud as it requires a
multi-core environment to do distributed compute tasks.
:::


```{bibliography}
:filter: docname in docnames
:style: plain
```