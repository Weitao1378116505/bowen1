from appium import webdriver
from time import sleep
import unittest

class SZ(unittest.TestCase):
    def setUp(self):
        self.des={
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "6286c4da",
            "appPackage": "com.wayyue.shanzhen",
            "appActivity": ".view.main.SZMainActivity",
            "noReset": "true"
        }
        self.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.des)



        sleep(1)
        self.dr.find_element_by_id('com.wayyue.shanzhen:id/tabLayout').find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
        print("hello")
    def tearDown(self):
        self.dr.quit()

if __name__=="__main__":
    unittest.main()