(session1/python-for-economics)=
# Introduction to Python for Economics

```{admonition} Aims / Outcomes / Expectations:
1. Provide an overview of `python`
2. Reduce the `fixed costs` of using `python`
3. Get setup and comfortable using `python`
4. Show Examples
5. Provide resources for further study
```

## Why Python?

### Proprietary vs Open Source

**Proprietary:**

1. Excel
2. MATLAB
3. STATA

These can be `good` tools for `specific tasks` but
also have some drawbacks.

**Pro:**
1. Simpler to use with Integrated graphical interfaces
2. Company that provides support
3. Stable

**Con:**
1. Cost Money
2. More constrained to a `narrow` domain than
   more general high-level programming languages so can
   be difficult to achieve some task types
3. Access to higher performance can be expensive

**Open Source:**

1. Python
2. Julia
3. R

Are typically considered the leading `programming languages` to
support `scientific computing`.

**Pro:**
1. Free
2. Ultimately customisable and auditable being `open source`
3. Quick moving communities writing packages and extensions

**Con:**
1. Initially less `user friendly` with limited `point and click`
   style of interaction
2. Quick moving communities writing packages and extensions :-).

### Choice of Programming Languages

There is a large variety of programming languages available to
choose from and this is largely down to a trade-offs between
`productivity for writing`, `speed`, and `design for a purpose`.

**Low Level:**

Provide fine grained control

1. Assembly
2. LLVM (Assembler)

**Example:** `1 + 1` in assembly

```nasm
pushq   %rbp
movq    %rsp, %rbp
movl    $1, -12(%rbp)
movl    $1, -8(%rbp)
movl    -12(%rbp), %edx
movl    -8(%rbp), %eax
addl    %edx, %eax
movl    %eax, -4(%rbp)
movl    -4(%rbp), %eax
popq    %rbp
```

**Intermediate Level:**

1. C/C++
2. Fortran
3. Java

:::{admonition} Design for Purpose:
Linus Torvalds thinks `C` is the [best language choice](https://www.reddit.com/r/programming/comments/1t0gfy/linus_torvalds_on_the_question_if_there_is_a/) for writing
the `linux` kernel. This is because the `C` programming language
is a nice balance between `low-level` and `productivity`. It is
`productive` enough to write large and complex systems reasonably
quickly but has enough access to `low-level` features to build
interfaces for `hardware` and `systems`.

It is a good fit for writing `operating system kernels`.
:::

**Example:** `1 + 1` in C

```c
#include<stdio.h>
int main()
{
int sum = 0;
sum = 1 + 1;
printf("Sum = %d\n", sum);
return 0;
}
```

**High Level:**

Provide a high degree of productivity through `abstraction` and
`automation` etc.

**Features:** Automatic memory management, input and output, and
advanced `native support` for objects that improve `productivity`

1. Ruby
2. Javascript
3. Python
4. Julia

**Example:** `1 + 1` in python

```python
1 + 1
```

## Scientific Computing

**Scientific Computing** ultimately requires:

1. `Productive` - easy to read, write, debug, explore
2. `Fast` computations

In `scientific computing` we also don't want to have to worry much
about interfacing or managing the `hardware` on a day to day
basis -- however we do want the ability to maximise usage of that
hardware when required.

## Trade-Offs (Productivity vs Execution)

These two requirements typically come with a `trade-off`:

```{figure} img/tradeoff.pdf
```

```{figure} img/tradeoff2.pdf
```

```{figure} img/tradeoff3.pdf
```

```{figure} img/tradeoff4.pdf
```

One of the strengths of `python` is its adaptability to various
contexts while retaining a very high level of `productivity`.
This is largely due to `language design` (i.e. everything
is an object), and advances in access in `compute`. `Python`
was first released in `1991`. It has taken 20 years to become
as popular as it has become.

## Platforms: Windows, macOS, Linux


## Resources

Some additional resources for those interested:

1. [QuantEcon Python Programming](https://python-programming.quantecon.org)
2. [QuantEcon Python Intermediate Economics](https://python.quantecon.org)


