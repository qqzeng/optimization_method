#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/4
=====

@desc: 使用黄金分割法对单谷函数求解极值
        1. 黄金分割法属于区间收缩法
        2. 首先找出包含极小点的搜索区间，然后按照黄金分割点通过对函数值的比较不断缩小搜索区间。在这个过程中必须要保证极小点始终在搜索区间内。
        当区间长度足够小时，就可以粗略地认为极小点的近似值为区间中点所对应的函数值。
        3. 黄金分割法适用于单谷函数，即在某一区间内只存在唯一极小点的函数。
        4. 需要注意的是：
            4.1. 理论上，当黄金分割比取0.618时，试点最大个数为10，即不超过10个试点才有意义，即最多9次迭代，所以其最小精度为 0.013
            4.2. 所以，如果我们需要提高精度，可以取黄金分割为更精确的值，比如 0.6180339
            4.3. 默认的，是求极小值点，所以对于测试函数 goal_function，其只有极大值点小，因此需要对内部的两个 while 循环条件互换
"""

import numpy as np
import matplotlib.pyplot as plt

"""
测试函数 goal_function 图解
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
    plt.title("segmented function example")
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
f: 目标函数
[a_, b_]： 包含极小值点的区间
"""
def golden_section(f, a_, b_):
    golden_section_p1 = 0.618 # 黄金分割比
    theta = 0.15
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
对 黄金分割法进行测试
"""
def test_golden_section():
    f = lambda x : x ** 2 - 2 * x - 4
    golden_section(f, 0, 3)
    # golden_section(goal_function, 0, 3)


if __name__ == '__main__':
    # test_figure()
    test_golden_section()
