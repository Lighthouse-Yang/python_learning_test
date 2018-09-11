"""
    Author : YangBo
    Time : 2018-09-11 9:59
    function:装饰器前提知识.
    1.作用域:
    2.高阶函数:(1.函数名可以作为返回值.  2.函数名可以作为参数输入.)
    3.闭包:7
"""


def outer():
    x = 10      # 条件1-inner是内部函数.

    def inner():   # 条件1-inner是内部函数.
        print(x)   # 条件2-外部环境的一个变量.

    return inner   # 结论：内部函数inner就是一个闭包.
# inner() 局部变量，全局无法调用.


f = outer()
f()
# 在outer的外层执行inner函数时依然可以执行，所以内部函数inner是闭包.
# 闭包=函数块+定义函数时的环境.
