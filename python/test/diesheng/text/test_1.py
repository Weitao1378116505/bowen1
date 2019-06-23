from HTMLTestReportCN import HTMLTestRunner
import unittest
from  appium import webdriver
from time import sleep
from diesheng.config import ds1
from diesheng.config import ds2
from diesheng.config import ds3
log=ds3.get_logger(name='test_1')
class DS(unittest.TestCase):# unittest.TestCase :写测试用例的类，单元测试必须继承他
    # 每个用例执行前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):
        self.des={
          "platformName": "Android",
          "platformVersion": "8.1.0",
          "deviceName": "6286c4da",
          "appPackage": "com.qk.butterfly",
          "appActivity": ".main.LauncherActivity",
          "noReset": "true"
        }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.des)


    def  test_1(self):
        # 写测试用例
        log.info("点击密  登录，进入账号密码登录页面")
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        # 使用脚本与测试数据相结合
        for i in ds1.read_data():
            # 使用账号密码登录
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('{}'.format(i[0]))
            log.info(f'输入的手机号是{i[0]}')
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('{}'.format(i[1]))
            log.info(f'输入的密码是{i[1]}')
            self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
            sleep(3)
        # 断言
            try :
                if "登录"==self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').text:
                    sleep(2)
                # b=="登录":
                # self.assertEqual(b,'登录',msg='失败了')
                    print('失败')
        # 进入登录之后的页面
            except:
                log.info('登录成功的处理........')
                a=self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
                self.assertEqual(a,"热门",msg='登录成功')
                print('成功')
    def test_2(self):
        sleep(3)
        c = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
        self.assertEqual(c, "热门", msg='登录成功')
        print('成功')
    def test_3(self):
        sleep(3)
        a = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
        self.assertEqual(a, "你好", msg='登录成功')
        print('成功')
 # 每个测试用例执行完之后，运行trardown一次，作用：测试用例执行完清理测试环境中的数据
    def tearDown(self):
        log.info('手机与appium断开连接')
        self.dr.quit()
if __name__=='__main__':
    unittest.main()
    ds2.report((DS('test_1'),DS('test_2'),DS('test_3')),report_path=r'C:\开大\test\diesheng\report\a.html')

