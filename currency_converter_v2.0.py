"""
    author : Yang
    功能 ：汇率转换
    版本：2.0
    日期：10/08/2018
    新增功能：根据输入判断是人民币还是美元，进行相应的转换计算.
"""
# 汇率
USD_VS_RMB = 6.77
# 带单位的货币输入
currency_str_value = input('请输入带单位的货币金额：')
# 获取货币单位
unit = currency_str_value[-3:]
value_str = currency_str_value[:-3]
value = eval(value_str)

if unit == 'CNY':
    # 输入的是人民币——人民币兑换美元
    usd_value = value/USD_VS_RMB
    print('美元金额：', usd_value)
elif unit == 'USD':
    # 输入的是美元——美元兑换人民币
    rmb_value = value*USD_VS_RMB
    print('人民币金额：', rmb_value)
else:
    print('暂时不支持兑换')








# change_str_way = input('请选择您要兑换的币种： 1.人民币(RMB)    2.美元(USD)')
# change_way = eval(change_str_way)
# if change_way == 1 :
#     usd_str_value = input('请输入美元(USD)金额:')
#     # 将字符串转化为数字
#     usd_value = eval(usd_str_value)
#     vs = 6.77
#     rmb_value = usd_value * vs
#     print('兑换人民币(RMB)', rmb_value)
# elif change_way == 2 :
#     rmb_str_value = input('请输入人民币(RMB)金额:')
#     # 将字符串转化为数字
#     rmb_value = eval(rmb_str_value)
#     vs = 6.77
#     usd_value = rmb_value / vs
#     print('兑换美元(USD)', usd_value)
#
# else:
#     print ('输入有误，请重新输入')