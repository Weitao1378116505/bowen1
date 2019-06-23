from time import sleep
from appium import webdriver
import unittest
from HTMLTestReportCN import HTMLTestRunner
from app.config  import  ds

class DS(unittest.TestCase):
    def  setUp(self):
         self.des={"platformName": "Android",
              "platformVersion": "8.1.0",
              "deviceName": "6286c4da",
              "appPackage": "com.qk.butterfly",
              "appActivity": ".main.LauncherActivity",
              "noReset": "true"}
         self.dr=webdriver.Remote('http://127.0.0 .1:4723/wd/hub',desired_capabilities=self.des)
    def test_1(self):
        sleep(2)
        self.dr.find_element_by_id("android:id/tabs").find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_invite').click()
        sleep(2)
        c = self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_share').text
        sleep(2)
        self.assertEqual(c,"立即邀请",msg='第一次断言')
        print("可以邀请好友")
    def test_2(self):
        sleep(2)
        self.dr.find_element_by_id("android:id/tabs").find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
        sleep(2)
        a=self.dr.find_element_by_id('com.qk.butterfly:id/framelayout').find_elements_by_class_name('android.widget.TextView')[0].text
        self.assertEqual(a,"我的",msg="断言顶部")
        print('查看顶部字符')
    def test_3(self):
        sleep(2)
        self.dr.find_element_by_id("android:id/tabs").find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
        sleep(2)
        b=self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').text
        self.assertEqual(b,"确定",msg="确定退出")
        print('点击确定退出')
    def  tearDown(self):
        self.dr.quit()


if   __name__=="__main__":
    # unittest.main()
    ds.report((DS('test_1'),DS('test_2'),DS('test_3')),path_test=r'C:\开大\test\app\report\DS.html')
