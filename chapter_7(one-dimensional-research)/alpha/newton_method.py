#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/4
=====

@desc: 用牛顿法来求解函数的极值
"""

from sympy.abc import x
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# init_session(use_latex=True)
# init_printing(use_latex=True)

# 画图的函数
def makeplot(f,l,d):
    plt.plot(d,[f.evalf(subs={x:xval}) for xval in d],'b',
             d,[l.evalf(subs={x:xval}) for xval in d],'r')

def test_sympy():
    # 函数
    f = x ** 3 - 2 * x - 6
    # 在x=6处正切于函数的切线
    line = 106 * x - 438

    d1 = np.linspace(2, 10, 1000)
    d2 = np.linspace(4, 8, 1000)
    d3 = np.linspace(5, 7, 1000)
    d4 = np.linspace(5.8, 6.2, 100)
    domains = [d1, d2, d3, d4]

    for i in range(len(domains)):
        # 绘制包含多个子图的图表
        plt.subplot(2, 2, i+1)
        makeplot(f,line,domains[i])
    plt.show()

"""
 利用定义求解函数的某点的导数值
"""
def test_derivative():
    f = lambda x: x ** 3 - 2 * x - 6

    # 我们设定参数h的默认值，如果调用函数时没有指明参数h的值，便会使用默认值
    def derivative(f, h=0.00001):
        return lambda x: float(f(x + h) - f(x)) / h

    fprime = derivative(f)
    print(fprime(6))
    # result is : 106.000179994

"""
利用 sympy 求解函数的导数，及某点的导数值
"""
def test_derivative_sympy():
    f = x**3-2*x-6
    print(f.diff())
    # result is :3*x**2-2
    print(f.diff().evalf(subs={x:6}))

"""
newton 法求解函数极值图解
"""
def test_newton_figure():
    f = lambda x: x ** 2 - 2 * x - 4
    l1 = lambda x: 2 * x - 8
    l2 = lambda x: 6 * x - 20

    x = np.linspace(0, 5, 100)

    plt.plot(x, f(x), 'black')
    plt.plot(x[30:80], l1(x[30:80]), 'blue', linestyle='--')
    plt.plot(x[66:], l2(x[66:]), 'blue', linestyle='--')

    l = plt.axhline(y=0, xmin=0, xmax=1, color='black')
    l = plt.axvline(x=2, ymin=2.0 / 18, ymax=6.0 / 18, linestyle='--')
    l = plt.axvline(x=4, ymin=6.0 / 18, ymax=10.0 / 18, linestyle='--')

    plt.text(1.9, 0.5, r"$x_0$", fontsize=18)
    plt.text(3.9, -1.5, r"$x_1$", fontsize=18)
    plt.text(3.1, 1.3, r"$x_2$", fontsize=18)

    plt.plot(2, 0, marker='o', color='r')
    plt.plot(2, -4, marker='o', color='r')
    plt.plot(4, 0, marker='o', color='r')
    plt.plot(4, 4, marker='o', color='r')
    plt.plot(10.0 / 3, 0, marker='o', color='r')

    plt.show()

"""
newton 法求解函数极值
"""
def newton_tangent(fun, s = 1, max_iter = 100, prt_step = False, theta = 0.01):
    for i in range(max_iter):
        s = s - fun.subs(x,s)/fun.diff().subs(x,s)
        if prt_step:
            print("After {0} iteration, the solution is updated to {1}".format(i+1,s))
        if abs(float(fun.subs(x, s))) <= theta:
            return s

"""
对new_ton 法求解函数极值的方法进行测试
"""
def test_newton_1():
    f = x ** 2 - 2 * x - 4
    _x = newton_tangent(f, s=2, max_iter=4, prt_step=True)
    print(float(_x), float(f.subs(x, _x)))

"""
对new_ton 法求解函数极值的方法进行测试
"""
def test_newton_2():
    f = integrate(atan(x), (x, 0, x))
    _x = newton_tangent(f.diff(), s=1, max_iter=4, prt_step=True, theta = 0.01)
    print(float(_x), float(f.subs(x, _x)))


if __name__ == '__main__':
    test_newton_1()
