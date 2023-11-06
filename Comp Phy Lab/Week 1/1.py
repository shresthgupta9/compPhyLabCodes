import cmath

a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))

discriminant = (b**2) - (4 * a * c)

sol1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
sol2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
print('The solution are {0} and {1}'.format(sol1,sol2))