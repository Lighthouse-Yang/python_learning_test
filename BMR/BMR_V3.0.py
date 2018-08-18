"""
    BMR
    功能:计算人体的BMR数值.
    新增功能:程序循环执行直到用户选择退出.
    time:16/08/2018
    版本:2.0
"""


# 男性
def man(weight, height, age):
    BMR = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    return BMR


# 女性
def woman(weight, height, age):
    BMR = 13.7 * weight + 5.0 * height - 6.8 * age + 66
    return BMR


def main():
    """
    主函数
    """

    change = input('是否退出程序：Y/N')

    while change != 'Y':
        """
        循环,当输入Y时程序停止
        """
        # gender = input('请输入您的性别:')
        # age = int(input('请输入您的年龄:'))
        # height = float(input('请输入您的身高(cm):'))
        # weight = float(input('请输入您的体重(kg):'))
        print('请输入以下信息，用空格分割')
        input_str = input('性别 体重(kg) 身高(cm) 年龄：')
        # input_str = '男 75 175 25' input_str拿到的是这样的字符串.
        # 方法一：

        """
        input_str.find(' ')------find函数功能找到相应字符的位置.
        即在input_str = '男 75 175 25' 的情况下，
        会输出：1
        代表空格的位置为1，那我们可以用 input_str[:1]拿到从头开始到1位置的字符(不包括1位置的字符)
        这样我们就拿到了 '男' 这个字符，同理其余字符也可以这样拿到但是相对比较麻烦.
        """
        # 方法一实施：
        # gender = input_str[:1]
        # weight = float(input_str[2:4])
        # height = float(input_str[5:8])
        # age = int(input_str[9:])


        # 方法二：

        """
        优点：相比较方法一更简单.
            split函数：python中字符分割的函数.
            for example :L = input_str.split(' ')   
                使用时函数参数的选择即为分割标准，如上例中' '中间为空格即为按照空格分割字符串.
                         函数输出：L = ['男', '75', '175', '25']
        利用type()函数查看其类型：
            type(L)----输出为list代表其为列表类型.这样就可以用L[0] L[1] L[2]等方式拿到字符
        """
        # 方法二实施：

        L = input_str.split(' ')
        gender = L[0]
        weight = float(L[1])
        height = float(L[2])
        age = int(L[3])
        input_str.split(' ')
        if gender == '男':
            bmr = man(weight, height, age)
        elif gender == '女':
            bmr = woman(weight, height, age)
        else:
            bmr = -1
        if bmr != -1:
            print('您的性别：{} 体重：{}kg 身高：{}cm 年龄：{}岁'.format(gender, weight, height, age))
            print('您的BMR数值为：{}大卡'.format(bmr))
            # {} 为一个占位作用
        else:
            print('暂不支持该性别的计算')
        print()  # 什么也不输入时会输入一个空行
        print('**************************************')
        change = input('是否退出程序：Y/N')
    print('程序已退出')


if __name__ == '__main__':
    main()
