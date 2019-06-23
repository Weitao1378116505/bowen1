from kuangjia.config.dingdan import Ding_Dan
from kuangjia.data.shuju import shuju
import unittest
class Ddan(unittest.TestCase):
    # ss=shuju()
    # print(ss[0])
    def test_1(self):
        ss = shuju()
        print(ss)
        aaa=Ding_Dan().cha_mingxi(int(ss[1][0]))
        # print(aaa)
        self.assertEqual(aaa["data"]["orderNo"],"V2100880181219390",msg="处理")
    def test_2(self):
        print("hello")
        pass
    def test_3(self):
        a=1
        if a==1:
           pass
        print("真棒")

if __name__=="__main__":
    unittest.main()

# 将所有的以test开头的函数当成测试用例
# 执行顺序是按test后的编码，从小到大依次执行