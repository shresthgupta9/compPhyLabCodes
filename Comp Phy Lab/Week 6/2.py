import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

# given values
dx = 0.1
dt = 0.0025
xco = np.arange(0, 1 + dx, dx)
tco = np.arange(0, 0.1 + dt, dt)
explicit = np.empty(shape=(len(xco), len(tco)), dtype=float) # or np.zeros

# initial conditions
for i in range(len(explicit)):
  explicit[i][0] = math.sin(3 * math.pi * xco[i] / 2)
for j in range(len(explicit[0])):
  explicit[0][j] = 0

# explicit method
"""
row only goes from 0 to second last because for last
column del u / del x = 0 so from condition u(n, j + 1) = u(n, j)
"""
for j in range(len(explicit[0]) - 1):
    for i in range(1, len(explicit) - 1):
        explicit[i][j + 1] = explicit[i][j] + ((dt / (dx**2)) * (explicit[i + 1][j] - (2 * explicit[i][j]) + explicit[i - 1][j]))
    explicit[len(explicit) - 1][j + 1] = explicit[len(explicit) - 2][j + 1]

# print(explicit)

# implicit method
"""
not sure if its solvable by implicit method
"""

T, X = np.meshgrid(tco, xco)
ax.plot_surface(X, T, explicit)
plt.show()