#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/14
=====

@desc: 利用变量轮换法来求解无约束的多元函数的极值问题
"""

import numpy as np

"""
目标函数
"""
def goal_function(x):
    pass

"""
使用变量轮换法来求解无约束的多元函数求解极值
"""
def variable_rotation(f, x1, theta = 0.01, max_iter = 100):
    dimension = x1.shap[0]
    np.diag(np.bincount(np.arange(dimension)))
    i = 0
    x = list(range(dimension + 1))
    x[1] = x1
    while i < max_iter:
        for j in range(dimension):
            pass

"""
测试 使用变量轮换法来求解无约束的多元函数求解极值
"""
def test_variable_rotation():
    _f = lambda x1, x2, x3 : 3 * x1 * x1 + 2 * x2 * x2 + x3 * x3
    _x1 = np.array([[1], [2], [3]])
    _theta = 0.01
    variable_rotation(_f, _x1, _theta)

"""
测试
"""
def test():
    for j in range(10):
        print(j)

if __name__ == '__main__':
    # test_figure()
    # test_variable_rotation()
    test()