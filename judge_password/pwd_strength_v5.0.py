"""
    作者：Yang
    1.0功能：判断密码强度.
    版本：3.0
    时间：24/08/2018
    2.0新增功能：循环终止.
    3.0新增功能：将密码及强度存入外部介质.
    4.0新增功能：读取文件中保存的密码.
    5.0新增功能：定义一个password工具类.利用'类'就行面向对象编程.
"""
import datetime


class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        # 类的属性
        self.password = password             # 将外围的password传入
        self.strength_level = 0

    # 类的方法
    def check_number_exist(self):
        """                          # password_str其实就是外部传入的password.
            判断字符串是否含有数字       # 再整个PasswordTool类中都可以通过self.password来调用.
        """
        has_number = False
        for c in self.password:
            # 判断字符串中是否只含有数字isnumeric()
            # 通过for循环遍历，如果遇到数字则isnumeric()函数为真，则执行has_number = True并break循环.
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        """
            判断字符串是否含有字母
        """
        has_letter = False
        for c in self.password:
            # 判断字符串中是否只含有数字isnumeric()
            # 通过for循环遍历，如果遇到数字则isnumeric()函数为真，则return True.
            if c.isalpha():
                has_letter = True
        return has_letter

    # 处理字符串
    # 规则1：密码长度大于8
    def process_password(self):
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度必须大于8位！')

        # 规则2：要含有数字及字母
        # 因为函数check_number_exist(password)返回的是True/False，所以通过if条件语句即可
        # 返回值为True 则执行语句.
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码中要包含数字！')

        # 规则3：密码要包含字母.
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码中要包含字母！')


def main():
    """
        主函数
    """
    try_time = 5

    while try_time > 0:
        password = input('请输入密码：')
        # 实例化密码工具对象.
        password_tool = PasswordTool(password)
        password_tool.process_password()

        # 写入文件中
        f = open('password_3.0.txt', 'a')
        # 获取now时间，并保留到毫秒级.
        f.write(str(datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")) + '----')
        f.write('密码：{}-----强度：{}\n'.format(password, password_tool.strength_level))
        f.close()

        if password_tool.strength_level == 3:
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

    # 读取文件
    # f = open('password_3.0.txt', 'r')
    # 1.read()            功能：读取文件中所有内容.
    # content = f.read()
    # print(content)

    # 2.readline()        功能：读取文件中的一行数据.(执行一次只读取一行数据)
    # line = f.readline()
    # print(line)

    # 3.readlines()       功能：读取文件内所有内容，返回值为列表，其中每一项是以换行符为结尾的字符串.
    # readlines()读取返回值为列表，利用for进行遍历.
    # 1-lines = f.f.readlines()-----for line in lines():
    # 2-for line in f.readlines():      这是readlines()遍历的三种写法.
    # 3-for line in f:
    #    print('read:{}'.format(line))
    # f.close()


if __name__ == '__main__':
    main()