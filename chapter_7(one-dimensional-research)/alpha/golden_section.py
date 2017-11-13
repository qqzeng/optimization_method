#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/4
=====

@desc: 使用黄金分割法对单谷函数求解极值
"""

import numpy as np
import matplotlib.pyplot as plt

"""
测试函数作图
"""
def test_figure():
    x = np.arange(0, 3, 0.01)
    y = []
    for i in x:
        if  i <= 2:
            y.append(i / 2)
        else:
            y.append(-i + 3)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("segmented funciton example")
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
黄金分割法求解极小值
"""
def golden_section():
    theta = 0.15
    a = 0; b = 3
    a_ = 0; b_ = 3
    x1 = a + 0.618 * (b - a)
    x2 = a + 0.382 * (b - a)
    y1 = goal_function(x1)
    y2 = goal_function(x2)
    i = 0; j = 0
    print("===============begain=================\nparam: a={0} b={1}".format(a, b))
    while (b - a) / (b_ - a_) >= theta:
        while y1 > y2 and (b - a) / (b_ - a_) >= theta:
            a = x2
            x2 = x1
            x1 = a + 0.618 * (b - a)
            y1 = goal_function(x1)
            y2 = goal_function(x2)
            i += 1
            print("a={0} b={1}\n".format(a, b))
        while y1 <= y2 and (b - a) / (b_ - a_) >= theta:
            b = x1
            x1 = x2
            x2 = a + 0.382 * (b - a)
            y1 = goal_function(x1)
            y2 = goal_function(x2)
            j += 1
            print("a: ", a, "b: ", b)
    print("================================\nresult: left={0} right={1}\n".format(j, i))
    print(a, b, (a + b) / 2, goal_function((a + b) / 2))
    return a, b,(a + b) / 2,  goal_function((a + b) / 2)


if __name__ == '__main__':
    # test_figure()
    _a, _b, _median, _y = golden_section()
