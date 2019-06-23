# 生成html测试报告
import HTMLTestReportCN
# 用于单元测试，验证预期结果与实际结果是否一致，一致代表通过，不一致代表失败
import unittest
class  w(unittest.TestCase):
    # 测试用例方法，必须以test开头
    def test_1(self):
        # 预期结果
        x="宝马"
        # 实际结果
        y="劳斯莱斯"
        # 第一个断言方法，判断预期结果与实际结果是够相等
        # x，y的位置可以互换
        self.assertEqual(x,y,msg="msg的作用是备注信息")


    def test_2(self):
        x="宝马"
        y="宝马"
        self.assertEqual(x,y,msg="111")

if __name__=='__main__':
    # 使用unitttest类的main方法，自动加载当前脚本中的类，并自动运行测试用例
    # unittest.main()
    ##############生成测试报告###################
    # 第一步：创建测试套件，理解成玩具枪的弹夹
    aa=unittest.TestSuite()
    # 第二步向测试套件里添加测试用例，理解成添加子弹
    aa.addTest(w('test_1'))
    aa.addTest(w('test_2'))
    # 将生成的测试结果写入html文件里

    with open("a.html",'wb')as fb:
        b= HTMLTestReportCN.HTMLTestRunner(
            stream=fb,
            title="报告名称",
            description="报告描述",
            verbosity=2     #(verbosity代表输出等级，默认0,2代表最详细)
        )
        # 执行测试用例，并生成html测试报告
        b.run(aa)