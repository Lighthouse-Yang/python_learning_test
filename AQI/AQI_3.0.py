"""
    空气质量计算AQI
    作者:Yang
    功能：AQI计算.
    新增功能：读取CSV文件.
    版本：3.0
    日期：30/08/2018
"""
import csv
import json

def process_json_file(filepath):
    """
        解码json文件.
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    """
        主函数
    """

    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []
    # 列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()