"""
    Author : YangBo
    Time : 2018-09-11 10:57
    function:装饰器--源代码对修改封闭，对扩展开放.
    解析：通过对闭包的利用，实现一个函数功能的扩展.
"""
import time


def show_time(f):              # 装饰器

    def inner():
        start = time.time()  # 开始时间.
        f()                  # 调用函数.
        end = time.time()    # 结束时间.
        print('spend {}'.format(end - start - 2))
    return inner


@show_time                  # foo = show_time(foo)           # show_time()返回inner然后将其赋值给变量foo.
def foo():
    print('foo...')
    time.sleep(2)


foo()


@show_time                # bar = show_time(bar)  就等于此句.
def bar():
    print('我是bar函数，我没有啥特殊的功能')
    time.sleep(2)


bar()
