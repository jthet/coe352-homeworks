#!/usr/bin/env python3
def bisection_method(f, a, b, tol, max_iter):
    '''
    Finds an approximate root of a function within an interval.

    Parameters:
        f <function>: The function for which the root is sought.

        a <float>: Left endpoint of the interval [a, b].

        b <float>: Right endpoint of the interval [a, b].

        tol <float>: Tolerance level for convergence.

        max_iter <int>:Maximum number of iterations.

    Returns:
        <float>: Approximate root of the function within the interval.

    Example:
        root = bisection_method(lambda x: x**2 - 3, 1, 2, 1e-6, 100)
    '''

    # initial check
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at interval end points must have opposite signs")
    
    iters = 0
    
    while (b - a) / 2 > tol and iters < max_iter:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint  # Found the root exactly
        elif f(a) * f(midpoint) < 0:
            b = midpoint # update right side if dif signs 
        else:
            a = midpoint # update left side if signs are the same
        iters += 1

    return (a + b) / 2

# function f(x) for this hw problem
def f(x):
    return x**2 - 3

# interval [a, b]
a = 1
b = 2

# tolerance and max iterations
tolerance = 1e-8
max_iter=100

# Call the bisection method to find the root
root = bisection_method(f, a, b, tolerance, max_iter)

# Print the result
print("Approximate root:", root)
