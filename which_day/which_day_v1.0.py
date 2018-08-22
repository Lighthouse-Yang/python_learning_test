"""
    作者： Yang
    版本：1.0
    功能：判断日期是这一年的第几天.
    日期：21/08/2018
"""
import datetime


def main():
    """
        主函数
    """
    input_date_str = input('请输入日期(yyyy/mm/dd):')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day
    ping_year = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(ping_year[:month - 1]) + day
    # 判断闰年
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        if month > 2:
            days = days + 1
    print('这一天是第{}天'.format(days))


if __name__ == '__main__':
    main()

