import matplotlib.pyplot as plt

# only 1 root 1.6006
def eqn (x):
    return (2 * (x**3) - (2 * x) - 5)

def derivative (x):
    return (6 * (x**2) - 2)

newtonx = []
newtony = []
secantx = []
secanty = []

def newtonMethod(x, epsilon):
    newtonitr = 0
    while(abs(eqn(x)) > epsilon):
        delta = -1 * (eqn(x) / derivative(x))
        x += delta
        newtonx.append(x)
        newtony.append(eqn(x))
        newtonitr += 1

    return x, newtonitr

def secantMethod (prev, next, epsilon):
    secantitr = 0
    while (abs(eqn(next)) > epsilon):
        temp = next - (((next - prev) * eqn(next)) / (eqn(next) - eqn(prev)))
        prev = next
        next = temp
        secantx.append(next)
        secanty.append(eqn(next))
        secantitr += 1
    
    return next, secantitr

prev = 0
next = 5
epsilon = 10**(-4)

print("Root from Newton Raphson method is", newtonMethod(next, epsilon)[0])
print("Root from Secant method is", secantMethod(prev, next, epsilon)[0])
print("Number of iterations for newton method is", newtonMethod(next, epsilon)[1])
print("Number of iterations for secant method is", secantMethod(prev, next, epsilon)[1])

plt.plot(newtonx, newtony, label = "Newton Raphson")
plt.plot(secantx, secanty, label = "Secant Method")
plt.legend()
plt.show()