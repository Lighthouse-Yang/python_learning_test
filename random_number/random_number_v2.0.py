
"?""""
    作者：Yang
    时间：26/08/2018
    版本：2.0
    功能：模拟掷骰子.
    2.0新增功能：模拟两个骰子的情况.
"""

import random


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
    total_time = 50000
    # 初始化列表[0,0,0,0,0,0]
    # 当掷骰子后出现几，则在相应的列表位置上加上.
    result_list = [0] * 11

    # 初始化点数
    roll_list = range(2, 13)
    # zip()函数将两个列表链接.类型为元组类型.
    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_time):
        roll1 = roll_dice()
        roll2 = roll_dice()

        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1
    for i, result in roll_dict.items():
            print('点数{}的次数：{}, 频率：{}'.format(i, result, result / total_time))


if __name__ == '__main__':
    main()