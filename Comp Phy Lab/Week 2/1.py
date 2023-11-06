import matplotlib.pyplot as plt

# defining given values
def diffEqn(x, y):
    return x * y
h = 0.1

# storing x-coordinates
xco = []
for i in range(21):
    xco.append(round(1 + (i * 0.1), 1))

# euler's method
eulY = [0] * 21
eulY[0] = 5
for i in range(1, 21):
    eulY[i] = eulY[i - 1] + h * diffEqn(xco[i - 1], eulY[i - 1])

# improved euler's method
impEulY = [0] * 21
impEulY[0] = 5
for i in range(1, 21):
    impEulY[i] = impEulY[i - 1] + ((h / 2) * (diffEqn(xco[i - 1], impEulY[i - 1]) + diffEqn(xco[i - 1] + h, impEulY[i - 1] + (h * diffEqn(xco[i - 1], impEulY[i - 1])))))

# RK-2 method
rk2 = [0] * 21
rk2[0] = 5
for i in range(1, 21):
    k1 = h * diffEqn(xco[i - 1], rk2[i - 1])
    k2 = h * diffEqn(xco[i - 1] + h, rk2[i - 1] + k1)
    rk2[i] = rk2[i - 1] + ((k1 + k2) / 2)

# plotting graph
# the improved euler's method and rk-2 method are so close that they are overlapping in graph
plt.plot(xco, eulY)
plt.plot(xco, impEulY)
plt.plot(xco, rk2)
plt.show()