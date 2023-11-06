print("The matrix is like this\na b\nc d")

a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))
d = float(input('Input d: '))

determinant = abs(a*d - b*c)

if(determinant == 0):
    print ("Inverse does not exist")


else:
    newa = d / determinant
    newb = -b / determinant
    newc = -c / determinant
    newd = a / determinant
    print("The Inverse of given matrix is\n{0} {1}\n{2} {3}".format(newa, newb, newc, newd))