#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/14
=====

@desc: 外推内插+黄金分割
"""

import numpy as np
import matplotlib.pyplot as plt

"""
函数图形化
"""
def subplots():
    x = np.linspace(-10, 10, 1000)
    y = -x*x*x + 100 * (x - 1)*(x - 1) - 10*x + 1
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(' figure')
    plt.show()

"""
目标函数
"""
def goal_function(x):
    if x <= 2:
        return x / 2
    else:
        return -x + 3


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
    print("===============begin=================\nparam: x1={0} h0={1} times={2}".format(x1, h0, times))
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
            print("===============end====================\nparam: x1={0} x2{1} x3={2} x4={3} h{4}={5} times={6}"
                  .format(x[1], x[2], x[3], x[4], i, h0, h0))
            x_min_index = get_min(f, x, get_min(f, x, get_min(f, x, 1, 2), 3), 4)
            print("result: a={0} b={1}\n".format(x[x_min_index - 1], x[x_min_index + 1]))
            return [x[x_min_index - 1], x[x_min_index + 1]]
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
            print("===============end====================\nparam: x1={0} x2={1} x3={2} x4={3} h{4}={5} times={6}"
                  .format(x[1], x[2], x[3], x[4], i, h0, h0))
            x_min_index = get_min(get_min(get_min(f, x, 1, 2), 3), 4)
            print("result: a={0} b={1}\n".format(x[x_min_index - 1], x[x_min_index + 1]))
            return [x[x_min_index - 1], x[x_min_index + 1]]

"""
黄金分割法求解极小值
goal_function: 目标函数(lambda 表达式)
[a_, b_]: 由外推内插求解得来的包含极小值的区间
"""
def golden_section(f, a_, b_):
    golden_section_p1 = 0.6180339
    theta = 0.015
    a = a_; b = b_
    x1 = a + golden_section_p1 * (b - a)
    x2 = a + (1 - golden_section_p1) * (b - a)
    y1 = f(x1)
    y2 = f(x2)
    i = 0; j = 0
    print("===============begin=================\nparam: a={0} b={1}".format(a, b))
    while (b - a) / (b_ - a_) >= theta:
        while y1 < y2 and (b - a) / (b_ - a_) >= theta:
            a = x2
            x2 = x1
            x1 = a + golden_section_p1 * (b - a)
            y1 = f(x1)
            y2 = f(x2)
            i += 1
            print("a={0} b={1}\n".format(a, b))
        while y1 >= y2 and (b - a) / (b_ - a_) >= theta:
            b = x1
            x1 = x2
            x2 = a + (1 - golden_section_p1) * (b - a)
            y1 = f(x1)
            y2 = f(x2)
            j += 1
            print("a: ", a, "b: ", b)
    print("================================\nresult: left={0} right={1}\n".format(j, i))
    print(a, b, (a + b) / 2, f((a + b) / 2))
    return a, b,(a + b) / 2,  f((a + b) / 2)

"""
黄金分割法求解极小值
（由外推内插来确定极小值所在区间，然后利用黄金分割来求解指定区间的极小值点）
"""
def golden_section_method(f, x1 = 0, h0 = 1, times = 2, max_iter = 100):
    [a, b] = extrapolation_interpolation_method(f, x1, h0, times, max_iter)
    print("[{0}, {1}]\n".format(a, b))
    a, b, median, y = golden_section(f, a, b)
    return median, y

"""
测试 黄金分割法求解极小值
"""
def test_golden_section_method():
    _x1 = 0; _h0 = 1; _times = 2;
    # _f = lambda x: x * x * x - 100 * x + 1
    _f = lambda x : -x*x*x + 100 * (x - 1)*(x - 1) - 10*x + 1
    # median=1.0688837566802603 y=-10.435553410700193
    _median, _y = golden_section_method(_f, _x1, _h0, _times)
    print("median={0} y={1}\n".format(_median, _y))


if __name__ == '__main__':
    test_golden_section_method()
    # subplots()