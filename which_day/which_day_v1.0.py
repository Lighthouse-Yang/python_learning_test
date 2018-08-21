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
    ping_year = ('31', '28', '31','30', '31', '30', '31', '31', '30', '31', '30', '31')
    run_year = ('31', '29', '31','30', '31', '30', '31', '31', '30', '31', '30', '31')
    # print(ping_year)
    # print(type(ping_year))       # 元组类型
    # print(type(ping_year[2]))    # 字符串类型

    i = 1
    s = 0
    if year % 400 == 0:
        # 能整除400则为闰年

        while i < month:
            s = s +int(run_year[i - 1])
            i = i + 1
        days = s + day
        print('闰年', days)
    else:
        while i < month:
            s = s + int(ping_year[i - 1])
            i = i + 1
        days = s + day
        print('平年', days)


if __name__ == '__main__':
    main()

