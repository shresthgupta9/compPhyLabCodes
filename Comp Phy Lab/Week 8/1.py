import numpy as np

# given function
def fn(x):
    return ((x**2) * np.exp(x - 1))

# trapezoidal fn
def trapezoidal_integration(xco, h):
    integration = (h / 2) * (fn(xco[0]) + fn(xco[len(xco) - 1]))
    for i in range(1, len(xco) - 1):
        integration += (h * fn(xco[i]))
    return integration

# simpson 1/3 fn
def simpson(xco, h):
    integration = 0
    for i in range(len(xco) - 2):
        if(i % 2 == 0):
            integration += (h / 3) * (fn(xco[i]) + (4 * fn(xco[i + 1])) + fn(xco[i + 2]))
    return integration
        
# x-co
h = 0.01
lower_limit = 0
upper_limit = 1
xco = np.arange(lower_limit, upper_limit + h, h)

print(trapezoidal_integration(xco, h))
print(simpson(xco, h))