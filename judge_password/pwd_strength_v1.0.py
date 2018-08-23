"""
    作者：Yang
    功能：判断密码强度.
    版本：1.0
    时间：23/08/2018
"""


def check_number_exist(password_str):
    """
        判断字符串是否含有数字
    """
    for c in password_str:
        # 判断字符串中是否只含有数字isnumeric()
        # 通过for循环遍历，如果遇到数字则isnumeric()函数为真，则return True.
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password_str):
    """
        判断字符串是否含有字母
    """
    for c in password_str:
        # 判断字符串中是否只含有数字isnumeric()
        # 通过for循环遍历，如果遇到数字则isnumeric()函数为真，则return True.
        if c.isalpha():
            return True
    return False


def main():
    """
        主函数
    """
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

    if strength_level == 3:
        print('恭喜密码强度合格！')
    else:
        print('密码强度不合格！')


if __name__ == '__main__':
    main()