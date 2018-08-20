"""
    作者：Yang
    功能：52周存钱挑战
    新增功能：自带计数的循环--for循环.
    方法：利用math库、列表功能、for循环
    版本：3.0
    日期：20/08/2018
"""
import math


def main():
    """
        主函数
    """
    money_per_week = 10    # 每周存入金额
    # i = 1                  # 记录周数
    increase_money = 10    # 递增的金额
    total_week = 52        # 总周数
    saving = 0             # 账户累计

    money_list = []

    # while i <= total_week:
    for i in range(total_week):
        # for循环的i遍历list的每一个元素，并且遍历后会将元素位置赋值给i，
        # 所以不再需要i++来计数，只需要打印就可以.

        # 存钱操作
        # saving = money_per_week + saving    两句相等
        # saving += money_per_week
        # append()函数功能：将元素添加到列表末尾.
        money_list.append(money_per_week)

        saving = math.fsum(money_list)
        # 输出信息
        print('第{}周，存入{}元，账号累计{}元'.format(i + 1, money_per_week, saving))
        # money_per_week = money_per_week + increase_money
        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()