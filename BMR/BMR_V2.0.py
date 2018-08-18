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
        gender = input('请输入您的性别:')
        age = int(input('请输入您的年龄:'))
        height = float(input('请输入您的身高(cm):'))
        weight = float(input('请输入您的体重(kg):'))

        if gender == '男':
            bmr = man(weight, height, age)
        elif gender == '女':
            bmr = woman(weight, height, age)
        else:
            bmr = -1
        if bmr != -1:
            print('您的BMR数值为：', bmr)
        else:
            print('暂不支持该性别的计算')
        print()  # 什么也不输入时会输入一个空行
        change = input('是否退出程序：Y/N')
    print('程序已退出')


if __name__ == '__main__':
    main()