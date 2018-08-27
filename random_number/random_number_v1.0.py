"""
    作者：Yang
    功能：模拟掷骰子.
    时间：26/08/2018
    版本：1.0
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
    total_time = 10000
    # 初始化列表[0,0,0,0,0,0]
    # 当掷骰子后出现几，则在相应的列表位置上加上.
    result_list = [0, 0, 0, 0, 0, 0]
    for i in range(total_time):
        result_list[roll_dice() - 1] += 1
    print(type(result_list[2]))
    # enumerate()函数.返回值是一个元组.
    for i, result in enumerate(result_list):
        print('点数{}的次数：{}, 频率：{}'.format(i + 1, result, result / total_time))


if __name__ == '__main__':
    main()