#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/14
=====

@desc: 1. 书本第7章相关算法的简单实现。
       2. 其中 beta 目录下的算法是人为确定包含极小值点的搜索区间。
           而 beta 目录下为其对应的使用 外推内插法 来自动确定搜索区间的简单实现。
       3. 算法书本算法描述的python简单实现，仅为对算法理解的更为深刻，不能作为实际使用，没有经过效率、可靠性等方面的详细测试。
       =======================
       4. 求解非线性规划问题的下降迭代算法包含了两个最关键的步骤：
            4.1. 构造出搜索方向dk
            4.2. 求出步长λk
       5. 而求解步长λk，即求解λ的一元函数，我们称这样的极小点的问题为一维搜索。其主要方法有两类：
            5.1. 区间收缩（黄金分割）
            5.2. 函数逼近法（牛顿法和抛物线逼近法）
       6. 一维搜索法不仅可以求最优步长上，也是求单变量函数极小点的一种方法，因此它也被称为是单变量函数寻优法。
"""