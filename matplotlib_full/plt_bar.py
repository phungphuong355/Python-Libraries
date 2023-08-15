#! /usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

# Bar 1
x = np.array([x for x in 'abcdef'])
y = np.array([3, 4, 6, 8, 3, 4])
plt.bar(x, y)
plt.show()

# Bar 2
x = np.array([x for x in 'abcdef'])
y = np.array([3, 4, 6, 8, 3, 4])
plt.barh(x, y)
plt.show()

# Hist 3
x = np.random.normal(179, 10, 250)
plt.hist(x)
plt.show()

