"""
    author : Yang
    功能 ：绘制分形树
    日期：15/08/2018
    版本：1.0
    功能：利用递归函数绘制分行树.
"""
import turtle


def draw_branch(branch_length):
    """
    绘制分形树
    """
    if branch_length > 20:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        print('向前', branch_length)
        turtle.right(20)
        print('右转 20')
        draw_branch(branch_length - 10)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40')
        draw_branch(branch_length - 10)

        # 返回之前的树枝
        turtle.right(20)
        print('右转 20')
        turtle.backward(branch_length)
        print('向后', branch_length)


def main():
    """
    主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.pencolor('green')
    draw_branch(80)
    turtle.exitonclick()


if __name__ == '__main__':
    main()

