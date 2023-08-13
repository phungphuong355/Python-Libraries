#!/usr/bin/env python
import numpy as np

# print(dir(np))
# help(np)

print(np.arange(6))  # [0 1 2 3 4 5]
print(np.random.randint(0, 10, 5))  # [4 6 3 8 2]

# Tensor 1
a = np.array([1, 2, 3, 4, 5, 6])
print(a)  # [1 2 3 4 5 6]
print(type(a))  # <class 'numpy.ndarray'>
print('Three last items: {}'.format(a[3:]))  # Three last items: [4 5 6]
print('The shape: {}'.format(a.shape))  # The shape: (6,)

# Tensor 2
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)  # [[1 2 3] [4 5 6]]
print(x.shape)  # (2, 3)
print(x[:, 1])  # [2 5]

# Tensor 1 zero
print(np.zeros(6))  # [0. 0. 0. 0. 0. 0.]
# Tensor 1 one
print(np.ones(6))  # [1. 1. 1. 1. 1. 1.]
print(np.empty(6))  # [1. 1. 1. 1. 1. 1.]

b = np.array([2, 1, 3, 4, 5, 6, 7, 8, 9])
print(np.sort(b))  # [1 2 3 4 5 6 7 8 9]
print(np.flip(b))  # [9 8 7 6 5 4 3 2 1]
# Change into Tensor 2 (3x3)
print(b.reshape(3, 3))  # [[1 2 3] [4 5 6] [7 8 9]]
# Chane into Tensor 2
print(b[np.newaxis, :])  # [[2 1 3 4 5 6 7 8 9]]
print(b[np.newaxis, :].shape)  # (1, 9)
print(np.expand_dims(b, axis=1))  # [[2] [1] [3] [4] [5] [6] [7] [8] [9]]
print(np.expand_dims(b, axis=1).shape)  # (9, 1)

a = np.arange(1, 13, 1).reshape(3, 4)
print(a)  # [[ 1  2  3  4] [ 5  6  7  8] [ 9 10 11 12]]
print(a[a > 5])  # [ 6  7  8  9 10 11 12]
print((a >= 5) | (a == 1))  # [[ True False False False] [ True  True  True  True] [ True  True  True  True]]

a1 = np.array([[1, 1],
               [2, 2]])
a2 = np.array([[3, 3],
               [4, 4]])
# Stack arrays in sequence vertically (row wise).
print(np.vstack((a1, a2)))  # [[1 1] [2 2] [3 3] [4 4]]
# Stack arrays in sequence horizontally (column wise).
print(np.hstack((a1, a2)))  # [[1 1 3 3] [2 2 4 4]]

a = np.arange(1, 25).reshape(2, 12)
print(a)  # [[ 1  2  3  4  5  6  7  8  9 10 11 12] [13 14 15 16 17 18 19 20 21 22 23 24]]
#  Split an array into multiple sub-arrays horizontally (column-wise).
print(np.hsplit(a, 3))
# [array([[ 1,  2,  3,  4], [13, 14, 15, 16]]),
# array([[ 5,  6,  7,  8], [17, 18, 19, 20]]),
# array([[ 9, 10, 11, 12], [21, 22, 23, 24]])]
print(np.hsplit(a, (3, 4)))
# [array([[ 1,  2,  3], [13, 14, 15]]),
# array([[ 4], [16]]),
# array([[ 5,  6,  7,  8,  9, 10, 11, 12], [17, 18, 19, 20, 21, 22, 23, 24]])]
print(a.copy())  # [[ 1  2  3  4  5  6  7  8  9 10 11 12] [13 14 15 16 17 18 19 20 21 22 23 24]]

a = np.array([1, 2])
b = np.ones(2, dtype=int)
print(a + b)  # [2 3]
print(a.sum())  # 3

a = np.array([[1, 2], [3, 4]])
print(a.sum(axis=0))  # [4, 6]
print(a * 2)  # [[2 4] [6 8]]
print(a.max())  # 4
print(a + 1)  # [[2 3] [4 5]]
x = np.array([4, 5])
print(a + x)  # [[5 7] [7 9]]

# Random array
rnd = np.random.default_rng()
a = rnd.integers(1, 20, 50)
print(np.unique(a))  # [ 1  2  3  5  6  7  8  9 10 11 12 13 15 16 17 18 19]
index, ulist, count = np.unique(a, return_index=True, return_counts=True)
print(index)  # [ 1  2  3  5  6  8  9 10 11 12 13 14 15 16 17 18 19]
print(ulist)  # [ 5 27 15  0 21 18  3 12 29 30  7 22  1  2  8 10  6]
print(count)  # [7 5 2 3 4 1 4 2 1 2 3 1 3 3 2 4 3]

rnd = np.random.default_rng()
a = rnd.integers(1, 10, (5, 3))
print(a)  # [[9 3 9] [1 6 9] [1 5 2] [1 4 5] [2 3 9]]
print(a.T)  # [[4 9 4 4 2] [4 5 3 1 8] [6 4 5 8 8]]
print(a.transpose())  # [[2 9 6 1 2] [7 2 9 5 4] [4 9 8 8 5]]
print(np.flip(a, axis=1))  # [[1 7 6] [6 3 2] [7 8 2] [6 6 5] [3 9 2]]
print(np.flip(a[2]))  # [4 8 9]
print(a.flatten())  # [5 2 1 6 6 4 4 9 4 7 4 4 2 1 2]

rnd = np.random.default_rng()
a = rnd.integers(1, 10, 5)
print(a)  # [4 7 1 7 9]
a.sort()
print(a)  # [1 4 7 7 9]
print(np.flip(a))  # [9 7 7 4 1]
