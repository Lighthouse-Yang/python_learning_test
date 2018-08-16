"""
    BMR
    功能:计算人体的BMR数值.
    time:16/08/2018
    版本:1.0
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
    gender = input('请输入您的性别：')
    str_age = input('请输入您的年龄:')
    age = int(str_age)
    str_height = input('请输入您的身高(cm):')
    height = float(str_height)
    str_weight = input('请输入您的体重(kg):')
    weight = float(str_weight)

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

    # print('您的BMR：', bmr)


if __name__ == '__main__':
    main()
