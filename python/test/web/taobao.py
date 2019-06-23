from selenium import webdriver
# import requests
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
def a():
    sleep(5)

from HTMLTestReportCN import HTMLTestRunner
dr=webdriver.Firefox()
url="http://www.taobao.com"
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# dd=requests.get(url=url,hreard=head)
dr.get(url)
a()
dr.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
a()
dr.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
a()
dr.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys('13781186505')
a()
dr.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys('tao423510++')
a()
w=dr.find_element_by_xpath('//*[@id="nc_1_n1z"]')
sleep(2)
ActionChains(dr).drag_and_drop_by_offset(w,260,0).perform()
sleep(1)
dr.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()