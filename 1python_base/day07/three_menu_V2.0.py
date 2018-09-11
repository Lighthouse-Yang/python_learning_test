"""
    Author : YangBo
    Time : 2018-09-10 14:14
    function：三级菜单V2.0
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


current_layer = menu
parent_layer = menu
parent_layers = []

while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:
        continue
    if choice in current_layer:
        # parent_layer = current_layer   # 改之前相当于父亲
        parent_layers.append(current_layer)   # 在进入下一层之前，把当前层(及下一层的父层)加入到列表末尾.
        current_layer = current_layer[choice]  # 改成了子层
    elif choice == 'b':
        # current_layer = parent_layer  # 把子层改变父亲层
        if parent_layers:
            current_layer = parent_layers.pop()
    else:
        print('无此选项')
