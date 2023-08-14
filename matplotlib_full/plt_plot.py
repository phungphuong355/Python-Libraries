#! /usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

# Plot 1
x_point = np.array([1, 8])
y_point = np.array([3, 10])
plt.plot(x_point, y_point)
plt.show()
plt.plot(x_point, y_point, "o")
plt.show()

# Plot 2
y_points = np.array([3, 8, 1, 10, 5, 7])
plt.plot(y_points)
plt.plot(y_points, 'o')
plt.show()

# Plot 3
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, marker="o", linestyle='--')
plt.show()

# Plot 4
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, 'o:r')  # color: r, marker: o
plt.show()

# Plot 5
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, 'H--y', ms=15)  # color: y, marker: H
plt.show()

# Plot 6
y_points = np.array([3, 8, 1, 10])
plt.plot(y_points, 'H--y', ms=15, mec='r')
plt.show()

# Plot 7
y_points = np.array([3, 8, 1, 10, 17, 21, 18])
plt.plot(y_points, 'H--y', ms=15, mec='b', mfc='r')
plt.show()

# Plot 8
y_points = np.array([3, 8, 1, 10, 17, 21, 18])
plt.plot(y_points, color='b')
plt.show()

# Plot 9
y_points = np.array([3, 8, 1, 10, 17, 21, 18])
plt.plot(y_points, color='b', ls=':')
plt.show()

# Plot 10
x_point = np.array([3, 8, 1, 10, 17, 21, 18])
y_point = np.array([2, 11, 16, 23, 15])
plt.plot(x_point, color='b')
plt.plot(y_point, color='r')
plt.show()

# Plot 11
x_point = np.array([3, 8, 1, 10, 17, 21, 18])
y_point = np.array([2, 11, 16, 23, 15])
plt.subplot(2, 1, 1)
plt.plot(x_point, color='b')
plt.plot(y_point, color='r')

a_point = np.random.randint(1, 10, (5,))
b_point = np.random.randint(1, 5, (3,))
plt.subplot(2, 1, 2)
plt.plot(a_point, color='r')
plt.plot(b_point, color='y')
font = {'color': 'blue', 'size': 20}
plt.xlabel('Average Pulse', loc='left')
plt.ylabel('Calorie')
plt.title('Chart demo', fontdict=font)
plt.grid(color='y', linestyle=':', axis='x')
plt.show()
