"""
    Author : YangBo
    Time : 2018-09-24 16:45
    function:正则化.
"""
# coding=utf-8
# 0导入模板, 生成模拟数据集.
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
BATCH_SIZE = 30
seed = 2
# 基于seed产生随机数.
rmd = np.random.RandomState(seed)
"""
    随机数返回00行2列的矩阵中取出一行
    判断如果两个坐标的平方和小于2,给Y赋值1,其余赋值0.
"""
X = rmd.random(300, 2)
# 作为输入数据集的标签(正确答案).
Y = [int(x0*x0 + x1*x1 < 2) for (x0, x1) in X]
# 遍历Y中的每个元素,1赋值''