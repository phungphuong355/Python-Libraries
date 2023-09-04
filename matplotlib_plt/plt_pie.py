#! /usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

# Pie 1
y = np.array([35, 25, 15, 35])
plt.pie(y)
plt.show()

# Pie 2
y = np.array([35, 25, 15, 35])
labels = np.array(['apple', 'orange', 'mango', 'melon'])
plt.pie(y, labels=labels)
plt.show()

# Pie 3
y = np.array([35, 25, 15, 35])
labels = np.array(['apple', 'orange', 'mango', 'melon'])
explore = np.array([0.2, 0.1, 0.1, 0.1])
plt.pie(y, labels=labels, explode=explore, shadow=True)
plt.show()

# Pie 4
y = np.array([35, 25, 15, 35])
labels = np.array(['apple', 'orange', 'mango', 'melon'])
colors = np.array(['black', 'green', 'blue', 'orange'])
explore = np.array([0.2, 0.1, 0.1, 0.1])
plt.pie(y, labels=labels, explode=explore, shadow=True, colors=colors)
plt.show()
