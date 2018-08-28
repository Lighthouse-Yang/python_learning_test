
"?""""
    作者：Yang
    时间：26/08/2018
    版本：2.0
    功能：模拟掷骰子.
    2.0新增功能：模拟两个骰子的情况.
    3.0新增功能：模拟两个骰子情况的可视化.
    4.0新增功能：对结果进行简单的数据分析---直方图.
"""

import random
import matplotlib.pyplot as plt
# 修改绘图默认的文字，将其修改为中文.
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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
    total_time = 10000

    # 记录骰子的结果
    roll_list = []

    for i in range(total_time):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    #     # 功能：在列表末尾加上一个元素.
    #     # 目的：将每一次模拟出的结果通过append()函数加到列表末端.
    #     roll1_list.append(roll1)
    #     roll2_list.append(roll2)
    #
    #     for j in range(2, 13):
    #         if (roll1 + roll2) == j:
    #             roll_dict[j] += 1
    # for i, result in roll_list:
    #         print('点数{}的次数：{}, 频率：{}'.format(i, result, result / total_time))

    # 数据可视化.
    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='black', linewidth='1')
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()