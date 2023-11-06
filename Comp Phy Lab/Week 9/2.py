import numpy as np
import matplotlib.pyplot as plt

k_b = 1  
T = 300  
m = 1  
n = 1

total_time = 10
num_steps = 10000  
dt = total_time / num_steps

x0 = 1
v0 = 1

random_force = np.random.normal(0, 1, num_steps)

x_v = np.zeros(num_steps)
v_v = np.zeros(num_steps)

x_v[0] = x0
v_v[0] = v0

for i in range(1, num_steps):
    a = (-n * v_v[i - 1] + (random_force[i])*(np.sqrt(2 * k_b * T * n * dt))) / m
   
    v_v[i] = v_v[i - 1] + a * dt
    x_v[i] = x_v[i - 1] + v_v[i] * dt

mean_displacement = np.mean(x_v)

mean_squared_displacement = np.mean(np.square(x_v))

print("Mean Displacement:", mean_displacement)
print("Mean Squared Displacement:", mean_squared_displacement)