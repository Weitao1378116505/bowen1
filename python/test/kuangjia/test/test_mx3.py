from kuangjia.data.MXshuju import shuju
from kuangjia.config.mingxi import MX
import unittest
class MinX(unittest.TestCase):
    def test_1(self):
        ss=shuju()[3]
        aa=MX().mingxi(ss[0])
        self.assertEqual(aa["errMsg"], "处理成功", msg="处理")
        print("能正常处理")
    def test_2(self):
        ss = shuju()[3]
        aa = MX().mingxi(ss[0])
        self.assertEqual(aa["data"]["ascCode"],None, msg="None=null")
        print("ascCode为空值")
    def test_3(self):
        ss = shuju()[3]
        aa = MX().mingxi(ss[0])
        self.assertEqual(aa["data"]["orderNo"],None, msg="None=null")
        print("orderNo为空值")
if __name__=="__main__":
    unittest.main()