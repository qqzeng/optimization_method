#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/14
=====

@desc: 外推内插+牛顿法
       需要注意的是：
            1. 在实现牛顿法时，使用了 sympy 库，本文件中的所有函数的入参 f，都表示是一个 expr，不是一个 lambda 对象
            2. 可以使用 f.subs(x, x.val) 来将 x 的值 x.val 代入到表达式 f 中进行计算
"""
from sympy.abc import x
from sympy import *

"""
返回指定数组x中具有较小函数值f(x[index])的索引index
"""
def get_min(f_, x_, x1_, x2_):
    if f_.subs(x, x_[x1_]) < f_.subs(x, x_[x2_]):
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
    x_arr = list(range(5))
    x_arr[1] = x1
    while i < max_iter:
        x_arr[2] = x_arr[1] + h0
        #  go left
        if f.subs(x, x_arr[2]) < f.subs(x, x_arr[1]):
            i += 1
            h0 *= 2
            x_arr[3] = x_arr[2] + h0
            print("process#{0}: h{1}={2} x{3}={4}\n".format(i, i, h0, i, x_arr[2]))
            while f.subs(x, x_arr[3]) < f.subs(x, x_arr[2]):
                i += 1
                h0 *= 2
                x_arr[3] = x_arr[2] + h0
                print("process#{0}: h{1}={2} x{3}={4}\n".format(i, i, h0, i, x_arr[2]))
            x_arr[2] = x_arr[3] - h0
            x_arr[1] = x_arr[2] - h0 / 2
            x_arr[4] = (x_arr[2] + x_arr[3]) / 2
            # reorder by array index
            t = x_arr[3]
            x_arr[3] = x_arr[4]
            x_arr[4] = t
            print("===============end====================\nparam: x1={0} x2{1} x3={2} x4={3} h{4}={5} times={6}"
                  .format(x_arr[1], x_arr[2], x_arr[3], x_arr[4], i, h0, h0))
            x_min_index = get_min(f, x_arr, get_min(f, x_arr, get_min(f, x_arr, 1, 2), 3), 4)
            print("result: a={0} b={1}\n".format(x_arr[x_min_index - 1], x_arr[x_min_index + 1]))
            return [x_arr[x_min_index - 1], x_arr[x_min_index + 1]]
        # go right
        else:
            i += 1
            h0 *= 2
            x_arr[3] = x_arr[2] - h0
            print("process#{0}: h{1}={2} x{3}={4}\n".format(i, i, h0, i, x_arr[2]))
            while f.subs(x, x_arr[3]) < f.subs(x, x_arr[2]):
                i += 1
                h0 *= 2
                x_arr[3] = x_arr[2] - h0
                print("process#{0}: h{1}={2} x{3}={4}\n".format(i, i, h0, i, x_arr[2]))
            x_arr[2] = x_arr[3] + h0
            x_arr[1] = x_arr[2] + h0 / 2
            x_arr[4] = (x_arr[2] + x_arr[3]) / 2
            # reorder by array index
            t = x_arr[3]
            x_arr[3] = x_arr[4]
            x_arr[4] = t
            print("===============end====================\nparam: x1={0} x2={1} x3={2} x4={3} h{4}={5} times={6}"
                  .format(x_arr[1], x_arr[2], x_arr[3], x_arr[4], i, h0, h0))
            x_min_index = get_min(f, x_arr, get_min(f, x_arr, get_min(f, x_arr, 1, 2), 3), 4)
            print("result: a={0} b={1}\n".format(x_arr[x_min_index - 1], x_arr[x_min_index + 1]))
            return [x_arr[x_min_index - 1], x_arr[x_min_index + 1]]


"""
newton 法求解函数极值
fun_: 目标函数
s：默认起始点
max_iter: 默认的最大迭代的次数
theta: 迭代终止条件（也可选取其它条件作为终止条件）
"""
def newton_tangent(fun_, s = 1, max_iter = 100, prt_step = False, theta = 0.01):
    fun = fun_.diff()
    for i in range(max_iter):
        s = s - fun.subs(x,s)/fun.diff().subs(x,s)
        if prt_step:
            print("after {0} iteration, the solution is updated to {1}".format(i+1,s))
        if abs(float(fun.subs(x, s))) <= theta:
            return s

"""
牛顿法求解极小值
（由外推内插来确定极小值所在区间，然后利用牛顿法来求解指定区间的极小值点）
"""
def newton_tangent_method(f, x1 = 0, h0 = 1, times = 2, max_iter = 100):
    [a, b] = extrapolation_interpolation_method(f, x1, h0, times, max_iter)
    print("[{0}, {1}]\n".format(a, b))
    _x = newton_tangent(f, s=2, max_iter=4, prt_step=True)
    return  float(_x), float(f.subs(x, _x))

"""
测试 牛顿法求解极小值
"""
def test_newton_tangent_method():
    _x1 = 0; _h0 = 1; _times = 2;
    _f = -x * x * x + 100 * (x - 1) * (x - 1) - 10 * x + 1
    _x, _y = newton_tangent_method(_f, _x1, _h0, _times)
    print(float(_x), float(_f.subs(x, _x)))


if __name__ == '__main__':
    test_newton_tangent_method()
    # subplots()