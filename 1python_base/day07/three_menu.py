"""
    day07
    三级菜单
    功能：可以一层一层的进入到所用层.
         可以在每层返回上一层.
         可以在任意层退出,返回菜单.
"""
menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'CCTV':{},
                '渣打银行':{}
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360安全卫士':{}
            },
            '三里屯':{
                '优衣库':{},
                '大使馆':{},
            },
        },
        '昌平':{
                '沙河':{
                '老男孩':{},
                '阿泰包子':{},
                },
                '天通苑':{
                '链家':{},
                '我爱我家':{},
                },
                '回龙观':{},
        },
        '海淀':{
                '五道口':{
                    '谷歌':{},
                    '网易':{},
                    '搜狐':{},
                    '快手':{}
                },
                '中关村':{
                    'YouKu':{},
                    '爱奇艺':{},
                    '土豆':{},
                    '汽车之家':{},
                    '新东方':{},
                    '腾讯':{},
                },
        }
    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                'CICC':{},
                '高盛':{},
            },
            '外滩':{}
        },
        '静安':{}
    },
    '山东':{
        '济南':{},
        '青岛':{},
        '德州':{
            '乐陵':{
                '丁务镇':{}
            },
            '平原':{},
        }
    }
}
# 方法1：
while True:
    for key in menu:
        print(key)
    choice = input("1>>:").strip()
    if choice in menu:
        while True: #程序停在第二层.
            for key2 in menu[choice]:
                print(key2)
            choice2 = input("2>>:").strip()
            if choice2 in menu[choice]:
                for key3 in menu[choice][choice2]:
                    print(key3)
                choice3 = input("3>>:").strip()
                if choice3 in menu[choice][choice2]:
                    while True:
                        for key4 in menu[choice][choice2][choice3]:
                            print(key4)
                        choice4 = input("4>>:").strip()