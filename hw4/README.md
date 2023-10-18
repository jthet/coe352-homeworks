# Homework 4

This directory contains a Python script named "bisection.py" that uses the Bisection Method to find an approximate root of a function within a specified interval.

## Script Description:

- `bisection_method` function: This function takes a function `f`, left (`a`) and right (`b`) endpoints of an interval, a tolerance level (`tol`), and a maximum number of iterations (`max_iter`). It then iteratively applies the Bisection Method to approximate a root of the function within the given interval. The function returns the approximate root.

- `f(x)` function: This is the function used in this homework problem, but can be replaces with any function

- Interval `[a, b]`: The interval in which the root of the function should be contained.

- Tolerance and Maximum Iterations: You can adjust the tolerance level (`tolerance`) and the maximum number of iterations (`max_iter`) as per your requirements.

## Usage:

To use the script, simply run it using a Python 3 interpreter. It will calculate and print the approximate root of the function within the specified interval.

Example usage:

```bash
$ python3 bisection.py
Approximate root: 1.7320508137345314
```

For this specific script, it will find an approximate root of the function `f(x) = x^2 - 3` within the interval [1, 2] with a tolerance level of 1e-8 and a maximum of 100 iterations.

