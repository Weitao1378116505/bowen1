# 生成测试报告用的
# 第一步：创建测试套件，理解成玩具枪的弹夹
from HTMLTestReportCN import HTMLTestRunner
import unittest
def report(*test_name,report_path):
    aa = unittest.TestSuite()
# 第二步向测试套件里添加测试用例，理解成添加子弹
    for i in test_name[0]:
        aa.addTest(i)
# 将生成的测试结果写入html文件里

    with open(report_path, 'wb')as fb:
        b = HTMLTestRunner(
            stream=fb,
            title="报告名称",
            description="报告描述",
            verbosity=2  # (verbosity代表输出等级，默认0,2代表最详细)
             )
    # 执行测试用例，并生成html测试报告
        b.run(aa)