"""
    作者：Yang
    时间：26/08/2018
    版本：2.0
    功能：模拟掷骰子.
    2.0新增功能：模拟两个骰子的情况.
    3.0新增功能：模拟两个骰子情况的可视化.
    4.0新增功能：对结果进行简单的数据分析---直方图.
    5.0新增功能：使用科学计算简化程序.
"""

import random
import matplotlib.pyplot as plt
import numpy as np
# 修改绘图默认的文字，将其修改为中文.
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    total_time = 10000

    # 记录骰子的结果
    # 创建total_time个1-6的随机数，存储为total_time行1列的矩阵.
    roll1_arr = np.random.randint(1, 7, size=total_time)
    roll2_arr = np.random.randint(1, 7, size=total_time)
    # 矩阵相加.
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

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
    plt.hist(result_arr, bins=range(2, 14), normed=1, edgecolor='black', linewidth='1', rwidth=0.8)

    # 设置x轴坐标显示
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_labels)

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()