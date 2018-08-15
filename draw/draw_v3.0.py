"""
    author : Yang
    功能 ：绘制五角星
    日期：14/08/2018
    功能：利用递归函数进行五角星绘制.
"""
import turtle


def draw_pentagram(size):
    """
    绘制五角星
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    size += 10
    if size <= 200:
        draw_pentagram(size)


def main():
    """
    主函数
    """
    # 初始边长
    size = 100
    draw_pentagram(size)


if __name__ == '__main__':
    main()

