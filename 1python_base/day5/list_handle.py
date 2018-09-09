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
#
"""
   列表的简单操作. 
"""

# 1.count():计算某元素出现的次数.
t = ['a', 'b', 'c', 'f', 'a', 'b', 'c', 'c']
print(t.count('c'))

# 2.extend():连接两个列表.
a = [1, 2, 3]
b = [2, 4, 6]
a.extend(b)     # a后边连上b列表.
print(a)

# 3.index():查找相应元素的位置信息.
print(a.index(3))   # 查找元素3的位置.
# 当有多个相同元素时，可以利用切片读取进行读取位置.
first_2_index = a.index(2)
print(first_2_index)
litter_list = a[first_2_index + 1:]
print(litter_list)
# 拿到了第二个2在小列表中的位置.
second_2_litter_list_index = litter_list.index(2)
print(second_2_litter_list_index)
second_2_index = first_2_index + second_2_litter_list_index + 1
print('第二个2在列表a中的位置：', second_2_index)
print('元素为：', a[second_2_index])

# 4.列表元素的排序.
t = [3, 4, 5, 7, 9, 0]
# reverse()  列表元素倒叙.
t.reverse()
print(t)
# 按照条件排序.
# sort()从小到大.
t.sort()
print(t)