"""
    作者：Yang
    1.0功能：判断密码强度.
    版本：3.0
    时间：24/08/2018
    2.0新增功能：循环终止.
    3.0新增功能：将密码及强度存入外部介质.
"""
import datetime


def check_number_exist(password_str):
    """
        判断字符串是否含有数字
    """
    has_number = False
    for c in password_str:
        # 判断字符串中是否只含有数字isnumeric()
        # 通过for循环遍历，如果遇到数字则isnumeric()函数为真，则执行has_number = True并break循环.
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):
    """
        判断字符串是否含有字母
    """
    has_letter = False
    for c in password_str:
        # 判断字符串中是否只含有数字isnumeric()
        # 通过for循环遍历，如果遇到数字则isnumeric()函数为真，则return True.
        if c.isalpha():
            has_letter = True
    return has_letter


def main():
    """
        主函数
    """
    try_time = 5

    while try_time > 0:
        password = input('请输入密码：')

        # 密码强度
        strength_level = 0

        # 规则1：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度必须大于8位！')

        # 规则2：要含有数字及字母
        # 因为函数check_number_exist(password)返回的是True/False，所以通过if条件语句即可
        # 返回值为True 则执行语句.
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码中要包含数字！')

        # 规则3：密码要包含字母.
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码中要包含字母！')

        # 写入文件中
        f = open('password_3.0.txt', 'a')
        # 获取now时间，并保留到毫秒级.
        f.write(str(datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")) + '----')
        f.write('密码：{}-----强度：{}\n'.format(password, strength_level))
        f.close()

        if strength_level == 3:
            print('恭喜密码强度合格！')
            # 密码合格，则直接跳出循环.
            break
        else:
            print('密码强度不合格！')
            # 密码不合格，则减少一次机会.
            try_time -= 1
        print(' ')

    if try_time <= 0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()