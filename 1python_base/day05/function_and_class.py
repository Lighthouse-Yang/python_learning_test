"""
    Author : YangBo
    Time : 2018-09-17 12:31
    function:函数、类(父类、子类)、继承及使用
"""


class Animals():
    def breathe(self):
        print('呼吸')

    def move(self):
        print('移动')

    def eat(self):
        print('吃东西')


class Mammals(Animals):
    def breastfeed(self):
        print('喂奶')


class Cats(Mammals):
    def __init__(self, spots):
        self.spots = spots

    def catch_mouse(self):
        print('捉老鼠')

    def left_foot_forward(self):
        print('左脚往前')

    def left_foot_backward(self):
        print('左脚往后')

    def dance(self):
        print('跳舞函数调用')
        self.left_foot_forward()
        self.left_foot_backward()
        self.left_foot_forward()
        self.left_foot_backward()


kitty = Cats(10)             # 创建对象
print(kitty.spots)           # 打印调用Cats类内的变量spots.
kitty.catch_mouse()          # 调用Cats类下的函数catch_mouse.
kitty.dance()                # 调用Cats类下的函数dance.
kitty.breastfeed()           # 调用Cats类的父类Mammals的函数breastfeed.
kitty.move()                 # 调用Cats类的父类Mammals的父类Animals的函数move.