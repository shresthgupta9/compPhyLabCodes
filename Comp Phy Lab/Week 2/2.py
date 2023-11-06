import matplotlib.pyplot as plt
import math

# defining given values
def diffEqn(t, y):
    return (y - (t * t) + 1)
h = 0.1

# storing x-coordinates
xco = []
for i in range(21):
    xco.append(round((i * 0.1), 1))

# RK-2 method
rk2 = [0] * 21
rk2[0] = 0.5
for i in range(1, 21):
    k1 = h * diffEqn(xco[i - 1], rk2[i - 1])
    k2 = h * diffEqn(xco[i - 1] + h, rk2[i - 1] + k1)
    rk2[i] = rk2[i - 1] + ((k1 + k2) / 2)

# given analytical eqn
def analyticalFn(t):
    return ((t * t) + (2 * t) + 1 - (0.5 * math.exp(t)))
analy = [0] * 21
for i in range(21):
    analy[i] = analyticalFn(xco[i])

# calculating error
err = [0] * 21
for i in range(21):
    err[i] = analy[i] - rk2[i]    
    
plt.plot(xco, rk2)
plt.show()
plt.plot(xco, err)
plt.show()