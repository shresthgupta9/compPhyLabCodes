from matplotlib import pyplot as plt
import math

def factorial(x):
    if x == 0 or x == 1:
        return x                                                        
    else:
        return (x * factorial(x-1))
piby20x = []
piby20 = []
piby3x = []
piby3 = []

i = 0
n = 10
while (i * (math.pi / 20) <= math.pi):
    ans = 0
    for j in range(n + 1):
        ans += (pow(-1, j) * pow(i * (math.pi / 20) , (2*j)+1)) / factorial((2*j)+1)
    piby20.append(ans)
    piby20x.append(i * (math.pi / 20))
    i += 1
    
i = 0
while (i * (math.pi / 3) <= math.pi):
    ans = 0
    for j in range(n + 1):
        ans += (pow(-1, j) * pow(i * (math.pi / 3) , (2*j)+1)) / factorial((2*j)+1)
    piby3.append(ans)
    piby3x.append(i * (math.pi / 3))
    i += 1

plt.plot(piby20x, piby20)
plt.plot(piby3x, piby3)
plt.show()

# print(piby20x)
# print(piby20)
# print("\n")
# print(piby3x)
# print(piby3)
