"""
    作者：Yang
    功能：52周存钱挑战
    2.0新增功能：记录每周存款数.
    3.0新增功能：使用循环直接计数.
    4.0新增功能：用户灵活设置存钱数.
    5.0新增功能：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额.
    方法：利用math库、列表功能、for循环
    版本：5.0
    日期：21/08/2018
"""
import math
import datetime


# 全局变量
saving = 0


def save_money_in_n_weeks(money_per_week, increase_money, total_week):    # 形参
    """
    记录n周内的存款金额
    """

    money_list = []             # 记录每周存款数的列表
    saved_money_list = []       # 记录每周账户累计
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
        saved_money_list.append(saving)
        # 输出信息
        # print('第{}周，存入{}元，账号累计{}元'.format(i + 1, money_per_week, saving))
        # money_per_week = money_per_week + increase_money
        money_per_week += increase_money
    return saved_money_list


def main():
    """
        主函数
    """
    money_per_week = float(input('请输入初次存入的金额：'))    # 每周存入金额
    increase_money = float(input('请输入每周递增钱数：'))    # 递增的金额
    total_week = int(input('请输入存钱总周数：'))        # 总周数
    # 调用函数
    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)    # 实参
    input_date_str = input('请输入日期(yyyy/mm/dd)')
    # 日期解析，但解析后是datetime类型，需要转化为字符串类型.
    """方法一：
    1.日期解析
    2.利用isocalendar函数输出(年, 周数, 星期几)
    3.将上一步输出转化为字符串类型
    4.截取字符串,拿到自己想要的字符串.
    5.将自己拿到的字符转化为整型int然后进行后续计算.
    """
    time_str = str(datetime.datetime.isocalendar(datetime.datetime.strptime(input_date_str, format('%Y/%m/%d'))))
    week_num = int(time_str[7:9])

    """
    方法二：更简洁,简单.
    1.通过strptime()解析日期
    2.利用isocalendar函数和列表相似的特点，利用位置读取字符
    例如：解析后-----time_str = [2018, 08, 09]
                   time_str.isocalendar()后 变成了[2018, 32 , 3],其中2018是第0位置,32是第1位置,3是第二位置.
    """
    # time_str = datetime.datetime.strptime(input_date_str, format('%Y/%m/%d'))
    # week_num = time_str.isocalendar()[1]

    # week_num = int(input('请输入第几周:'))
    print('第{}周的存款金额：{}元'.format(week_num, saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()