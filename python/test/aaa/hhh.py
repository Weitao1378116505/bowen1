# import requests
# import random
# import json
# import time
#
# starturl = 'https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd={0}&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin={1}&ein={2}'
# rnd = random.random()
# sin = 0
# ein = 29
#
# while True:
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#     }
#     headers['referer'] = 'https://y.qq.com/portal/playlist.html'
#     disslist = requests.get(starturl.format(rnd, sin, ein), headers=headers).text
#     disslist = json.loads(disslist.strip('getPlaylist()'))
#     # print(disslist)
#
#     for i in disslist['data']['list']:
#         dissid = i['dissid']
#         dissName = i['dissname']
#         # print(dissidlist)
#
#         dissurl = 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid={0}&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
#         headers['referer'] = 'https://y.qq.com/n/yqq/playsquare/{0}.html'.format(dissid)
#         song = requests.get(dissurl.format(dissid), headers=headers).text
#         song = json.loads(song.strip('playlistinfoCallback()'))
#
#         num = 1
#         for s in song['cdlist'][0]['songlist']:
#             # 获取songmid
#             songmid = s['songmid']
#             # 获取歌曲名
#             songName = s['songname']
#             # 获取strMediaMid
#             strMediaMid = s['strMediaMid']
#             # filename
#             filename = 'C400' + str(s['strMediaMid']) + '.m4a'
#             vkeyurl = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback&uin=0&songmid={0}&filename={1}&guid=7670101313'
#             # 发送请求
#             headers['referer'] = 'https://y.qq.com/portal/player.html'
#             responses = requests.get(vkeyurl.format(songmid, filename), headers=headers).text
#             responses = json.loads(responses.strip('MusicJsonCallback()'))
#             # print(responses)
#             # 提取vkey
#             for vk in responses['data']['items']:
#                 vkey = vk['vkey']
#
#
#
#
#                 musicurl = 'http://dl.stream.qqmusic.qq.com/{0}?vkey={1}&guid=7670101313&uin=0&fromtag=66'
#                 del headers['referer']
#                 result = requests.get(musicurl.format(filename, vkey), headers=headers, stream=True).raw.read()
#                 with open(r'C:\Users\weit\Desktop\music/' + songName + '.mp3', 'wb') as file:
#                     file.write(result)
#                 # time.sleep(0.1)
#             print('{0}歌单的第{1}歌-歌曲名称:{2}'.format(dissName, num, songName))
#             num += 1
#     if sin < disslist['data']['sum']:
#         sin += 30
#         ein += 30
#         rnd = random.random()
#         time.sleep(1)
#     else:
#         break
# import socket
# while True:
#     sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     host=(('192.168.0.97',3000))
#     m=input('>>>')
#     sock.sendto(m.encode('utf-8'),host)
#     bB=sock.recv(1024)
#     print(bB.decode('utf-8'))









# import socket
# while True:
#     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     sock.connect(('192.168.0.97',3000))
#     b='hello'
#     sock.send(b.encode('utf-8'))
#     a=sock.recv(1024)
#     print(a.decode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host=(('192.168.0.97',3000))
# b='hello'
# s.sendto(b.encode('utf-8'),host)
# aa=s.recv(1024)
# print(aa.decode('utf-8'))


#
# from selenium import webdriver
# from time import sleep
# re =webdriver.Chrome()
# re.get('https://qzone.qq.com')
# re.switch_to_frame('login_frame')
# sleep(2)
# re.find_element_by_css_selector('#switcher_plogin').click()
# sleep(2)
# re.find_element_by_xpath('//*[@id="u"]').send_keys('1678665473')
# sleep(2)
# re.find_element_by_xpath('//*[@id="p"]').send_keys('zwy423510++')
# sleep(2)
# re.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# # re.find_element_by_xpath('//*[@id="$1_substitutor_content"]').click()
# # sleep(2)
# re.find_element_by_xpath('//*[@id="$1_substitutor_content"]').send_keys('   今天已经星期五了   ')
# sleep(2)
# re.find_element_by_xpath('//*[@id="QM_Mood_Poster_Inner"]/div/div[4]/div[4]/a[2]/span').click()




# from selenium import webdriver
# from time import sleep
# re =webdriver.Chrome()
# re.get('https://www.baidu.com')
# sleep(1)
# re.find_element_by_xpath('//*[@id="kw"]').send_keys('开封大学')
# sleep(1)
# re.find_element_by_xpath('//*[@id="su"]').click()
# sleep(1)
# re.find_element_by_xpath('//*[@id="1"]/h3/a[1]/em').click()


# import requests
# url='https://m801.music.126.net/20190524173917/c462a5be83d83961977d0904970140b4/jdyyaac/000e/565c/010b/7d63c13ce1a64ac9fae36a2e3b354630.m4a'
# res = requests.get(url)
# # p=res.content.decode()
# print(res)
# with open('1.mp4','wb',encoding='utf-8') as f:
#     f.write(res)

# def f(x):
#     y=x+1
#     return  y
# print(f(1))


# import  pymysql
# import  xlwt
# import xlrd
# conn = pymysql.connect(host='192.168.0.87',port=3306,user='root',passwd='123456')
# a=xlwt.Workbook('a1.xls')
# b=a.add_sheet('test')
# b.write(0,0,'name')
# b.write(0,1,'sex')
# b.write(0,2,'id')
# b.write(0,3,'kemu')
# a.save('a1.xls')
# m=conn.cursor()
# m.execute("use  test;")
# a=xlrd.open_workbook('a.xls')
# sheet=a.sheets()[0]
# c=sheet.nrows
# print(c)
# for i in range(c):
#     b = sheet.row_values(i)
#     if i==0:
#         # m.execute("'(create  table day1({}  char(20),{}  char(),{} int(),{}  char())'.format(b[0],b[1],b[2],b[3])")
#         m.execute('create table day1 ({} char(10),{}  char(10),{} char(10));'.format(b[0],b[1],b[2]))
#     else:
#         # m.execute("insert  into  day1  values('{}','{}','{}').format(b[0],b[1],b[2])")
#         m.execute("insert into day1 values('{}','{}','{}');".format(b[0],b[1],b[2]))


from appium import webdriver
from time import sleep
# des={
#   "platformName": "Android",
#   "platformVersion": "8.1.0",
#   "deviceName": "6286c4da",
#   "appPackage": "com.ss.android.ugc.aweme",
#   "appActivity": ".main.MainActivity",
#   "noReset": "true"
# }# 抖音
# des={
#   "platformName": "Android",
#   "platformVersion": "8.1.0",
#   "deviceName": "6286c4da",
#   "appPackage": "com.tencent.tim",
#   "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#   "noReset": "True",
#   "unicodekeyboard": "unicod"
# }  # qqtim
# # http://127.0.0.1:4723/wd/hub 写死的
# # 测试脚本与appium服务器建立一个session连接
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=des)
# # dr.quit()
# 层级定位 第一步：先定义一个唯一的元素，在定位多个相同的元素
# a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# 安卓独有的
# 输入账号
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').click()
# sleep(1)
# dr.find_element_by_accessibility_id("清除帐号").click()
# sleep(1)
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').send_keys('1678665473')
# sleep(1)
# # 输入密码
# dr.find_element_by_id('com.tencent.tim:id/password').clear()
# sleep(1)
# dr.find_element_by_id('com.tencent.tim:id/password').send_keys('zwy423510++')
# sleep(1)
# # 点击登录
# dr.find_element_by_id('com.tencent.tim:id/login').click()
# a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# a[-1].click()
# for i in a:
#   sleep(0.5)
#   i.click()
#   sleep(0.5)
#   print(i.text)
# sleep(2)
# print(a)
# 滑动 1:获取手机屏幕大小
# s = dr.get_window_size()
# print(s)
# # 2:放缩 x，y轴
# while True:
#   x1=s['width']*0.5
#   y1=s['height']*0.4
#   y2=s['height']*0.7
#   # 第三步：使用swipe方法进行滑动炒作
#   dr.swipe(x1,y2,x1,y1,duration=500)
#   sleep(30)
# dr.find_element_by_accessibility_id('好友动态').click()
# sleep(2)
# dr.find_elements_by_class_name('android.widget.ImageView')[1].click()
# t=dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name("android.widget.RelativeLayout")
# t[-1].click()
# sleep(1)
# dr.find_element_by_class_name("android.widget.FrameLayout").find_elements_by_class_name("android.widget.ImageView").click()

