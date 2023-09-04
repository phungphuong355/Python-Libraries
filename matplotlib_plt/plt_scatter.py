#! /usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

# Scatter 1
x = np.array([3, 1, 5, 6, 6, 8])
y = np.array([3, 4, 6, 8, 3, 4])
plt.scatter(x=x, y=y)
plt.show()

# Scatter 2
x = np.array([3, 1, 5, 6, 6, 8, 7, 6, 8])
y = np.array([3, 4, 6, 8, 3, 4, 33, 66, 77])
plt.scatter(x, y, color='hotpink')
plt.show()

# Scatter 3
x = np.array([3, 1, 5, 6, 6, 8])
y = np.array([3, 4, 6, 8, 3, 4])
c = np.array([0, 20, 30, 50, 70, 100])
plt.scatter(x, y, c=c, cmap='copper_r')
plt.show()

# Scatter 4
x = np.array([3, 1, 5, 6, 6, 8])
y = np.array([3, 4, 6, 8, 3, 4])
c = np.array([1, 20, 30, 50, 70, 100])
s = np.array([10, 5, 2, 6, 7, 4])
plt.scatter(x, y, c=c, cmap='copper_r', s=s)
plt.show()

# Scatter 5
x = np.array([3, 1, 5, 6, 6, 8])
y = np.array([3, 4, 6, 8, 3, 4])
c = np.array([0, 20, 30, 50, 70, 100])
plt.scatter(x, y, c=c, cmap='copper_r', alpha=0.5)
plt.show()