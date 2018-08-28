
"?""""
    作者：Yang
    时间：26/08/2018
    版本：2.0
    功能：模拟掷骰子.
    2.0新增功能：模拟两个骰子的情况.
    3.0新增功能：模拟两个骰子情况的可视化.
"""

import random
import matplotlib.pyplot as plt


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_time = 10
    # 初始化列表[0,0,0,0,0,0]
    # 当掷骰子后出现几，则在相应的列表位置上加上.
    result_list = [0] * 11

    # 初始化点数
    roll_list = range(2, 13)
    # zip()函数将两个列表链接.类型为元组类型.
    roll_dict = dict(zip(roll_list, result_list))

    # 记录骰子的结果
    roll1_list = []
    roll2_list = []

    for i in range(total_time):
        roll1 = roll_dice()
        roll2 = roll_dice()

        # 功能：在列表末尾加上一个元素.
        # 目的：将每一次模拟出的结果通过append()函数加到列表末端.
        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1
    for i, result in roll_dict.items():
            print('点数{}的次数：{}, 频率：{}'.format(i, result, result / total_time))

    # 数据可视化.
    x = range(1, total_time + 1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()