"""
    author : Yang
    功能 ：汇率转换
    日期：10/08/2018
"""

change_str_way = input('请选择您要兑换的币种： 1.人民币(RMB)    2.美元(USD)')
change_way = eval(change_str_way)
if change_way == 1 :
    usd_str_value = input('请输入美元(USD)金额:')
    # 将字符串转化为数字
    usd_value = eval(usd_str_value)
    vs = 6.77
    rmb_value = usd_value * vs
    print('兑换人民币(RMB)', rmb_value)

elif change_way == 2 :
    rmb_str_value = input('请输入人民币(RMB)金额:')
    # 将字符串转化为数字
    rmb_value = eval(rmb_str_value)
    vs = 6.77
    usd_value = rmb_value / vs
    print('兑换美元(USD)', usd_value)

else:
    print ('输入有误，请重新输入')