import matplotlib.pyplot as plt

h = 0.1
xi = 0
yi = 0
xf = 9
yf = 0

def uDash(x, u, v):
    return v

def vDash(x, u, v):
    return ((72 * x) - (8 * (x**2)) + (2 * u))

# storing x-coordinates
xco = []
i = 0
while (i <= 9):
    xco.append(round(i, 2))
    i += h

size = len(xco)

# RK-2 method
def rktwo(uo, vo):
    uval = [0] * size
    vval = [0] * size
    uval[0] = uo
    vval[0] = vo

    for i in range(1, size):
        k1u = h * uDash(xco[i - 1], uval[i - 1], vval[i - 1])
        k1v = h * vDash(xco[i - 1], uval[i - 1], vval[i - 1])

        k2u = h * (uDash(xco[i - 1], uval[i - 1], vval[i - 1]) + k1v / 2)
        k2v = h * (vDash(xco[i - 1] + (h / 2), uval[i - 1] + (k1u / 2), vval[i - 1] + k1v / 2))

        uval[i] = uval[i - 1] + k2u
        vval[i] = vval[i - 1] + k2v

    return uval

# guessing values of y'(x = 0)
alpha = 10
beta = 20

slope = ((beta - alpha) / (rktwo(yi, beta)[size - 1] - rktwo(yi, alpha)[size - 1]) * (yf - rktwo(yi, alpha)[size - 1])) + alpha

yshooting = rktwo(xi, slope)

# plotting graph
plt.plot(xco, yshooting, label = "Shooting/RK-2")
plt.legend()
plt.show()