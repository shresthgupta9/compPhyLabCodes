# roots are -2.4909, 0.6566 and 1.8342
def eqn (x):
    return ((x**3) - (5 * x) + 3)

def bisectionMethod(low, high, epsilon):
    mid = (low + high) / 2
    while(abs(eqn(mid)) > epsilon):
        mid = (low + high) / 2
        if ((eqn(low) * eqn(mid)) < 0):
            high = mid
        elif((eqn(high) * eqn(mid)) < 0):
            low = mid

    return low
    
low = [-5, 0, 1]
high = [0, 1, 5]
epsilon = 10**(-4)

for i in range (3):
    print(bisectionMethod(low[i], high[i], epsilon))