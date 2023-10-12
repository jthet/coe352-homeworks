#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def odefunc(y, a):
    # y' = dy/dt = f(y, t) = - a * y
    return -a * y

# Forward Euler method
def trapezoidal(y0, a, dt, T):
    N = int(T/dt)  # Number of steps
    y = np.zeros(N)
    t = np.zeros(N)
    y[0] = y0 # initial condition

    for n in range(0, N-1):
        y[n+1] = (y[n] * (1 - (a * dt / 2))) / (1 + (a * dt / 2))
        t[n+1] = t[n] + dt

    return t, y


def exact_solution(y0, a, t):
    return y0 * np.exp(-a * t)

def main():
    # Parameters
    y0 = 1  # Initial value
    a = 1  # chosing alpha (constant) to be 1
    T = 10  # Total time

    # Use range of dt for stability analysis, contains both stable and unstable
    # we know dt is positive, and must follow dt <= 2/a, or for a=1 , dt <=2
    dt_values = [0.001, 0.01, 0.1, 1.0, 1.5, 2, 2.5, 3] # mix of stable and unstable (unstable for forward euler)
    # dt_values = [0.001, 0.01, 0.1, 0.5, 1.0, 1.5]  # all stable

    # Plot
    for dt in dt_values:
        t, y = trapezoidal(y0, a, dt, T)
        plt.plot(t, y, label=f'dt={dt}')

    # Plotting the exact solution
    t_exact = np.linspace(0, T, 1000)
    y_exact = exact_solution(y0, a, t_exact)
    plt.plot(t_exact, y_exact, 'k--', label='Exact')

    plt.xlabel('Time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.title('Trapezoidal Method: Stability Analysis')
    plt.show()

if __name__ == '__main__':
    main()