import matplotlib.pyplot as plt
import math
import numpy as np

# defining given values
h = 0.001

def lhs(x):
    return (x**3 - (132 * (x**2) / 32) + (28 * x / 32) + (147 / 32))

def rhs(x):
    return (5 * math.sin(x))

# storing x-coordinates
i = -2
xco = []
while (i < 4):
    xco.append(i)
    i += h

# storing lhs and rhs values
lval = []
rval = []
for i in range(len(xco)):
    lval.append(lhs(xco[i]))
    rval.append(rhs(xco[i]))

# plotting graph
plt.plot(xco, lval, label = "LHS")
plt.plot(xco, rval, label = "RHS")
plt.legend()
plt.show()