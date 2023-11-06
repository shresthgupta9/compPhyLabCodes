import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

# given and assuming 
rod = 10 # cm
time = 100 # sec
dx = 0.1
dt = 0.01
k = 0.25

# setting coordinates
xco = np.arange(0, rod + dx, dx)
tco = np.arange(0, time + dt, dt)
u = np.empty([len(xco), len(tco)], dtype=float)

# initial conditions
for i in range(len(u)):
    u[i][0] = 0
for j in range(len(u[0])):
    u[0][j] = 100
    u[len(u) - 1][j] = 50

# explicit method
"""
row only goes from 0 to second last because for last
column del u / del x = 0 so from condition u(n, j + 1) = u(n, j)
"""
for j in range(len(u[0]) - 1):
    for i in range(1, len(u) - 1):
        u[i][j + 1] = u[i][j] + ((k * dt / (dx**2)) * (u[i + 1][j] - (2 * u[i][j]) + u[i - 1][j]))

T, X = np.meshgrid(tco, xco)
ax.plot_surface(T, X, u)
plt.show()