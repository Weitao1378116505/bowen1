from HTMLTestReportCN import HTMLTestRunner
import unittest
def report(*test_name,path_test):
    aa = unittest.TestSuite()
    for i in test_name[0]:
        aa.addTest(i)
    with open(path_test, 'wb')as fb:
        b = HTMLTestRunner(
            stream=fb,
            title="碟声退出报告",
            description="报告描述",
            verbosity=2 )
        b.run(aa)