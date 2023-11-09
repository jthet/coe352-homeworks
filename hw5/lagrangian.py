import numpy as np
import matplotlib.pyplot as plt

# Define the mesh points
nodes = np.linspace(0, 1, 5)  # 5 nodes for a four-element mesh

# Calculate the function values at the nodes
f_values = np.sin(np.pi * nodes)

# Define the basis functions (hat functions) for linear finite elements


def basis_function(x, i, nodes):
    if (i > 0) and (i < len(nodes) - 1):
        if nodes[i-1] <= x <= nodes[i]:
            return (x - nodes[i-1]) / (nodes[i] - nodes[i-1])
        elif nodes[i] < x <= nodes[i+1]:
            return (nodes[i+1] - x) / (nodes[i+1] - nodes[i])
    return 0.0

# Define the finite element interpolant function


def fe_interpolant(x, nodes, f_values):
    f_h = 0.0
    for i in range(len(nodes)):
        f_h += f_values[i] * basis_function(x, i, nodes)
    return f_h


# Create a fine mesh to plot the functions
x_fine = np.linspace(0, 1, 1000)
f_exact = np.sin(np.pi * x_fine)
f_approx = np.array([fe_interpolant(xi, nodes, f_values) for xi in x_fine])

# Plot the exact function and the finite element interpolant
plt.figure(figsize=(10, 6))
plt.plot(x_fine, f_exact, label='f(x) = sin(πx)', color='black')
plt.plot(x_fine, f_approx, label='fh(x) (FE Interpolant)',
         linestyle='--', color='red')
plt.scatter(nodes, f_values, color='red', zorder=5, label='Nodes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Comparison of f(x) and the Finite Element Interpolant, fh(x)')
plt.grid(True)
plt.show()
