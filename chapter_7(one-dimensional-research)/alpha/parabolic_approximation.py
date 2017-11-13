#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/4
=====

@desc: 使用抛物线逼近法来求解函数的极值
"""
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

"""
函数图形化
"""
def test_subplots():
    x = np.linspace(2, 7, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('sin figure')
    plt.show()

"""
numpy 求解线性方程组
2x+3y+z=4
4x+2y+3z =17
7x+y-z=1
"""
def linear_equation_solution_numpy():
    from scipy.linalg import solve
    a = np.array([[2, 3, 1], [4, 2, 3], [7, 1, -1]])
    b = np.array([[4], [17], [1]])
    x = solve(a, b)
    print(x)

"""
sympy 求解线性方程组
2x+3y+z=4
4x+2y+3z =17
7x+y-z=1
"""
def linear_equation_solution():
    a = Matrix([[2, 3, 1], [4, 2, 3], [7, 1, -1]])
    b = Matrix([[4], [17], [1]])
    x = symarray('x', 3).reshape(3, 1)
    print(solve(a * x - b))

"""
抛物线逼近法
"""
def parabolic_approximation(f, x1, x2, x3, max_iter = 100, theta = 0.01):
    print("===============begain=================\nparam: x1={0} x1={1} x1={2}".format(x1, x2, x3))
    i = 0
    while (i == 0) or (i < max_iter and abs(x_star - x2) > theta):
        from scipy.linalg import solve
        A = np.array([[x1 * x1, x1, 1], [x2 * x2, x2, 1], [x3 * x3, x3, 1]])
        B = np.array([[f(x1)], [f(x2)], [f(x3)]])
        [[a], [b], [c]] = solve(A, B)
        x_star = -b / (2 * a)
        if f(x_star) < f(x2):
            if x_star < x2:
                x3 = x2
                x2 = x_star
            else:
                x1 = x2
                x2 = x_star
        else:
            if x_star < x2:
                x1 = x_star
            else:
                x3 = x_star
        i += 1
        print("process#{0}: x1={0} x1={1} x1={2}".format(i, x1, x2, x3))
    print("===============end=================\nx1={0} x1={1} x1={2}".format(x1, x2, x3))
    return x2, f(x2)

"""
目标函数
"""
def goal_fun(x):
    return np.sin(x)

"""
测试抛物线逼近法
"""
def test_parabolic_approximation_1():
    f = lambda x : sin(x)
    x = np.linspace(2, 7, 100)
    x_, y_ = parabolic_approximation(goal_fun, 3, 5, 6, max_iter=100, theta=0.001)
    print("result: x*={0} y*={1}".format(x_, y_))


if __name__ == '__main__':
    # test_subplots()
    test_parabolic_approximation_1()
    # linear_equation_solution_numpy()