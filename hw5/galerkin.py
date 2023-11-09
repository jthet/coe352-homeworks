import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Note this is for a grid from [0, 1]

num_steps = int(input("How many steps?:\n*for a step size of h=0.25, there are 4 steps\n")) +1


# Number of basis functions
N = 3

# Define the basis funcs
def phi(i, x):
    return np.sin(i * np.pi * x)

def dphi(i, x):
    return i * np.pi * np.cos(i * np.pi * x)

# Stiffness matrix calc, K
K = np.zeros((N, N))
for i in range(1, N+1):
    for j in range(1, N+1):
        K[i-1, j-1], _ = quad(lambda x, i, j: dphi(i, x)
                              * dphi(j, x), 0, 1, args=(i, j))

# Calculate F
f = np.zeros(N)
for i in range(1, N+1):
    f[i-1], _ = quad(lambda x, i: phi(i, x) * x, 0, 1, args=(i,))

# solve coefficients with Ku=f, (but c instead of u)
c = np.linalg.solve(K, f)

# find approx solution
def yh(x):
    return sum(c[i-1] * phi(i, x) for i in range(1, N+1))

# find exact solution


def y_exact(x):
    return x * (1 - x**2) / 6


# Mesh
x_mesh = np.linspace(0, 1, 1000)
x_mesh_approx = np.linspace(0, 1, num_steps)

# Evaluate the approximate and exact solutions on the mesh
yh_values = np.array([yh(x) for x in x_mesh_approx])
y_exact_values = np.array([y_exact(x) for x in x_mesh])

# Plot the approximate and exact solutions
plt.figure(figsize=(10, 6))
plt.plot(x_mesh_approx, yh_values,
         label='Approximate Solution $y_h(x)$', color='black')
plt.plot(x_mesh, y_exact_values, label='Exact Solution $y(x)$',
         linestyle='--', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(f'Exact vs Approximate Solutions, h = {1/(num_steps-1)}')
plt.grid(True)
plt.show()
