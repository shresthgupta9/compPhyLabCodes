from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

# given values
dx = 0.01
dt = dx / 2
v = 1
steps = 100

# x and t coordinate, taking steps as 100 so x is 0 to 1 and t is 0 to 0.5
xco = np.arange(0, 1, dx)
tco = np.arange(0, 0.5, dt)

# central difference matrix taking i as x and j as t
central = np.empty(shape=(steps, steps), dtype=int) # or np.zeros

# upwind scheme matrix taking i as x and j as t
upwind = np.empty(shape=(steps, steps), dtype=int) # or np.zeros

# setting u(x, 0) = 1
for i in range(100):
    central[i][0] = 1
    upwind[i][0] = 1

# central difference
for j in range(len(central[i]) - 1): # column
    for i in range(len(central)): # row
        central[i][j + 1] = central[i][j] + ((v * dt / 2 / dx) * ((central[i + 1][j] if i + 1 < 100 else 1) - central[i - 1][j]))

# upwind scheme
for j in range(len(upwind[i]) - 1): # column
    for i in range(len(upwind)): # row
        upwind[i][j + 1] = upwind[i][j] + ((v * dt / dx) * (upwind[i][j] - upwind[i - 1][j]))

# plotting 3d surface
X, T = np.meshgrid(xco, tco)
# ax.plot_surface(X, T, central)
# ax.plot_surface(X, T, upwind)
plt.show()