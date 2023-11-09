# Homework 5

This directory contains a Python script `galerkin.py` and `lagrangian.py` that perform the galerkin and lagrangian finite element approximations on a 1 dimensional grid [0, 1].

* Note: The homework has been turned into canvas, this repository just shows the plots and code.


## Question 1:
1) Use a uniform four-element mesh on [0, 1] and piecewise Lagrangian
linear finite element basis functions to construct a finite element interpolant, fh of
the function f (x) = sin(πx), that is, set the values fh(xi) = sin(πxi), i = 1, 2, 3, 4, 5,
and plot the function f and fh.

See `lagrangian.py`

Here is the plot:

![plot 1](https://github.com/jthet/coe352-homeworks/blob/main/hw5/images/q1.png)



## Question 2:
### Part C:
For the Galerkin approximation of the problem, let N = 3 and choose
the basis function φi = sin(iπx), i = 1, 2, 3. Calculate the stiffness matrix, Kij
and the load vector fi. Solve for the coefficients and construct the approximate
solution yh. Plot the exact and approximate solutions.

![plot 2](https://github.com/jthet/coe352-homeworks/blob/main/hw5/images/q2_c.png)

### Part D:
Using a uniform mesh with mesh size h = 0.25, compute the Galerkin
piece-wise linear finite element approximation by hand. Plot the exact and
approximate solutions.

![plot 3](https://github.com/jthet/coe352-homeworks/blob/main/hw5/images/q3_c.png)


