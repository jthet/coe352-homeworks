# COE 352 Homework 3

## Introduction
This homework uses the following IVP:

```math
\frac{dy}{dt} = -\alpha y\\
```
```math
y(0) = 1, \alpha > 0, 0 ≤ t ≤ T
```

#### Calculating the exact solution
To calculate the exact solution, the following logic was used:
```math
\frac{dy}{dt} = -\alpha y
```
```math
\frac{dy}{y} = -\alpha dt
```
```math
\int {\frac{dy}{y}} = \int {-\alpha dt}
```
```math
ln(y) + C = - \alpha t
```
```math
y = e^ {\alpha t + C} = Ce^ {\alpha t}
```
Then using the initial condition y(0) = 1, we get our exact solution:
```math
y = e^ {\alpha t}
```


## Forward Euler
Now, we will derive the update equation using Forward Euler time discretization
Forward Euler:
```math
y_{n+1} = y_n + \Delta t \cdot f(t_n, y_n)
```
where
```math
f(t_n, y_n) = \frac{dy}{dt} = -\alpha y\\
```
We get:
```math
y_{n+1} = y_n + \Delta t \cdot f(t_n, y_n) = y_n - \Delta t \alpha y_n = y_n (1 - \alpha \Delta t)
```
Therefore, our update equation using Forward Euler time discretization is:
```math
y_{n+1} = y_n (1 - \alpha \Delta t)
```

Furthermore, we know that Forward Euler time discretization loses stability with growth factors greater than 1, so we can derive a stability condition as follows:
```math
|(1 - \alpha \Delta t)| ≤ 1
```
So, our stability condition is:
```math
0 ≤ \alpha \Delta t ≤ 2 
```
The python script to find the numerical solution using this method is `forwardEuler.py`.

The Plot of the numerical and exact solution for various values &Delta;t, using &alpha; = 1:

![Forward Euler Plot](https://github.com/jthet/coe352-homeworks/blob/main/hw3/images/Figure_1.png)

Using only convergent &Delta;t's:
![Forward Euler Plot Convergent](https://github.com/jthet/coe352-homeworks/blob/main/hw3/images/Figure_2.png)


## Backward Euler
Now, we will derive the update equation using Backward Euler time discretization
Backward Euler:
```math
y_{n+1} = y_n + \Delta t \cdot f(t_{n+1} y_{n+1}
```

Using
```math
y_{n+1} = y_n + \Delta t f(t_{n+1} y_{n+1}) = y_n - \alpha \Delta t y_{n+1}
```
We can then derive our Backward Euler Output equation:

```math
y_{n+1} = \frac {y_n}{1 + \alpha \Delta t} 
```
It should be noted that the backward euler method for this IVP is unconditionally stable, as the stability condition is

```math
|\frac {1}{1 + \alpha \Delta t}| ≤ 1
```
Which is always satisfied as both &Delta;t and &alpha; are always positive.


The python script to find the numerical solution using this method is `backwardEuler.py`.

The Plot of the numerical and exact solution for various values &Delta;t, using &alpha; = 1:

![Forward Euler Plot](https://github.com/jthet/coe352-homeworks/blob/main/hw3/images/Figure_3.png)



## Trapezoidal Method
Now, we will derive the update equation using Forward Euler time discretization
Backward Euler:
```math
y_{n+1} = y_n + \Delta t \cdot f(t_{n+1} y_{n+1}
```

Using
```math
y_{n+1} = y_n + \Delta t f(t_{n+1} y_{n+1}) = y_n - \alpha \Delta t y_{n+1}
```
We can then derive our Backward Euler Output equation:

```math
y_{n+1} = \frac {y_n}{1 + \alpha \Delta t} 
```
It should be noted that the backward euler method for this IVP is unconditionally stable, as the stability condition is

```math
|\frac {1}{1 + \alpha \Delta t}| ≤ 1
```
Which is always satisfied as both &Delta;t and &alpha; are always positive.


The python script to find the numerical solution using this method is `backwardEuler.py`.

The Plot of the numerical and exact solution for various values &Delta;t, using &alpha; = 1:

![Forward Euler Plot](https://github.com/jthet/coe352-homeworks/blob/main/hw3/images/Figure_4.png)

