#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
=====
@author: qqzeng
@email: qtozeng@gmail.com
@date: 2017/11/14
=====

@desc: 1. 书本第8章相关算法的简单实现。
       2. 其中 beta 目录下的算法是人为确定包含极小值点的搜索区间。
           而 beta 目录下为其对应的使用 外推内插法 来自动确定搜索区间的简单实现。
       3. 算法书本算法描述的python简单实现，仅为对算法理解的更为深刻，不能作为实际使用，没有经过效率、可靠性等方面的详细测试。
       ===========================================================================================================
       4. 无约束问题的最优化方法大致分为两类：
            一类在计算过程中只用到目标函数值，而无需计算导数，通常称为直接搜索法。
            另一类在计算过程中需要计算目标函数的导数，称为解析法或使用导数的最优化方法。
       5. 各种不同的约束问题的最优化方法的根本不同之处在于迭代过程中选择的搜索方向的不同。
       6. 变量轮换法，可变单纯形法和模式搜索法等属于直接搜索法。而最速下降法，牛顿法，共轭梯度法和拟牛顿法等属于解析法。
"""