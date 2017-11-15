#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/14
=====

@desc: 利用变量轮换法来求解无约束的多元函数的极值问题
       使用了 sympy 库，本文件中函数的入参 f，表示是一个 expr，不是一个 lambda 对象
"""

import numpy as np
import sympy as sp
# 导入 chapter_7 的相关算法模块
import sys
sys.path.append("..\\chapter_07(one-dimensional-research)")
import beta.newton_method_2 as newton_method


"""
目标函数
"""
def goal_function(x):
    pass

"""
借助 sympy 模块来计算带有未知变量的表达式，且利用了矩阵操作来转换表达式
"""
def mat_operation_fun(x_arr):
    A = sp.Matrix([[x_arr[0, 0] * x_arr[0, 0]], [x_arr[0, 1] * x_arr[0, 1]], [x_arr[0, 2] * x_arr[0, 2]]])
    coe = sp.Matrix([[3, 2, 1]])
    _f_mat = coe * A
    _f = _f_mat[0, 0]
    return _f


"""
变量轮换法来求解无约束的多元函数求解极值
=====================================
f: 目标函数（在这里需要是 sympy 中 Expr 对象）
x1: 初始点（一个向量，一般来说，初始化为列向量更符合习惯。但这并不影响最终的结果）
theta: 迭代终止条件，即两次迭代后两个未知变量的差的二范数
max_iter: 理论上，（人为）设定的一个最大的迭代次数
"""
def variable_rotation(f, x1, theta = 0.01, max_iter = 100):
    x = sp.Symbol('x')
    dimension = x1.shape[0]
    E = np.diag(np.bincount(np.arange(dimension)))
    i = 0
    x_arr = list(range(dimension + 2))
    f_arr = list(range(dimension + 2))
    x_arr[1] = x1.T
    f_arr[1] = f
    print("=====================variable rotation begin========================")
    print("param: x1={0} f={1}".format(x1, f))
    while i < max_iter:
        if i != 0:
            x_arr[1] = x_arr[dimension + 1]
        for j in range(dimension):
            x_arr[2 + j] = x_arr[1 + j] + (E[:, j]) * x
            f_arr[2 + j] = mat_operation_fun(x_arr[2 + j])
            print("process#{0} x_arr[{1}]={2} f_arr[{3}]={4}".format(i+1, 2+j, x_arr[2+j], 2+j, f_arr[2+j]))
            _x1 = 0;_h0 = 1;_times = 2
            x_star, y_star = newton_method.newton_tangent_method(f_arr[2 + j], _x1, _h0, _times)
            print("process#{0} x_star={0} y_star={1}".format(x_star, y_star))
            x_arr[2 + j] = x_arr[1 + j] + (E[:, j]) * x_star
            print("x_arr[{0}]={1}".format(2+j, x_arr[2 + j]))
        _2_norm_accuracy = np.linalg.norm(x_arr[dimension + 1] - x_arr[1],ord = 2)
        if _2_norm_accuracy < theta:
            print("=====================variable rotation end========================")
            print("result: after {0} iteration, _x_star={1} _y_star={2}".format(i + 1, x_arr[dimension + 1], y_star))
            return i + 1, x_arr[dimension + 1], y_star
        else:
            print("process#{0} the accuracy is {0} >= {1}".format(_2_norm_accuracy, theta))
            print("-----------------------------------------------------------------------------")
            i += 1

"""
测试 变量轮换法来求解无约束的多元函数求解极值
"""
def test_variable_rotation():
    # _f = lambda x1, x2, x3 : 3 * x1 * x1 + 2 * x2 * x2 + x3 * x3
    x1, x2, x3 = sp.symbols('x1,x2,x3')
    init_var_x = np.array([[x1, x2, x3]])
    _f = mat_operation_fun(init_var_x)
    _x1 = np.array([[1], [2], [3]])
    _theta = 0.01
    variable_rotation(_f, _x1, _theta)


if __name__ == '__main__':
    # test_figure()
    test_variable_rotation()
