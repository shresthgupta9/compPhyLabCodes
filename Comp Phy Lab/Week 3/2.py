import matplotlib.pyplot as plt
import math
import numpy as np

# defining given values
h = 0.1
def uDash(x, u, v):
    return v

def vDash(x, u, v):
    return ((10 * math.sin(x)) - (5 * v) - (6 * u))

def analytical(x):
    return ((-6 * math.exp(-3 * x)) + (7 * math.exp(-2 * x)) + math.sin(x) - math.cos(x))

# storing x-coordinates
xco = []
for i in range(31):
    xco.append(round((i * 0.1), 1))

# euler method
def euler(uo, vo):
    uval = [0] * 31
    vval = [0] * 31
    uval[0] = uo
    vval[0] = vo

    for i in range(1, 31):
        uval[i] = uval[i - 1] + (h * uDash(xco[i - 1], uval[i - 1], vval[i - 1]))
        vval[i] = vval[i - 1] + (h * vDash(xco[i - 1], uval[i - 1], vval[i - 1]))
    return uval

eulY = euler(0, 5)

# RK-4 method
def rkfour(uo, vo):
    uval = [0] * 31
    vval = [0] * 31
    uval[0] = uo
    vval[0] = vo

    for i in range(1, 31):
        k1u = h * uDash(xco[i - 1], uval[i - 1], vval[i - 1])
        k1v = h * vDash(xco[i - 1], uval[i - 1], vval[i - 1])

        k2u = h * (uDash(xco[i - 1] + (h / 2), uval[i - 1] + (k1u / 2), vval[i - 1] + k1v / 2))
        k2v = h * (vDash(xco[i - 1] + (h / 2), uval[i - 1] + (k1u / 2), vval[i - 1] + k1v / 2))

        k3u = h * (uDash(xco[i - 1] + (h / 2), uval[i - 1] + (k2u / 2), vval[i - 1] + (k2v / 2)))
        k3v = h * (vDash(xco[i - 1] + (h / 2), uval[i - 1] + (k2u / 2), vval[i - 1] + (k2v / 2)))

        k4u = h * (uDash(xco[i - 1] + h, uval[i - 1] + k3u, vval[i - 1] + k3v))
        k4v = h * (vDash(xco[i - 1] + h, uval[i - 1] + k3u, vval[i - 1] + k3v))

        uval[i] = uval[i - 1] + (k1u / 6) + (k2u / 3) + (k3u / 3) + (k4u / 6)
        vval[i] = vval[i - 1] + (k1v / 6) + (k2v / 3) + (k3v / 3) + (k4v / 6)

    return uval

rk4 = rkfour(0, 5)

# analytical method
analY = [0] * 31
for i in range(31):
    analY[i] = analytical(xco[i])

# plotting graph
plt.plot(xco, eulY, label = "Euler")
# rk4 and analytical are overlapping
plt.plot(xco, rk4, label = "RK-4")
plt.plot(xco, analY, label = "Analytical")
plt.legend()
plt.show()