"""
    空气质量计算AQI
    作者:Yang
    功能：AQI计算.
    新增功能：读取CSV文件.
    新增功能：读取文件,判断格式调取相应的操作，利用OS模块.
    新增功能：爬虫-网页访问.
    版本：5.0
    日期：31/08/2018
"""
import requests


def get_html_text(url):
    """
        返回url的文本
    """
    r = requests.get(url, timeout=5)
    print(r.status_code)
    return r.text


def read_city_name(filepath):
    f = open(filepath, "r")
    # 读取全部内容 ，并以列表方式返回
    for line in f.readlines():
        line = line.strip('\n')
        return line
        print(line)
    f.close()

def main():
    """
        主函数
    """
    filepath = 'city_name.txt'
    city_pinyin = read_city_name(filepath)
    print(city_pinyin)
    # city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    print(url)
    url_text = get_html_text(url)

    aqi_div = """<div class="span12 data">
        <div class="span1">
          <div class="value">
            """
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index: end_index]
    print('空气质量为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()