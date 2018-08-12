"""
    author : Yang
    功能 ：汇率转换
    版本：3.0
    日期：12/08/2018
    新增功能：程序可以一直运行，直到客户选择退出.
"""
# 汇率
USD_VS_RMB = 6.77
i = 0
# 带单位的货币输入
currency_str_value = input('请输入带单位的货币金额(退出exit)：')

while currency_str_value != 'exit':
    i = i + 1
    print('循环次数', i)
    # 获取货币单位
    unit = currency_str_value[-3:]
    value_str = currency_str_value[:-3]
    value = eval(value_str)

    if unit == 'CNY':
        # 输入的是人民币——人民币兑换美元
        usd_value = value/USD_VS_RMB
        print('美元(usd)金额：', usd_value)
    elif unit == 'USD':
        # 输入的是美元——美元兑换人民币
        rmb_value = value*USD_VS_RMB
        print('人民币金额：', rmb_value)
    else:
        print('暂时不支持兑换')
    print('***************************************')
    # 带单位的货币输入
    currency_str_value = input('请输入带单位的货币金额(退出exit)：')

print('程序已退出')