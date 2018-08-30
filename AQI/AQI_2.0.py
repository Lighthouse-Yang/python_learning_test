"""
    空气质量计算AQI
    作者:Yang
    功能：AQI计算.
    新增功能：
    版本：2.0
    日期：30/08/2018
"""
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
    top5_list = city_list[:5]

    f = open('tops_aqi_json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    print(city_list)


if __name__ == '__main__':
    main()