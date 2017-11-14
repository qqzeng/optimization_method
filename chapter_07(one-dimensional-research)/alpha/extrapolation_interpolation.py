#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/14
=====

@desc: 外推内插法来寻找给定函数的一个包含极小值的区间
        1. 黄金分割法和抛物线逼近法等一维搜索法都要事先给定一个包含极小点的初始搜索区间，则外推内插法便可用来解决此问题。
        2. 其又称为区间试探法，即从一点出发，按一定步长，试图确定出函数值呈现 "高-低-高"的三点。
        它会首先从一个方向去找，若不成功，则退回来，再沿反方向寻找，若方向正确，则加大步长进行探索，
        直至 xk 点的函数值刚刚变为增加为止。这样便使得最终找到的三点满足：
        x1 < x2 < x3 and f(x1) > f(x2) f(x3) > f(x2)
        3. 需要注意的是：
            3.1 在外推内插法中，若能估计最优解的大体位置，初始点 x1 要尽量取接近函数最优解的值。
            3.2 步长为h0，倍数一般取为两倍
"""
import numpy as np
import matplotlib.pyplot as plt

"""
函数图形化
"""
def test_subplots():
    x = np.linspace(-10, 10, 1000)
    y = x*x*x - 2 * x + 1
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(' figure')
    plt.show()

"""
返回指定数组x中具有较小函数值f(x[index])的索引index
"""
def get_min(f_, x_, x1_, x2_):
    if f_(x_[x1_]) < f_(x_[x2_]):
        return x1_
    else:
        return x2_

"""
用外推内插法寻找包含极小值的区间
f: 目标函数
x1: 初始点
h0: 初始步长
times: 步长加倍数
"""
def extrapolation_interpolation_method(f, x1 = 0, h0 = 1, times = 2, max_iter = 100):
    print("===============begain=================\nparam: x1={0} h0={1} times={2}".format(x1, h0, times))
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
用 外推内插法 寻找包含极小值的区间的测试
"""
def test_extrapolation_interpolation_method():
    _x1 = 0; _h0 = 1; _times = 2; _f = lambda x : x*x*x - 2 * x + 1
    [a, b] = extrapolation_interpolation_method(_f, _x1, _h0, _times)
    print("[{0}, {1}]\n".format(a, b))


if __name__ == '__main__':
    # test_subplots()
    test_extrapolation_interpolation_method()
