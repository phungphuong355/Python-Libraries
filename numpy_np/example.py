#! /usr/bin/env python
import numpy as np


def operate_Matrix(arr1: np.ndarray, arr2: np.ndarray, sign: str):
    """Can Input 4 sign: +, -, *, /"""
    ma, na = arr1.shape
    mb, nb = arr2.shape
    if sign == "+":
        return arr1 + arr2
    elif sign == "-":
        return arr1 - arr2
    elif sign == "*":
        if na == mb:
            return arr1 @ arr2
        else:
            return None
    elif sign == "/":
        if na == np.linalg.inv(arr2).shape[0]:
            return arr1 @ np.linalg.inv(arr2)
        else:
            return None
    else:
        return "Repeat the sign"


# help(operate_Matrix)
a = np.array([[1, 3, 6], [4, 2, 3], [7, 5, 2]])
b = np.array([[4, 5, 6], [4, 2, 9], [2, 3, 0]])
print("a {} b =\n{}".format("+", operate_Matrix(a, b, "+")))
print("a {} b =\n{}".format("-", operate_Matrix(a, b, "-")))
print("a {} b =\n{}".format("*", operate_Matrix(a, b, "*")))
print("a {} b =\n{}".format("/", operate_Matrix(a, b, "/")))
