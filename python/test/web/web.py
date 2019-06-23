# web 自动化
# selenium：web自动化测试工具集
# 是selenium 1.0的组成
# 1：selenium IDE 是火狐浏览器的一个插件
# 作用：录制和回放
# 2：selenium Grid 是自动化测试的一个辅助工具
#  作用：可以实现在不同的环境中同时执行测试
# 3 ：selenium RC 是selenium1.0自动化测试的核心
# 作用：控制浏览器的行为

# selenium 2.0的组成
#  selenium1.0（selenium IDE，selenium grid ,selenium  rc)
# +   webdriver：是selenium 2.0的核心
#      作用：控制浏览器行为


# rc 和 webdriver 区别：rc通过将测试代码转换成JavaScript能够识别的动作从而间接去控制浏览器
#  webdriver是通过将浏览器的所有的原生接口集成到webdriver驱动中，通过驱动直接控制浏览器

from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
# dr.get('https://www.qzone.com')
# sleep(2)
# dr.switch_to_frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1678665473')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys("zwy423510++")
# sleep(1)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()

# selenium安装和环境搭建
# 定位 id，class name，name，text，css，xpath
# 定位一组对象;层级定位法：先定为父元素，在定位子元素
dr.get('https://www.ctrip.com/?allianceid=4901&sid=123474&ouid=index')
sleep(3)
# ww=dr.find_elements_by_class_name('mnav')
# print(ww)
# for i in ww:
#     b=i.get_attribute('name')  # 获取某个属性的值
#     print(b)
#     a=i.get_attribute('href')
#     print(a)
# aa=dr.find_element_by_xpath('//*[@id="J_roomCountList"]').find_elements_by_tag_name("option")
# for i in aa:
#     b=i.get_attribute('value')
#     print(b)
#     i.click()
#     sleep(3)
# dr.find_element_by_xpath('//*[@id="J_RoomGuestInfoTxt"]').click()
# for i in range(5):
#     bb=dr.find_element_by_xpath('//*[@id="J_cildNumSelectorBox"]/div/ul/li[1]').find_element_by_xpath('//*[@id="J_AdultCount"]/span[2]').click()
# from selenium.webdriver.common.action_chains import ActionChains
# # dr.get('http://www.jd.com')
# # sleep(3)
# # aa=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
# # # print(len(aa))
# # for i in aa:
# #     ActionChains(dr).move_to_element(i).perform()
# #     sleep(2)
#
#
#
# dr.get('https://www.qzone.com')
# sleep(2)
# dr.switch_to_frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('4547774')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys("zwy++")
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
#
# # iframe:内部镶嵌（窗口）
# # 切换到某个框架上去，通过id，name的值
# dr.switch_to_frame('tcaptcha_iframe')
# # dr.switch_to_default_content() #回退到最初的页面上
# w=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# sleep(2)
# # dr.switch_to_parent_frame
#
# # drag_and_drop里面二个参数：一个起始位置，一个终点位置
# # drag_and_drop_by_offset（ ）：三个参数（起始位置，x轴坐标，y轴坐标）
# ActionChains(dr).drag_and_drop_by_offset(w,170,0).perform()




# 任何浏览器管理窗口的原理
# 将每个窗口用一个特定的字符来标识
# 只需要获取每个窗口的标识号
# 通过切换标志号，就能达到切换窗口的目的

# 获取当前窗口的标识
# dr.get('http://www.douban.com')
# sleep(3)
# print(dr.title)
# print(dr.current_window_handle)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(2)
# aa=dr.window_handles
# dr.switch_to.window(aa[-1])
# sleep(2)
# print(dr.title)
# for i in range(0,10000,500):
# 滑动条
#     js="var q=document.documentElement.scrollTop={}".format(i)
#     dr.execute_script(js)
#     sleep(2)

# dr.get('file:///C:/Users/weit/Desktop/abc.html')
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# # 切换到弹出框上去
# ww=dr.switch_to_alert()
# # 获取弹出框上面的文本
# print(ww.text)
# # 点击确定
# ww.accept()
# # 点击取消
# ww.dismiss()
# # 点击输入
# ww.send_keys('6666')
# 只能等待
# import selenium.webdriver.support.ui as ui
# dr.get('https://www.baidu.com')
# # sleep(3)
# # 创建一个只能等待
# unit = ui.WebDriverWait(dr,10)  # 10代表最大等待时间
# # 如果定位的元素出现了就不必在等待
# unit.until(lambda dr: dr.find_element_by_link_text('hao123').is_displayed())
# # 检测hao123这个文本内容是否出现，如果出现就继续执行，如果没有出现，最大等待时间10s
# dr.find_element_by_link_text('新闻').click()
