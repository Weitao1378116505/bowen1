from  HTMLTestReportCN import HTMLTestRunner
import unittest
from kuangjia.config.dingdan import Ding_Dan
# pycharm本身也带了一个unittest模块
def BG(name):
    suit=unittest.TestSuite()
    # 将某一个类中所有的测试用例
    # suit.addTest(unittest.makeSuite(Ding_Dan))
    # 第一个参数存放测试脚本的路径，第二个参数时匹配测试文件的通配符
    # 自动发现符合通配符的文件中以test开头的函数，提取出来放在dis列表中
    for j in name:
        dis=unittest.defaultTestLoader.discover(r'C:\开大\test\kuangjia\test',pattern='{}.py'.format(j.strip()))
        for i in dis:
            suit.addTest(i)
    f=open('a.html','wb')
    runner=HTMLTestRunner(stream=f,tester='wt',description='结果如下',title="别克测试报告")
    runner.run(suit)
    f.close()

# if __name__=="__main__":
#     BG()