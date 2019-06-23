from kuangjia.data.shuju1 import shuju1
from kuangjia.config.qingq import QQ
import unittest
class Q(unittest.TestCase):
    def test_1(self):
        ss=shuju1()
        print(ss)
        print(ss[1])
        aa=QQ().qing(int(ss[1]))
        self.assertEqual(aa["data"]["orderType"], "11", msg="处理")
    def test_2(self):
        a=2
        self.assertEqual(a,2,msg="666")
if __name__=="__main__":
    unittest.main()