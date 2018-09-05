"""
    空气质量计算AQI
    作者:Yang
    功能：AQI计算.
    新增功能：读取CSV文件.
    新增功能：读取文件,判断格式调取相应的操作，利用OS模块.
    新增功能：爬虫-网页访问.
    新增功能：利用BeautifulSoup进行网页解析,实现网页爬虫.
    新增功能：获取所有城市的AQI.
    新增功能：将获取到的所有城市的AQI保存到csv文件中.
    9.0新增功能：利用Pandas就行数据处理及分析.
    版本：9.0
    日期：02/09/2018
"""
import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # # print(aqi_data.head(5))
    # # 获取多行时，需要放入一个列表['city', 'AQI']这样,所以是两个括号.
    # print(aqi_data[['city', 'AQI']])

    print('基本信息：')
    print(aqi_data.info())

    print('数据预览')
    print(aqi_data.head())

    # 基本统计
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI平均值：', aqi_data['AQI'].mean())

    # 排序——AQI top10    # 升序排列
    top100_city = aqi_data.sort_values(by=['AQI']).head(100)
    print('空气质量最好100个城市：')
    print(top100_city)

    # tail末尾
    # bottom100_top100_city = aqi_data.sort_values(by=['AQI']).tail(10)
    # 方法二：通过降序排列(ascending=False)取前十，记为最差的10个城市.
    bottom100_top100_city = aqi_data.sort_values(by=['AQI'], ascending=False).tail(100)
    print('空气质量最差100个城市：')
    print(bottom100_top100_city)

    # 保存成csv.
    top100_city.to_csv('top100_aqi.csv', index=False)
    bottom100_top100_city.to_csv('bottom100_top100_aqi.csv', index=False)


if __name__ == '__main__':
    main()