(session7/python-integrations)=

# Integrations with Other Languages

There are ways to interface with other languages such as `julia` and `R`.

This can be an alternative way of bridging to use something in these
ecosystems that may not be available in the `python` package ecoystem.

```{note}
I typically **don't recommend** this as the first option.

It is always better to try and
find a native solution before interfacing with another system.

Another option is always to write to disk in a common file format and then
use the alternate environment natively.
```

## Julia

The [pyjulia](https://github.com/JuliaPy/pyjulia) package is one way to
interface with `julia` in an object oriented way.

`Julia` is quickly becoming a popular language for the `statistics`
community so it is worth keeping an eye on this space.

For example you may want to use:

1. [Fixed Effects Models](https://github.com/FixedEffects/FixedEffectModels.jl)
   is a package that estimates linear models with high dimensional categorical
   variables and/or instrumental variables.

## R

There is the [rpy2](https://github.com/rpy2/rpy2) bridge between `R` and `python`

[Documentation is available for each release](https://rpy2.github.io/doc/v3.4.x/html/index.html)