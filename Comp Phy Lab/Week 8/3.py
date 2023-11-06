import numpy as np

# given function
def fn(x, y):
    return ((y**2) - x)

# simpson 1/3 fn
def simpson(xco, h, fn):
    integration = 0
    for i in range(len(xco)):
        yco = np.arange((xco[i] - 2)**2, 6 + h, h)
        for j in range(len(yco) - 2):
            if(j % 2 == 0):
                integration += (h / 3) * (fn(xco[i], yco[j]) + (4 * fn(xco[i], yco[j + 1])) + fn(xco[i], yco[j + 2]))
    return integration

# x-co
h = 0.01
lower_limit = 0
upper_limit = 1
xco = np.arange(lower_limit, upper_limit + h, h)

integration = h * simpson(xco, h, fn)

print(integration)