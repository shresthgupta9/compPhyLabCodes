import numpy as np

# given function
def fn(x):
    return (np.exp(-1 * (x ** 2)))

# expectaion of x function
def expec_x(x):
    return (x * np.exp(-1 * (x ** 2)))

# expectaion of x square function
def expec_x_square(x):
    return ((x**2) * np.exp(-1 * (x ** 2)))

# simpson 1/3 fn
def simpson(xco, h, fn):
    integration = 0
    for i in range(len(xco) - 2):
        if(i % 2 == 0):
            integration += (h / 3) * (fn(xco[i]) + (4 * fn(xco[i + 1])) + fn(xco[i + 2]))
    return integration

# x-co
h = 0.01
lower_limit = -10
upper_limit = 10
xco = np.arange(lower_limit, upper_limit + h, h)

# calculating A
A = 1 / (simpson(xco, h, fn))
print(A)

# first moment
expectation_of_x = A * simpson(xco, h, expec_x)
print(expectation_of_x)

# second moment
expectation_of_x_square = A * simpson(xco, h, expec_x_square)
print(expectation_of_x_square)