"""
    作者：Yang
    功能：52周存钱挑战
    2.0新增功能：记录每周存款数.
    3.0新增功能：使用循环直接计数.
    4.0新增功能：用户灵活设置存钱数.
    方法：利用math库、列表功能、for循环
    版本：4.0
    日期：20/08/2018
"""
import math

# 全局变量
saving = 0


def save_money_in_n_weeks(money_per_week, increase_money, total_week):    # 形参
    """
    记录n周内的存款金额
    """

    money_list = []
    global saving       # 声明global是一个全局变量
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
        # print('第{}周，存入{}元，账号累计{}元'.format(i + 1, money_per_week, saving))
        # money_per_week = money_per_week + increase_money
        money_per_week += increase_money
    return saving


def main():
    """
        主函数
    """
    money_per_week = float(input('请输入初次存入的金额：'))    # 每周存入金额
    increase_money = float(input('请输入每周递增钱数：'))    # 递增的金额
    total_week = int(input('请输入存钱总周数：'))        # 总周数
    save_money_in_n_weeks(money_per_week, increase_money, total_week)    # 实参
    print('总金额：', save_money_in_n_weeks(money_per_week, increase_money, total_week))


if __name__ == '__main__':
    main()