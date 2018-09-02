"""
    空气质量计算AQI
    作者:Yang
    功能：AQI计算.
    新增功能：读取CSV文件.
    新增功能：读取文件,判断格式调取相应的操作，利用OS模块.
    新增功能：爬虫-网页访问.
    新增功能：利用BeautifulSoup进行网页解析,实现网页爬虫.
    版本：6.0
    日期：01/09/2018
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        获取城市的AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    print(url)
    r = requests.get(url, timeout=30)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append((caption, value))
    return city_aqi


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    city_aqi = get_city_aqi(city_pinyin)
    print('空气质量为：{}'.format(city_aqi))



if __name__ == '__main__':
    main()