"""
    author : Yang
    功能 ：汇率转换
    版本：3.0
    日期：12/08/2018
    新增功能：将汇率换算功能封装在函数中，
"""


# 定义了函数
def convert_currency(im, er):
    """
    汇率兑换函数
    """
    out = im * er
    return out


# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input('请输入带单位的货币金额：')

# 获取货币单位
unit = currency_str_value[-3:]

if unit == 'CNY':
    exchange_rate = USD_VS_RMB

elif unit == 'USD':
    exchange_rate = 1 / USD_VS_RMB

else:
    exchange_rate = -1

if exchange_rate != -1:

    # 获取金额
    value_money = eval(currency_str_value[:-3])
    # 调用函数
    # 将函数返回结果赋值给out_money
    out_money = convert_currency(value_money, exchange_rate)
    print('兑换金额：', out_money)

else:
    print('暂时不支持兑换')