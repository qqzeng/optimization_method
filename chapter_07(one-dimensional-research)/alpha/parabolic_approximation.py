#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/4
=====

@desc: 使用抛物线逼近法来求解函数的极值
        1. 抛物线逼近法又称为三点二次插值法，其基本思想是在极小点附近用二次三项式 φ(x) 来逼近目标函数 f(x)
        2. 三点 x1 < x2 < x3 必须满足 f(x1) > f(x2) and f(x3) > f(x2) 即形成 "高-低-高"
        3. 实质上，抛物线逼近法就是过三点 (x1, f(x1)), (x2, f(x2)), (x3, f(x3)) 作抛物线 φ(x)，然后求解
        φ(x) 的极小值点作为 f(x) 的近似（达到一定的精度要求）极小值点。
        4. 当求出近似函数 φ(x) 的极小值点后，需要重新构造出新的用于下一轮构造三个点的值。即从 x1, x2, x3, x*
        中选取三个点。但这首先必须选出最小值的点，这实际上只需要比较 f(x2)和f(x*)的关系及 x2 和 x* 的关系即可。
        5. 在本算法实现中，使用到了 scipy.linalg 来求解线性方程组的解。
"""
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
    from sympy import Matrix, symarray, solve
    a = Matrix([[2, 3, 1], [4, 2, 3], [7, 1, -1]])
    b = Matrix([[4], [17], [1]])
    x = symarray('x', 3).reshape(3, 1)
    print(solve(a * x - b))

"""
抛物线逼近法
"""
def parabolic_approximation(f, x1, x2, x3, max_iter = 100, theta = 0.01):
    print("===============parabolic approximation begin=================\nparam: x1={0} x1={1} x1={2}".format(x1, x2, x3))
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
    print("===============parabolic approximation  end=================\nx1={0} x1={1} x1={2}".format(x1, x2, x3))
    return x2, f(x2)


"""
测试抛物线逼近法
"""
def test_parabolic_approximation_1():
    f = lambda x : np.sin(x)
    x_, y_ = parabolic_approximation(f, 4, 5, 6, max_iter=100, theta=0.001)
    print("result: x*={0} y*={1}".format(x_, y_))


if __name__ == '__main__':
    # test_subplots()
    test_parabolic_approximation_1()
    # linear_equation_solution_numpy()