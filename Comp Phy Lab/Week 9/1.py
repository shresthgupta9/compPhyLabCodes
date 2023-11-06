import numpy as np
import matplotlib.pyplot as plt

arr = np.random.normal(size=10000)

mean = arr.mean()
standardDeviation = arr.std()

print("mean = " + str(mean))
print("standard deviation = " + str(standardDeviation))

plt.hist(arr, 96)
plt.show()