# driver 中主要是控制跑回归测试时只跑哪些模块中的用例
from kuangjia.report.baogao import BG
with open('a.txt','r') as f:
    a=f.readlines()
    if 'all' in a:
        BG('*')
    else:
        BG(a)