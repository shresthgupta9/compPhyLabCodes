import math
import matplotlib.pyplot as plt

h = 0.1
xi = 0
yi = 0
xf = math.pi / 2
yf = -3

def uDash(x, u, v):
    return v

def vDash(x, u, v):
    return (-1 * u)

def analytical(x):
    return (-3 * math.sin(x))

# storing x-coordinates
xco = []
i = 0
while (i <= (math.pi / 2)):
    xco.append(round(i, 2))
    i += h

size = len(xco)

# euler method
def euler(uo, vo):
    uval = [0] * size
    vval = [0] * size
    uval[0] = uo
    vval[0] = vo

    for i in range(1, size):
        uval[i] = uval[i - 1] + (h * uDash(xco[i - 1], uval[i - 1], vval[i - 1]))
        vval[i] = vval[i - 1] + (h * vDash(xco[i - 1], uval[i - 1], vval[i - 1]))
    return uval

# guessing values of y'(x = 0)
alpha = 10
beta = 20

slope = ((beta - alpha) / (euler(yi, beta)[size - 1] - euler(yi, alpha)[size - 1]) * (yf - euler(yi, alpha)[size - 1])) + alpha

yshooting = euler(0, slope)
yanaly = []

for j in range(size):
    yanaly.append(analytical(xco[j]))

# plotting graph
plt.plot(xco, yshooting, label = "Shooting/Euler")
plt.plot(xco, yanaly, label = "Analytical")
plt.legend()
plt.show()