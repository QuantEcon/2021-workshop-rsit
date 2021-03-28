(session5/stata-and-python)=
# Stata and Python

:::{note}
I am interested in turning these workshop materials into a resource on using
`stata` and `python` together for the broader community.

Any feedback, ideas or suggested improvements are most welcome!
:::

One of the major new features of [Stata16](https://www.stata.com/new-in-stata/)
is [python integration](https://www.stata.com/new-in-stata/python-integration/).

There are various ways to use `python` effectively with `stata` and this session
will look at:

1. [Setting up **python** in **stata**](session5/stata-python-setup)
2. [Using **python** in **stata**](session5/stata-python-using)
3. [Using **stata** with **python** (via files)](session5/stata-python-file-interface)]

```{seealso}
We will also look at alternative ways to use `stata` and `python` in the
[next session](session7/stata-and-jupyter) through `jupyter` using `stata`
kernels.
```

```{tip}
There is a nice sequence of [blog posts](https://blog.stata.com/category/programming/)
in the `programming` channel of the stata blog discussing python.
```

(session5/stata-python-setup)=
## Setup Python in Stata

:::{margin}
Stata16 [has been updated for use on Apple Silicon based Macs](https://blog.stata.com/2020/11/10/stata-for-mac-with-apple-silicon/) but older versions will run through translation instead of
native support.
:::

```{note}
This session presumes you have already installed `Stata16+` on your computer and you are already
familiar with using `stata`
```

```{tip}
Some Universities install `stata` over the network as university provided software.
This can cause issues relating to permissions so please speak up if you run into
these problems and we can look at trying to find a solution.
```

```{admonition} macOS + Anaconda Issue
I ran into [this issue](https://www.statalist.org/forums/forum/general-stata-discussion/general/1578573-python-integration-pandas-package-causing-stata-to-close) on my `macOS` installation
of Stata and found the suggestion solution was required to prevent this behavior
```

Integration between computer software is always a tricky problem to solve and typically requires
some investment in setting up the integrations properly.

We will focus on setting up `python` in `stata` and getting access to your configuration.

Having good knowledge of how your system is configured helps greatly in reducing bugs and issues related
to software problems.

:::{margin}
This workflow has been put together on `macOS`. The `stata` application is pretty consistent
across platforms such as `Windows` but please let me know if we need `windows` tabs for clarity
:::

Open up the `Stata` application on your computer

```{figure} img/stata-open.png
```

### Checking your Configuration

To check your configuration you can type:

```stata
python query
```

in the command window which will provide the following details:

```{figure} img/stata-python-query.png
```

the `output` provides useful information about how `stata` and `python`
are linked together.

```{list-table}
:widths: 15 25
:header-rows: 1

* - Field
  - Description
* - `python_exec`
  - the location on your computer for the `python` interpreter you are using in `stata`
* - `python_userpath`
  - the location for any custom `python` code that you would like added to the python `sys.path`
* - `python system information`
  - this provides additional information about the `python` version and software used.
```

### Searching for Python on your System

Stata can search your system for any `python` installations and list them by typing:

```stata
python search
```

in the command window.

```{figure} img/stata-python-search.png
```

:::{note}
If `python` is not yet configured you will see:

```stata
. python search

no Python installation found; minimum version required is 2.7.
r(111)
```

this will require you to install a python environment such as [anaconda](resources/setup)
:::

### Setting the python distribution

Linking `stata` to a specific `python` installation (such as `anaconda`) can be done
using the `set python_exec` command such as:

:::{tabbed} macOS
```stata
set python_exec /Users/<user>/anaconda3/bin/python
```
:::

:::{tabbed} Windows
```stata
set python_exec C:\Users\<users>\anaconda3\python.exe
```
:::

This can be used together with `python search` to know which path to provide and then
the setting can be checked using `python query`.

### Updating your `sys.path` in `python`

`python` uses `sys.path` to specify the search path for looking up
`python packages` and other utilities and programs.

You can add a custom path for the python `stata` environment using `set python_userpath`

:::{tabbed} macOS
```stata
set python_userpath /Users/<user>/mypythoncode
```
:::

:::{tabbed} Windows
```stata
set python_userpath C:\Users\<users>\mypythoncode
```
:::

Then check the setting using `python query`.

### Testing Python

To check that everything is setup and ready to go you can run the
[first python example](session5/stata-and-python-firstexample) and verify
everything is working.

(session5/stata-python-using)=
## Using Python in Stata

:::{margin}
The [stata manual](https://www.stata.com/manuals/ppython.pdf) has a section
on the `python` command.

This [blog post](https://blog.stata.com/2020/08/25/stata-python-integration-part-2-three-ways-to-use-python-in-stata/)
does a really good job of explaining the different methods for using `python` in `stata`.
:::

(session5/stata-and-python-interactive)=
### Running `python` Interactively with a First Example

(session5/stata-and-python-firstexample)=

You can run `python` interactively within `stata` in a manner that is the
equivalent of running the `python` REPL program through a terminal.

This is activated by typing `python` in the command window.

```{figure} img/stata-python.png
```

You are now interfacing directly with the `python` interpreter as indicated in
the `Result` window.

You can now write `python code` such as:

```python
print("Hello World!")
```

```{figure} img/stata-python-hello-world.png
```

once you hit enter `stata` sends the code snippet to the python interpreter
for processing

```{figure} img/stata-python-hello-world-result.png
```

:::{margin}
```{note}
For `python` users the use of `end` takes some getting used to as the usual
way to exit the `python` REPL is using the `exit()` function. Stata uses `end`
across its ecosystem and is consistent with `stata`.
```
:::

To stop interfacing with the `python` interpreter you need to type `end` in
the command window

```{figure} img/stata-python-hello-world-end.png
```

this will return you to the standard `stata` interface.

:::{tip}
If you have a one line `python` command you can use
```stata
python: print("Hello World!")
```
which will pass the code to `python` and display the results
directly below in the `Results` window
```{figure} img/stata-python-hello-world-oneline.png
```
:::

(session5/stata-and-python-do)=
### Running `python` in a `do` file

Another option for running `python` code is through the `do` file.

Let's open the `do` file editor and add:

:::{margin}
This can be {download}`downloaded from here as a do file <do/example1.do>`
:::

```stata
di "Stata Here"
python: print("Python Here")
```

```{figure} img/stata-example1-do.png
```

and when you click on `Do` button you get the result:

```{figure} img/stata-example1-do-run.png
```

where the results from `python` are displayed similarly to `stata` output.

However, you often want to add in a **block of code** such as:

```python
for i in range(0,2):
    print("Python Here")
```

This can be done by delimiting the `python code` within the `do` file using:

1. `python` and `end`, or
2. `python:` and `end`

The difference between these two `delimiters` is in how `stata` handles any
errors in `python`. The `python` environment will continue to execute the rest
of the `python` code if an error is encountered, while `python:` will **immediately**
return control to `stata` once the error is encountered.

:::{margin}
This can be {download}`downloaded from here as a do file <do/example2a.do>`
:::

```stata
di "Stata Here"
python
for i in rang(2):
   print("Python Here")
print("Python Done")
end
di "Back in Stata Land!"
```

```{figure} img/stata-example2a-do-error.png
```

As you can see `stata` has continued to execute code past the point at which there is
an error. 

However if you use `python:` the execution will halt at the point of the `error`.

:::{margin}
This can be {download}`downloaded from here as a do file <do/example2b.do>`
:::

```stata
di "Stata Here"
python:
for i in rang(2):
   print("Python Here")
print("Python Done")
end
di "Back in Stata Land!"
```

```{figure} img/stata-example2b-do-error.png
```

```{tip}
I tend to use `python:` as I prefer to get to the error quickly to fix the problem
without any distracting output below it. Also in a long running program you will want
to fix the issue prior to the rest of the program executing.
```

We can use the error message to fix the issue now and run the fixed `do` file

:::{margin}
This can be {download}`downloaded from here as a do file <do/example2c.do>`
:::

```stata
di "Stata Here"
python:
for i in range(2):
   print("Python Here")
print("Python Done")
end
di "Back in Stata Land!"
```

```{figure} img/stata-example2c-do-run.png
```

#### The Do File Editor and White Space

```{admonition} Reminder
Whitespace is used by `python` to declare `scopes` and is an integral part
of the language definition
```

The `do` file editor doesn't provide you with full `text editor` support when writing
`python` code in the `do` file editor.

For example if you type:

```stata
python:
for i in range(10):
|<curser placed here>
```

the `editor` will **not** automatically indent your code.

However once you have set the
curser to the correct indentation level it will retain that indentation level for
subsequent lines.

```stata
python:
for i in range(10):
    |
    |<curser placed here>
```

So you need to be careful with `whitespace`

Also what you type in the `delimiters` is directly passed to `python`
so you can't indent these `code-blocks` such as:

```stata
di "Stata Here"
python:
    print("Python Here")
```

`python` will return the following error:

```{figure} img/stata-do-whitespace-error.png
```

(session5/stata-and-python-scripts)=
### Running `python` scripts in `stata`

A third option is to run a `python script` that contains some `python code`

If you save the following code in a file `example3.py`:

:::{margin}
This can be {download}`downloaded from here as a py file <do/example3.py>`
:::

```python
print("Python Here")
for i in range(2):
    print(f"{i} times hello")
print("I'm outta here")
```

you can then run this script in `stata` using:

:::{margin}
```{tip}
You will need to update you `working directory` before running the
python script
```
:::

```stata
python script example.py
```

with the output:

```{figure} img/stata-python-script-example.png
```

```{tip}
This is a very useful way to run `python` code as it leaves you
to write `python` code in any text editor you like such as
[vscode](https://code.visualstudio.com).
```

### Interacting between `Stata` and `Python`

```{note}
In many cases it can be simpler to keep `python` and `stata`
workflows independent of each other and use `files` to transfer
data between them.

This is covered in [](session5/stata-python-file-interface)
```

So far the `python` and `stata` runtime environments have been
independent of each other to learn about how to run `python` code
within `stata`.

However for most applications we want some level of `interaction` between `stata`
and `python` by copying back and forth objects between the different runtime
environments.

`Stata` makes various components of `stata` available to `python` via
the [stata function interface (sfi)](session5/stata-and-python-sfi)
to enable such interaction, such as:

1. [Current Stata Dataset](https://www.stata.com/python/api16/Data.html)
2. [Stata Frames](https://www.stata.com/python/api16/Frame.html)
   ```{note}
   [frames](https://www.stata.com/new-in-stata/multiple-datasets-in-memory/) have been introduced 
   to load more than one dataset
   ```
3. [Stata Macros](https://www.stata.com/python/api16/Macro.html)

In addition to access to [many other components](session5/stata-and-python-sfi).

#### Copying Data from Stata to Python

```{admonition} Stata Blog Post
This section is heavily inspired by [this excellent stata blog post](https://blog.stata.com/2020/11/05/stata-python-integration-part-8-using-the-stata-function-interface-to-copy-data-from-stata-to-python/)
that runs through another example.
```

```stata
sysuse auto
list foreign
```

listing the `foreign` data in `stata` shows:

```{figure} img/stata-sysuse-auto-list-foreign.png
```

then use `python` to look at the `raw` data using the `.get` method
of the `Data` object from the `stata function interface` package.

```stata
python
from sfi import Data
dataraw = Data.get('foreign')
dataraw
end
```

and it looks like

```{figure} img/stata-sysuse-auto-python-raw.png
```

Notice that the `data` looks different.

```{note}
`stata` has a concept of `labels`
```

If you use the `data explorer` you will see that the `foreign` variable consists of
`0,1` that are associated with labels `domestic` and `foreign` (respectively).

```{figure} img/stata-sysuse-auto-dataviewier-foreign.png
```

You may want to get more information about the `get` method so the best place
to look is the [documentation on sfi.Data](https://www.stata.com/python/api16/Data.html).
Then you can click on the [get method](https://www.stata.com/python/api16/Data.html#sfi.Data.get)

```{tip}
You **can't** use the `ipython` features such as `Data.get?` in this context because
`python` is interfacing directly with the `python` interpreter and not the
`ipython` interpreter (such as when you're using `jupyter`)
```

That page looks like:

```{figure} img/stata-docs-sfi-data-get.png
```

You can see that an option is to fetch the `value label` using `valuelabel=True`

```stata
python
from sfi import Data
dataraw = Data.get('foreign', valuelabel=True)
dataraw
end
```

and the `rawdata` is now returned as strings taking the value of the `labels` that
have been applied to the data

```{figure} img/stata-sysuse-auto-foreign-valuelabels.png
```

**Obtaining more variables at once:**

You can obtain more variables using the `get` method. Based on the documentation you can use
the following methods to specify what variables to fetch `var (int, str, or list-like, optional)`.

In addition you can also specify which `obs` you would like `obs (int or list-like, optional)`.

```stata
python
from sfi import Data
dataraw = Data.get('foreign mpg rep78', range(45,56))
dataraw
end
```

this code saves a `list of list` type object into the `python` object `dataraw`

```{figure} img/stata-sysuse-auto-3vars-range.png
```

The data is written as a list of `rows` in the order of the variables requested, which
in this case is: `foreign mpg rep78` such as the first element:

```python
[[0, 18, 2], ...
```

:::{margin}
```{note}
`range` is a `python` object that behaves like a list when constructing `ranges`
```
:::

The `range(45,56)` request will fetch observations `46` to `56` as shown in the `data` browser

:::{margin}
```{note}
The stata `data viewer` is indexed by `1` while `python` is indexed by `0`
```
:::

```{figure} img/stata-sysuse-auto-dataviewer-range.png
```

As per the `documentation` you can also specify a `list-like` object instead of a string separated
by a space such as `['foreign', 'mpg', 'rep78']`:

```stata
python
from sfi import Data
dataraw = Data.get(['foreign', 'mpg', 'rep78'], range(45,56))
dataraw
end
```

will return the same data

```{figure} img/stata-sysuse-auto-3vars-range-list.png
```

```{exercise}
What happens now if you specify `valuelabel=True` for the above `python`
code?
```

:::{margin}
Current `Stata` support is for moving `raw data` to the python context. It is left
to the user to push that raw data into some other object such as `pd.DataFrame`
or `pd.Series`. I hope support for `pd.DataFrame` will be coming in a future release.
:::

**pd.DataFrame and pd.Series:**

The discussion so far has focused on fetching `raw data` out of `stata` and copying
it to the `python` environment. But in many applications we are unlikely to want to
use the raw data directly and you will want to be comfortable with setting up
pandas `DataFrame` and `Series` objects such as:

```stata
python
from sfi import Data
import pandas as pd
dataraw = Data.get('foreign mpg rep78', range(45,56))
df = pd.DataFrame(dataraw)
df
end
```

You will notice that the `raw data` has now been placed in a `pd.DataFrame`
but `columns` and `index` variables haven't come across:

```{figure} img/stata-sysuse-auto-3vars-range-dataframe.png
```

You may want to parameterize your requests so you can use them in both
the `sfi.Data.get` method in addition to a `pd.DataFrame` method when converting
the `raw data` into a `pd.DataFrame`

You can save the variable selection as a python variable:

```python
vars = ['foreign', 'mpg', 'rep78']
```

then you can use these variables for both `stata` and `python`

:::{margin}
I have used:
1. `range(45,56)` for `stata`, and
2. `range(46,57)` for `pandas`
to harmonise given data ind `stata data viewer` is indexed by `1`.

I hope `stata` provide `sfi.Data.dataframe` that can help manage these
indexing issues.

```{note}
Most of the time you will not need to harmonise like this as you will
just use the data that has been selected.
```
:::

```stata
python
from sfi import Data
import pandas as pd
vars = ['foreign', 'mpg', 'rep78']
dataraw = Data.get(vars, range(45,56), valuelabel=True)
df = pd.DataFrame(dataraw, index=range(46,57), columns=vars)
df
end
```

which provides a much more consistent `pd.DataFrame` and lines up closely with
the stata context.

```{figure} img/stata-sysuse-auto-3vars-range-dataframe2.png
```

```{exercise}
How can you explain the value for the variable `rep78` for observation `51`?
```

**Missing Values:**

Missing values in `stata` are internally represented by the `largest` value for
each type. Within `stata` you typically work with missing values using `.`  such as:

```stata
list rep78 if rep78 != .
```

and much of this detail is taken care of for you.

So missing values are represented by the `maximum value`:

:::{margin}
This table is from the [stata manual](https://www.stata.com/manuals/u12.pdf#u12.2.2Numericstoragetypes)
:::

```{figure} img/stata-numeric-types-table.png
```

:::{margin}
I am **not** sure why `python` receives the missing value for a `double` numeric type when
`rep78` is coded as an `int` in `stata`. I will need to ask `statacorp`.
:::

However if using the raw data in `python` you will want to specify `missingval=np.nan`

```stata
python
from sfi import Data
import numpy as np
import pandas as pd
vars = ['foreign', 'mpg', 'rep78']
dataraw = Data.get(vars, range(45,56), valuelabel=True, missingval=np.nan)
df = pd.DataFrame(dataraw, index=range(46,57), columns=vars)
df
end
```

which returns the following:

```{figure} img/stata-sysuse-auto-3vars-range-dataframe3.png
```

#### Copying Data from Python to Stata

```{admonition} Stata Blog Post
There is [this excellent stata blog post](https://blog.stata.com/2020/11/19/stata-python-integration-part-9-using-the-stata-function-interface-to-copy-data-from-python-to-stata/)
that runs through another example.
```

### Real World Example (Gravity Model)

In this example we will:

1. build a dataset in `python` from multiple sources
2. provide the data to `stata` to run a `fixed effects` regression
3. compare the results using `linearmodels` in `python`
4. compare some plots

(session5/stata-and-python-sfi)=
### The stata function interface `sfi`

The [python api documentation](https://www.stata.com/python/api16/) contains
the details about the `sfi` package from `stata`.

```{list-table}
:widths: 15 25
:header-rows: 1

* - Class
  - Description
* - [Characteristics](https://www.stata.com/python/api16/Characteristic.html) 
  - Access `stata` characteristics
* - [Data](https://www.stata.com/python/api16/Data.html)
  - Access to the current `stata` dataset
* - [Datetimes](https://www.stata.com/python/api16/Datetime.html)
  - Access to `stata` datetimes
* - [Frames](https://www.stata.com/python/api16/Frame.html)
  - Access to `stata` Frames
* - [Macros](https://www.stata.com/python/api16/Macro.html)
  - Access to `stata` macros
* - [Mata](https://www.stata.com/python/api16/Mata.html)
  - An interface with global `mata` matrices
* - [Matrix](https://www.stata.com/python/api16/Matrix.html)
  - Access to `stata` matrices
* - [Missing](https://www.stata.com/python/api16/Missing.html)
  - Access to `stata` missing values
* - [Platform](https://www.stata.com/python/api16/Platform.html)
  - Access to `platform` information
* - [Scalars](https://www.stata.com/python/api16/Scalar.html)
  - Access to `stata` scalars
* - [SFIToolkit](https://www.stata.com/python/api16/SFIToolkit.html)
  - a set of `core` tools for interacting with `stata`
* - [StrLConnector](https://www.stata.com/python/api16/StrLConnector.html)
  - Provide access to `stata strL` datatype in `Data` and/or `Frame`
* - [ValueLabel](https://www.stata.com/python/api16/ValueLabel.html)
  - Access to `stata` value labels
```


## Resources

1. [Stata Manual](https://www.stata.com/manuals/ppython.pdf)
2. [Stata Blog Posts](https://blog.stata.com/category/programming/)


