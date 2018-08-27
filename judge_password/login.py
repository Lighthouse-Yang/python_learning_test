"""
    作者：Yang
    功能：1.将注册成功的密码和用户名存入文件中.
         2.读取文件中的密码和用户名，若正确则登录成功,否则登录失败.
    时间：25/08/2018
    版本：1.0
"""
import datetime


class PasswordTool:

        # 初始化---从外部传入username、password两个参数.
        def __init__(self, username, password, password_):
            self.username = username
            self.password = password
            self.password_ = password_
            self.strength_password = 0

        def determine_password(self):
            # 判断两次密码是否一致.
            if self.password == self.password_:
                return True
            else:                      # 此处需要二次优化.
                return False

        def length_password(self):
            # 判断密码长度.
            if len(self.password) >= 8:
                return True
            else:                     # 此处需要二次优化.
                return False

        def check_number_password(self):
            # 判断密码中是否含有数字.
            has_number = False
            for c in self.password:
                if c.isnumeric():
                    has_number = True
                    break
            return has_number

        def check_letter_password(self):
            # 判断密码中是否含有字母.
            has_letter = False
            for c in self.password:
                if c.isalpha():
                    has_letter = True
                    break
            return has_letter

        def check_result(self):
            """
                    开启判断密码强度工程
                            1.判断密码是否一致.
                            2.判断密码长度是否超过8.
                            3.判断密码中是否还有数字.
                            4.判断密码中是否还有字母.
            """
            # 1.调用'类'方法判断密码是否一致.
            if self.determine_password():
                pass
            else:
                print('密码不一致，请重新输入！')

            # 2.调用'类'方法判断密码长度是否大于等于8.
            if self.length_password():
                self.strength_password += 1
            else:
                print('密码位数必须大于等于8！')

            # 3.调用'类'方法判断密码是否包含数字.
            if self.check_number_password():
                self.strength_password += 1
            else:
                print('密码必须包含字母及数字！')

            # 4.调用'类'方法判断密码是否包含字母.
            if self.check_letter_password():
                self.strength_password += 1
            else:
                print('密码必须包含字母及数字！')


class FileTool:
    def __init__(self, filepath):
        self.filepath = filepath

    # 写入类方法
    def write_to_file(self, time, line):
        f = open(self.filepath, 'a')
        f.write(time)
        f.write(line)
        f.close()

    # 读取类方法
    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        主函数
    """
    # 用户名、密码为登录系统的参数
    print('-----------登录系统-----------')
    username = input('用户名：')
    password = input('密码：')
    password_ = input('确认密码：')
    filepath = 'LoginSystem.txt'
    # 调用PasswordTool类方法.
    password_tool = PasswordTool(username, password, password_)
    password_tool.check_result()
    # 调用FileTool类方法.
    time = (str(datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")) + '----')
    line = '密码：{}-----强度：{}\n'.format(password, password_tool.strength_password)
    file_tool = FileTool(filepath)
    file_tool.write_to_file(time, line)


if __name__ == '__main__':
    main()