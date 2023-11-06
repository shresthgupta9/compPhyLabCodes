import matplotlib.pyplot as plt
import math

# defining given values
def diffEqn(x, y):
    return ((x + y) * math.sin(x))
h = 0.1

# storing x-coordinates
xco = []
for i in range(61):
    xco.append(round((i * 0.1), 1))

# RK-2 method
rk2 = [0] * 61
rk2[0] = 5
for i in range(1, 61):
    k1 = h * diffEqn(xco[i - 1], rk2[i - 1])
    k2 = h * diffEqn(xco[i - 1] + (h / 2), rk2[i - 1] + (k1 / 2))
    # k2 = h * diffEqn(xco[i - 1] + h, rk2[i - 1] + k1)
    rk2[i] = rk2[i - 1] + ((k1 + k2) / 2)

# RK-4 method
rk4 = [0] * 61
rk4[0] = 5
for i in range(1, 61):
    k1 = h * diffEqn(xco[i - 1], rk4[i - 1])
    k2 = h * diffEqn(xco[i - 1] + (h / 2), rk4[i - 1] + (k1 / 2))
    k3 = h * diffEqn(xco[i - 1] + (h / 2), rk4[i - 1] + (k2 / 2))
    k4 = h * diffEqn(xco[i - 1] + h, rk4[i - 1] + k3)
    rk4[i] = rk4[i - 1] + (k1 / 6) + (k2 / 3) + (k3 / 3) + (k4 / 6)

# plotting graph
plt.plot(xco, rk2, label = "RK-2")
plt.plot(xco, rk4, label = "RK-4")
plt.legend()
plt.show()