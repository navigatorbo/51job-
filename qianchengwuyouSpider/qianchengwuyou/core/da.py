import pyecharts
from pyecharts import Bar
import pandas as pd
import pyecharts
from pyecharts import *

import os,sys
os.chdir('F:\python\python_file\qianchengwuyouSpider\qianchengwuyou')
os.getcwd()


class Dshow:
    def __init__(self):
        self.path= r'F:\python\python_file\qianchengwuyouSpider\qianchengwuyou\file\analysis\python.xlsx'
    def Make_Bar(self):
        sheet2 = pd.read_excel(self.path, sheet_name='salary_section-edu')
        dazhuan = sheet2['大专']
        benke = sheet2['本科']
        shuoshi = sheet2['硕士']
        boshi = sheet2['博士']
        attr = ['大专','本科','硕士','博士']
        v = [dazhuan.sum(),benke.sum(),shuoshi.sum(),boshi.sum()]
        bar =Bar('学历要求')
        bar.add('python',attr,v,
                 mark_point=['average'],
                 # is_convert=True,
                 is_more_utils=True
                 )
        bar.show_config()
        bar.render('./file/analysis/bar.html')

    def Make_Word(self):
        sheet2=pd.read_excel(self.path,sheet_name='Cndetail')
        h2 =sheet2['Cndetail'].drop(0)
        c2 = sheet2['frequency'].drop(0)
        worldcloud = WordCloud(width=1300, height=620)
        worldcloud.add('', h2, c2, word_size_range=[20, 100])
        worldcloud.render('./file/analysis/worldcloud01.html')

    def Make_Map(self):
        sheet3 = pd.read_excel(self.path,sheet_name='CNTregion')
        h3 = sheet3['CNTregion']
        c3 = sheet3['frequency']
        zp=dict(zip(h3,c3))
        dic = {}
        temp={}
        for key,value in zp.items():
            if key.find('-') >0:
                na = key.split('-')[0]
                dic[na] = value
            else:
                dic[key] = value
        for key,value in zp.items():
            if key.find('-') >0:
                na = key.split('-')[0]
                dic[na] += value
            else:
                dic[key] += value
        for key, value in dic.items():
            if key[-3:] != '开发区' and key[-1:] != '省':
                temp[key] = value

        geo = Geo("全国岗位分布", "data from 51job", title_color="#fff", title_pos="center", width=1200, height=600,
                  background_color='#404a59')
        # type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
        geo.add("空气质量评分", temp.keys(), temp.values(), type="effectScatter", is_random=True, effect_scale=5,
                visual_range=[0, 5],
                visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
        geo.show_config()
        geo.render("./file/analysis/岗位分布.html")


    def start_draw(self):
        self.Make_Bar()
        self.Make_Word()
        # self.Make_Map()

# if __name__ == '__main__':
#     model = Dshow()
#     model.Make_Map()