"""
    空气质量计算AQI
    作者:Yang
    功能：AQI计算.
    新增功能：读取CSV文件.
    新增功能：读取文件,判断格式调取相应的操作，利用OS模块.
    版本：3.0
    日期：30/08/2018
"""
import csv
import json
import os


def process_json_file(filepath):
    """
        解码json文件.
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list
    # with关于文件操作.
    # 功课：操作细节一样，只不过不需要关闭.
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    """
        处理csv文件.
    """
    # with关于文件操作.
    # 功课：操作细节一样，只不过不需要关闭.
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # ', '.join(row)
            # 功能：将按行输出的元素直接以''号内的符号为分割就行输出.
            print('---'.join(row))


def main():
    """
        主函数
    """

    filepath = input('请输入文件名称：')
    # 引入OS模块的os.path.splitext()函数
    # 功能：将文件名称和扩展名分开.filename.txt分割为filename、txt两者.
    filename, file_ext = os.path.splitext(filepath)
    if file_ext == '.json':
        # json文件
        process_json_file(filepath)
    elif file_ext == '.csv':
        # csv文件
        process_csv_file(filepath)
    else:
        print('不支持的文件格式！')


if __name__ == '__main__':
    main()