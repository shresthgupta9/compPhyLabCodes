import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
L = 100  
N = 20  
dx = L / N  
dy = L / N  

# Initialize the temperature distribution grid
T = np.zeros((N+1, N+1))

# Set boundary conditions
T[:, 0] = -100  
T[:, -1] = 100
T[0, :] = (T[0, 1] + T[1, 0]) / 2  
T[0, -1] = (T[0, -2] + T[1, -1]) / 2  
T[-1, :] = (T[-2, 0] + T[-1, 1]) / 2  
T[-1, -1] = (T[-2, -1] + T[-1, -2]) / 2  


num_iterations = 1000
for _ in range(num_iterations):
    T_new = T.copy()
    for i in range(1, N):
        for j in range(1, N):
            T_new[i, j] = (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1]) / 4
    T = T_new

# Create a grid of x and y values
x = np.linspace(0, L, N+1)
y = np.linspace(0, L, N+1)
X, Y = np.meshgrid(x, y)

# Create a 3D surface plot of the temperature distribution
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, T, cmap='viridis')

# Set labels and title
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')
ax.set_zlabel('Temperature (°C)')
plt.title('Temperature Distribution on a Square Plate')

# Show the plot
plt.show()