import os, time
home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILTER_EN = home + r'\file\filter\EN_filter.txt'
# if not os.path.exists(FILTER_EN):
#     os.makedirs(FILTER_EN)

# 新建文件夹的前缀
ymd = time.strftime('%Y%m%d', time.localtime())
PREFIX = home + '\\file\\analysis\\' + ymd
# if not os.path.exists(PREFIX):
#     os.makedirs(PREFIX)
if __name__ == '__main__':
    print(home)
    print(FILTER_EN)
    print(PREFIX)