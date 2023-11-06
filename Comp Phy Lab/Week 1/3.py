
a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))

p = float(input('Input p: '))
q = float(input('Input q: '))
r = float(input('Input r: '))

if (a*q == p*b):
    if a/p == b/q and b/q == c/r and a/p == c/r:
        print("Infinite solutions")
    else:
        print("Parallel lines, No solutions")

else:
    x = ((r*b) - (q*c)) / ((p*b) - (a*q))
    y = ((a*r) - (p*c)) / ((a*q) - (p*b))
    print("x = {0}".format(x))
    print("y = {0}".format(y))