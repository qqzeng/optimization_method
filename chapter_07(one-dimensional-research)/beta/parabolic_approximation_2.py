#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/14
=====

@desc: 外推内插+抛物线逼近
        需要注意的是：
            1. 由于抛物线逼近是三个 "高-低-高" 的点，所以需要 外推内插法 提供三个点。（这与先前的两种综合算法不同）
"""

from sympy import *
import numpy as np

"""
返回指定数组x中具有较小函数值f(x[index])的索引index
"""
def get_min(f_, x_, x1_, x2_):
    if f_(x_[x1_]) < f_(x_[x2_]):
        return x1_
    else:
        return x2_

"""
用 外推内插法 寻找包含极小值的区间
f: 目标函数
x1: 初始点
h0: 初始步长
times: 步长加倍数
"""
def extrapolation_interpolation_method(f, x1 = 0, h0 = 1, times = 2, max_iter = 100):
    print("===============extrapolation interpolation begin=================\nparam: x1={0} h0={1} times={2}".format(x1, h0, times))
    i = 0
    x = list(range(5))
    x[1] = x1
    while i < max_iter:
        x[2] = x[1] + h0
        #  go left
        if f(x[2]) < f(x[1]):
            i += 1
            h0 *= 2
            x[3] = x[2] + h0
            print("process#{0}: h{1}={2} x{3}={4}\n".format(i, i, h0, i, x[2]))
            while f(x[3]) < f(x[2]):
                i += 1
                h0 *= 2
                x[3] = x[2] + h0
                print("process#{0}: h{1}={2} x{3}={4}\n".format(i, i, h0, i, x[2]))
            x[2] = x[3] - h0
            x[1] = x[2] - h0 / 2
            x[4] = (x[2] + x[3]) / 2
            # reorder by array index
            t = x[3]
            x[3] = x[4]
            x[4] = t
            print("===============extrapolation interpolation end====================\nparam: x1={0} x2{1} x3={2} x4={3} h{4}={5} times={6}"
                  .format(x[1], x[2], x[3], x[4], i, h0, h0))
            x_min_index = get_min(f, x, get_min(f, x, get_min(f, x, 1, 2), 3), 4)
            print("result: a={0} b={1} c={2}\n".format(x[x_min_index - 1], x[x_min_index], x[x_min_index + 1]))
            return [x[x_min_index - 1], x[x_min_index], x[x_min_index + 1]]
        # go right
        else:
            i += 1
            h0 *= 2
            x[3] = x[2] - h0
            print("process#{0}: h{1}={2} x{3}={4}\n".format(i, i, h0, i, x[2]))
            while f(x[3]) < f(x[2]):
                i += 1
                h0 *= 2
                x[3] = x[2] - h0
                print("process#{0}: h{1}={2} x{3}={4}\n".format(i, i, h0, i, x[2]))
            x[2] = x[3] + h0
            x[1] = x[2] + h0 / 2
            x[4] = (x[2] + x[3]) / 2
            # reorder by array index
            t = x[3]
            x[3] = x[4]
            x[4] = t
            print("===============extrapolation interpolation end====================\nparam: x1={0} x2={1} x3={2} x4={3} h{4}={5} times={6}"
                  .format(x[1], x[2], x[3], x[4], i, h0, h0))
            x_min_index = get_min(f, x, get_min(f, x, get_min(f, x, 1, 2), 3), 4)
            print("result: a={0} b={1} c={2}\n".format(x[x_min_index - 1], x[x_min_index], x[x_min_index + 1]))
            return [x[x_min_index - 1], x[x_min_index], x[x_min_index + 1]]

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
    print("===============parabolic approximation end=================\nx1={0} x1={1} x1={2}".format(x1, x2, x3))
    return x2, f(x2)


"""
抛物线逼近法求解极小值
（由外推内插来确定极小值所在区间，然后利用抛物线逼近法来求解指定区间的极小值点）
"""
def parabolic_approximation_method(f, x1 = 0, h0 = 1, times = 2, max_iter = 100):
    [a, b, c] = extrapolation_interpolation_method(f, x1, h0, times, max_iter)
    print("[{0}, {1}, {2}]\n".format(a, b, c))
    x_, y_ = parabolic_approximation(f, a, b, c, max_iter=100, theta=0.001)
    return x_, y_

"""
测试抛物线逼近法
"""
def test_parabolic_approximation_method():
    _f = lambda x : np.sin(x)
    _x1 = 3; _h0 = 1; _times = 2;
    x_, y_ = parabolic_approximation_method(_f, _x1, _h0, _times)
    print("result: x*={0} y*={1}".format(x_, y_))


if __name__ == '__main__':
    test_parabolic_approximation_method()
