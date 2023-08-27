import json
from pyecharts.options import VisualMapOpts,TitleOpts
from pyecharts.charts import Map

map = Map()

f = open('C:/Users/孙文哲/Desktop/地图数据/疫情.txt','r',encoding='UTF-8')
f_data = f.read()
f.close()


f_dict = json.loads(f_data)
f_children_data = f_dict['areaTree'][0]['children']
list = []
for f_children in f_children_data:
    province_name = f_children['name']
    province_data = f_children['total']['confirm']
    list.append((province_name,province_data))

print(list)

map.add("各省确诊人数",list,'china')
map.set_global_opts(
    title_opts=TitleOpts(title='全国疫情地图',pos_left='center',pos_bottom='1%'),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-9","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999","color":"#FFFF99"},
            {"min":1000,"max":9999,"label":"1000-9999","color":"#FF9966"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#FF6666"},
            {"min": 100000, "max": 999999, "label": "100000-999999", "color": "#CC3333"},
            {"min": 1000000, "lable": '1000000+', "color": "#990033"}
                ]
    )
)
map.render()

print(1,2,34)