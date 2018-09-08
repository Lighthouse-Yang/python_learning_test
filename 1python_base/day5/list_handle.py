"""
    列表的操作.
    增删改查
"""
# 创建一个列表.
# names = []
# for i in range(5):
#     name = input('请输入您的名字：')
#     # 1.列表的增加.   append()   insert(位置, '元素')
#           append()函数--在列表末尾增加元素.
#           names.append(name)
#           增加——insert(位置, '元素')
#           names.insert(1, 'wang')    在位置1后插入'wang'.
#
#    2.列表的读取.   直接利用位置对列表进行切片处理.
#           print('切片读取：', names[0], names[1], names[:3], names[-2:])
#
#     # 3.列表的删除.   remove()  del()   pop()
#           """ remove()是对内容的删除.
#               names.remove('zhang')
#               names.remove(names[0])
#               这样就可以删除元素'zhang'或者位置0上所对应的元素内容.
#           """
#
#           """ del()是对列表的位置进行操作.
#               print('删除操作：')
#               del(names[0])
#               del names[-1:]
#               删除的是列表names的0位置内容与
#           """
#
#           """ pop()是对列表的位置进行操作.
#               print('删除操作：')
#               names.pop(1)
#               删除的是列表names的1位置内容，程序会返回所删除的内容.
#           """
# print(names)
#
#     # 4.列表的改动.   很好理解--对列表元素进行再次赋值即可.
#           names[0] = 'zaicifuzhi'
#           根据位置同时修改多个位置.
#           names[1:3] = ['li', 'zhang']

#     # 5.跳动取值：   #表示从0位置取到4位置，隔两个位置. [初始位置：终点位置：步长]
#             number = ['1', '5', '2', '@', '$', '*', '2', 8]
#             print(number[0:6])
#             print(number[0:6:2])
# 若要倒着取元素，则可以将步长设为负数.   取到'*', '$', '@'
#             print(number[5:2:-1])               # 倒着取元素即可.
