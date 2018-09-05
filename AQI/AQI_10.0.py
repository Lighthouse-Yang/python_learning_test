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
    10.0新增功能：利用Pandas就行数据清洗、数据处理及分析.
    版本：10.0
    日期：02/09/2018
"""
import pandas as pd
import matplotlib.pyplot as plt

# 解决plt中中文不能正常显示问题.
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号不能正常显示问题.
plt.rcParams['axes.unicode_minus'] = False


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

    # 数据清洗
    # 规则：只保留AQI大于0的数据.
    # 方法1：
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]
    # 方法2：
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]


    # 基本统计
    print('AQI最小值：', clean_aqi_data['AQI'].min())
    print('AQI平均值：', clean_aqi_data['AQI'].mean())

    # 排序——AQI top10    # 升序排列
    top10_city = clean_aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好100个城市：')
    print(top10_city)

    # tail末尾
    # bottom10_top10_city = aqi_data.sort_values(by=['AQI']).tail(10)
    # 方法二：通过降序排列(ascending=False)取前十，记为最差的10个城市.
    bottom10_top10_city = clean_aqi_data.sort_values(by=['AQI'], ascending=False).tail(10)
    print('空气质量最差10个城市：')
    print(bottom10_top10_city)

    # 保存成csv.
    top10_city.to_csv('top10_aqi.csv', index=False)
    bottom10_top10_city.to_csv('bottom10_top10_aqi.csv', index=False)
    top10_city.plot(kind='bar', x='city', y='AQI', title='空气质量最好的10个城市', figsize=(20, 20))

    plt.savefig('top10_aqi.png')


if __name__ == '__main__':
    main()