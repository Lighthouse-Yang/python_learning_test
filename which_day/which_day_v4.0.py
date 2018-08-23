"""
    作者： Yang
    版本：2.0
    功能：判断日期是这一年的第几天.
    2.0新增功能：用列表替换元组.
    3.0新增功能：将月份划分不同的集合在操作.
    4.0新增功能：用字典类型将月份与天数放在一起.
    日期：22/08/2018
"""
import datetime


def is_leap_year(year):
    """
        判断year是否为闰年
        是：返回Ture
        否：返回False
    """
    # 默认不是闰年，假如是则用True赋值.
    is_leap = False

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        is_leap = True
    return is_leap


def main():
    """
        主函数
    """
    input_date_str = input('请输入日期(yyyy/mm/dd):')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 包含30天的月份
    # _30_days_month_set = {4, 6, 9, 11}
    # _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    # 创建字典
    month_day_dict = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}
    day_month_dict = {30: {4, 6, 9, 11},
                      31: {1, 3, 5, 7, 8, 10, 12},
                      28: {2}}
    # 初始化天数
    days = 0
    for i in range(1, month):             # 起始值从1月开始,到month的前一个.
        days = days + month_day_dict[i]
    if is_leap_year(year) and month > 2:
        days += 1

    # 元组-----------元组不能改变元素的值.
    # ping_year = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # 列表-----------列表可以改变元素的值.
    # 假如是闰年，则将2月改为29天.
    # ping_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # if is_leap_year(year):
    #     ping_year[1] = 29
    # days = sum(ping_year[:month - 1]) + day
    print(input_date)
    print('这一天是{}年的第{}天'.format(year, days + day))


if __name__ == '__main__':
    main()

