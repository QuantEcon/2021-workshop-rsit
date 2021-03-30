(session8/python-files)=
# Python Files

Once you have chosen a text-editor, you are ready to begin writing Python files.


## Python file structure

What does a typical Python file look like?

```python
# Import standard lib libraries
import requests

# Import external libraries
import numpy as np
import pandas

# Import internal libraries


def my_function(x, y):
    return x + y


def another_function(x, y):
    return x*y


# If we want to do particular things when the file is run, we
# put it in the block below
if __name__ == "__main__":
    print(my_function(2, 2))
    print(another_function(2, 2))
```

A slightly more useful file might be something like the following:

```python
import pandas as pd


def convert_to_TX_time(ts):
    return ts.tz_convert("US/Central")


def convert_to_DE_time(ts):
    return ts.tz_convert("Europe/Berlin")


if __name__ == "__main__":
    ts = pd.Timestamp.utcnow()

    print(f"The time in TX is {convert_to_TX_time(ts)}")
    print(f"The time in DE is {convert_to_DE_time(ts)}")
```


## Running a Python file

Once we've written and saved a Python file, we can run it using `python filename.py`

When we run the file, it will by default execute all of the code in the file. We can specify that it should do a particular subset of things using the `if` statement we've included at the bottom of our files.


## Building internal libraries

As you work on slightly more involved projects, you will often (or at least you should) build a small collection of helper functions and components to minimize the amount of repetition in your code.

How can we package this up in a way that allows it to be usable? We can create our own package within our project folder!


### File structure

Imagine we have a file structure that has the following form

```
- web_scraping_project
  - scrapers
    - __init__.py
    - scraper1.py
    - scraper2.py
    - helpers
      - __init__.py
      - helper_functions.py
      - other_stuff.py
```

The `__init__.py` file under the `scrapers` and `helpers` folders denotes that these two folders should be interpreted as Python packages. This means that we could import code from them just like we are able to import code from `numpy` or `pandas`.

We will see an example of doing this in the web scraping section
