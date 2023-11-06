# only 1 root 1.7963
def eqn (x):
    return ((x**3) - x - 4)

def derivative (x):
    return (3 * (x**2) - 1)

def newtonMethod(x, epsilon):
    while(abs(eqn(x)) > epsilon):
        delta = -1 * (eqn(x) / derivative(x))
        x += delta

    return x

guess = 5
epsilon = 10**(-4)

print(newtonMethod(guess, epsilon))