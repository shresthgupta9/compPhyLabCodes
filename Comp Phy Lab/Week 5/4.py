import matplotlib.pyplot as plt

# defining given values
h = 0.1
yi = 1
ydash_i = 0

def uDash(x, u, v):
    return v

def vDash(x, u, v):
    return ((x * (v**2)) - (u**2))

# storing x-coordinates
i = 0
xco = []
while (i <= 10):
    xco.append(round(i, 2))
    i += h

size = len(xco)

# RK-4 method
def rkfour(uo, vo):
    uval = [0] * size
    vval = [0] * size
    uval[0] = uo
    vval[0] = vo

    for i in range(1, size):
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

rk4 = rkfour(yi, ydash_i)

# plotting graph
plt.plot(xco, rk4, label = "RK-4")
plt.legend()
plt.show()