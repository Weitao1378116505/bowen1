#!/usr/bin/python
#-*- coding:utf-8 -*-

# 九九乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         if j <= i :
#             print('{}x{}={}'.format(i,j,i*j),end=' ')
#     print('\n')

# 将字符串不用int 变成数字
# a='1231'
# b=a[::-1]
# d=0
# for i in range(len(a)):
#     for j in range(10):
#         if b[i] == str(j):
#             c=j*10**i
#             d=d+c
# print(d)

#创建目录aaa
# import os
# # os.mkdir('aaa')
# f=open('aaa//a.out','w+',encoding='utf-8')
# for i in range(5):
#     f.write('aaa')
#     f.write('\n')

# 将a.txt文件添加到数据库中
# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# aa=a[0].split(',')
# import pymysql
# conn=pymysql.connect(host='192.168.0.87',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use test')
# m.execute('create table kaoshi({} char(10),{} char(10),{} char(10));'.format(aa[0],aa[1],aa[2]))
# for i in range(1,len(a)):
#     bb=a[i].split(',')
#     m.execute('insert into kaoshi values("{}","{}","{}");'.format(bb[0],bb[1],bb[2]))


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.92',3000))
# s.listen(4)
# while  True :
#     a,b=s.accept()
#     reg=a.recv(1024)
#     print(reg.decode('utf-8'))
#     msg='welcome'
#     a.send(msg.encode('utf-8'))





# import smtplib
# import email.mime.multipart as  aa
# import email.mime.text as bb
# cc= aa.MIMEMultipart()
# cc['Subject']=('nihao')
# cc['From']=('weitao_423510@163.com')
# cc['To']=('18317822978@163.com')
# txt=""""hello"""
# aaa=bb.MIMEText(txt)
# cc.attach(aaa)
# ee=bb.MIMEText(open('a.txt','rb').read(),'base64','utf-8')
# ee["content-type"]='application/octet-stream'
# ee['Content-Disposition']='attachment.filename"a.txt"'
# cc.attach(ee)
# dd=smtplib.SMTP_SSL('smtp.163.com',465)
# dd.login('weitao_423510@163.com','a423510')
# dd.sendmail('weitao_423510@163.com','18317822978@163.com',cc.as_string())
# dd.close()


# https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&=0&_v=0.80226492&x-zp-page-request-id=f14ab29fd9c84c6987a2d1a82d7259ab-1557219520461-956404

# import requests
# import json
# url='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&=0&_v=0.80226492&x-zp-page-request-id=f14ab29fd9c84c6987a2d1a82d7259ab-1557219520461-956404'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res = requests.get(url,headers=head)
# p=res.content.decode('utf-8')
# aa = json.loads(p)
# f=open('b.txt','w+',encoding='utf-8')
# for  i in range(0,90):
#     b1=aa['data']['results'][i]['company']['name']
#     b2=aa['data']['results'][i]['jobName']
#     b3=aa['data']['results'][i]['salary']
#     b4=aa['data']['results'][i]['city']['display']
#     b5=aa['data']['results'][i]['eduLevel']['name']
#     f.write("{},".format(b1))
#     f.write("{},".format(b2))
#     f.write("{},".format(b3))
#     f.write("{},".format(b4))
#     f.write("{}".format(b5))
#     f.write('\n')
# f=open('b.txt','r',encoding='utf-8')
# a=f.readlines()
# import pymysql
# import xlwt
# ww=xlwt.Workbook('a.xls')
# sheet=ww.add_sheet('zhilian')
# c=["公司ID","岗位名称","薪资","公司地点","学历"]
# for k in range(len(c)):
#     sheet.write(0,k,c[k])
# for l in range(0,len(a)):
#     bb=a[l].split(',')
#     for a1 in range(len(c)):
#         sheet.write(l+1,a1,bb[a1])
# ww.save('a.xls')
# conn=pymysql.connect(host='192.168.0.87',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use test')
# m.execute('create table zhilian(公司ID  char(45),岗位名称 char(35),薪资 char(15),公司地点 char(10),学历 char(10))')
# for j in range(0,len(a)):
#     bb=a[j].split(',')
#     m.execute('insert into zhilian values("{}","{}","{}","{}","{}");'.format(bb[0],bb[1],bb[2],bb[3],bb[4]))


# import requests
# import re
# for q in range(52500,52514):
#     url='https://www.fabiaoqing.com/bqb/detail/id/{}.html'.format(q)
#     head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
#     res = requests.get(url,headers=head)
#     p=res.content.decode('utf-8')
#     patt=re.compile(r'<img class="bqbppdetail lazy" data-original="http://(.*?).jpg" title="(.*?)"')
#     c=patt.findall(p)
#     for i in c:
#         j=r"https://{}.jpg".format(i[0])
#         aa = requests.get(j)
#         hh = aa.content
#         with open(r'C:\Users\weit\Desktop\tupian1\{}.jpg'.format(i[1]),'wb') as f:
#             f.write(hh)



# import requests
# import random
# import jsontime
# #
# import
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



# import requests
# import re
# class pc():
#     def qqq(self):
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
#         return head
#     def sed(self,x,j):
#      url='http://www.skycn.com/soft/liaotian_{}.html'.format(j)
#      res = requests.get(url,headers=head)
#      p = res.content.decode('utf-8')
#      return p
#     def gl(self,p,head):
#         a=0
#         h=re.compile(r' <a href="(.*?)" class="soft-list-dl" dlcount="(.*?)" monkey="downsoft" title="(.*?)">高速下载</a>',re.S)
#         hh=h.findall(p)
#         for i in hh:
#             g=r"{}".format(i[0])
#             msg = requests.get(g,headers=head)
#             hhh=msg.content
#             with open (r'C:\Users\weit\Desktop\222\{}.exe'.format(i[2]),'wb' ) as f:
#                f.write(hhh)
#             a=a+1
# for j in range(8,42):
#     fr=pc()
#     head=fr.qqq()
#     p=fr.sed(head,j)
#     bb=fr.gl(p,head)

# import os
# a=os.listdir()
# c=0
# for i in a:
#     b=os.path.splitext(i)
#     if b[1]==".py":
#         print(b )
#         c=c+1
# print(c)


# import xlwt
# a=xlwt.Workbook('a.xls')
# sheet=a.add_sheet('hello')
# f=open('a.txt','r',encoding='utf-8')
# b=f.readlines()
# for i in range(len(b)):
#     c=b[i].split(',')
#     for k in range(len(c)):
#         sheet.write(i,k,c[k])
# f.close()
# a.save('a.xls')

# import  os
# import re
# p=os.listdir()
# q=','.join(p)
# a=re.compile(",(.*?).py")
# aa=a.findall(q)
# for i in range(len(aa)):
#     b=aa[i].split(',')
#     print('{}.py'.format(b[-1]))


# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}x{}={}'.format(j,i,i*j),end='\t')
#     print()




# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('192.168.0.97',3000))
# sock.listen(4)
# while True:
#     a,b=sock.accept()
#     aa=b.recv(1024)
#     print(aa.decode('utf-8'))
#     bb='welcome'
#     a.send(bb.encode('utf-8'))





# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sock.bind(('192.168.0.97',3000))
# a,b=sock.recvfrom(1024)
# print(a.decode('utf-8'))
# bb='welcome'
# sock.sendto(bb.encode('utf-8'),b)


# import os
# # import xlwt
# # a=os.chdir(r"C:\Users\weit\Desktop\aa")
# # for i in range(51):
# #     f=open('{}.txt'.format(i),'w+',encoding='utf-8')
# #     f.write('{}:{},{}'.format('wo','你真帅','你真好'))
# #     f.write('\n')
# #     f.write('{}:{},{}'.format('ni','你不好','你不帅'))
# # for j in range(51):
# #     os.popen(r"pict  C:\Users\weit\Desktop\aa\{}.txt > C:\Users\weit\Desktop\bb\{}.xls".format(j,j))




# import random
# import xlwt
# import xlrd
# f=xlwt.Workbook('a.xls')
# sheet=f.add_sheet('aa')
# name=['小米','小王','小明','小刚','小李','小石']
# for j in range(4):
#     random.shuffle(name)
#     sheet.write(2,j+4,'{}'.format(name[j]))
#     random.shuffle(name)
#     sheet.write(3,j+4,'{}'.format(name[j]))
#     random.shuffle(name)
#     sheet.write(4,j+4,'{}'.format(name[j+1]))
#     random.shuffle(name)
#     sheet.write(5,j+4,'{}'.format(name[j+1]))
# f.save(r'C:\Users\weit\Desktop\{}.xls'.format('a'))
#
# ff=xlrd.open_workbook(r'C:\Users\weit\Desktop\a.xls')
# sheet=ff.sheets()[0]
# q=['今天','明天','后天']
# for qq in q:
#     a = random.randint(2, 5)
#     a1 = sheet.row_values(a)
#     b = random.randrange(4, 7)
#     print('{}{}请吃饭'.format(a1[b],qq))


# import random
# a=['A',2,3,4,5,6,7,8,9,10]+['J','Q','K']
# a1=[]
# for i in range(4):
#     for i1 in a:
#         a1.append(i1)
# # print(len(a1))
# while True:
#     b = ['小宋', '小刘', '小张', '小吴']
#     random.shuffle(b)
#     b1=input("{}选牌".format(b[0]))
#     b1=int(b1)
#     random.shuffle(a1)
#     q1=a1[b1-1]
#     print("你要和谁比")
#     print(b[1::])
#     b2=input(">>")
#     if b2 in b:
#         b3=input("{}选牌".format(b2))
#         b3=int(b3)
#         random.shuffle(a1)
#         q2=a1[b3-1]
#     print('{}的牌是{}'.format(b[0],q1))
#     print('{}的牌是{}'.format(b2,q2))










# 打印打开的网页的标题
# dr.title
# if dr.title == '百度一下，你就知道':
#     print('yes')
# # 打印当前网页的地址
# print(dr.current_url)
# 设置浏览器窗口大小
# dr.set_window_size(400,500)
# 设置浏览器窗口的位置
# dr.set_window_position(500,500)
# 最大化浏览器
# dr.maximize_window()
# 最大化浏览器
# dr.minimize_window()
# 回退
# dr.back()
# # 前进
# sleep(2)
# dr.forward()

# # 打开浏览器
# dr = webdriver.Chrome()
# # 请求要打开的网页
# dr.get('https://www.baidu.com')
# sleep(2)
# dr.get('https://easonhan007.gitbooks.io/selenium-webdriver/content/04/resize_browser.py.html')
# sleep(2)
#  最重要：定位  不论用什么方式定位，都要保护定位的唯一性
#  1：通过id来定位
# dr.find_element_by_id('kw').send_keys('开封大学')
# sleep(2)
# dr.find_element_by_id('su').click()
# 2: 通过name属性
# dr.find_element_by_name('wd').send_keys('开大')
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
# # 3: 通过class属性
# dr.find_element_by_class_name('mnav').click()
# 4 : 根据link_text属性，文本定位
# dr.find_element_by_link_text('hao').click()
# 5 :模糊查询 文本定位 partial_link_text
# dr.find_element_by_partial_link_text('hao').click()
# 6: 根据标签来定位 tag_name
# 7: 根据路径来定位  xpath(路径标记语言）
#8 ：根据css定位
# dr.find_element_by_id('kw').send_keys('开封大学')
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="1"]/h3/a[1]/em').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="pane-news"]/div/ul/li[2]/strong').click()
# dr.find_element_by_css_selector('#s_tab > div > b').click()


# def  t(x):
#     num=0
#     for i in range(x+1):
#         num=num+i
#     return num
#
# a=t(1000)
# print(a)


# import unittest
# """写单元测试用的，写断言用的
#    拿预期结果和实际结果作对比的过程"""
# class aa(unittest.TestCase):
#     def test_1(self):
#         """假设预期结果为1
#         实际结果是2
#         判断预期结果是否等于实际结果"""
#         a=1 # 预期结果
#         # 断言
#         self.assertEqual(a,2)
# if __name__ == '__main__':
#         unittest.main()



# from selenium import  webdriver
# # from selenium import webdriver
# # from time import sleep
# from time import sleep
# dr=webdriver.Chrome()
# dr.get("http://www.baidu.com")
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys("ka")

# import xlwt
# a=xlwt.Workbook('a.xls')
# b=a.add_sheet('111')
# b.write(0,0,"name")
# b.write(0,1,"age")
# b.write(0,2,"cj")
# b.write(1,0,"李三")
# b.write(1,1,20)
# b.write(1,2,90)
# b.write(2,0,"李五")
# b.write(2,1,21)
# b.write(2,2,99)
# a.save('a.xls')


# import pymysql
# c=pymysql.connect(host="192.168.0.87",port=3306,user="root",passwd="123456")
# a=c.cursor()
# a.execute("show databases;")
# a.execute("use test;")
# a.execute('show tables;')
# import xlrd
# b=xlrd.open_workbook('a.xls')
# bb=b.sheets()[0]
# b1=bb.nrows
# b3=bb.ncols
# for i in range(b1):
#     b2=bb.row_values(i)
#     if i==0:
#         a.execute("create table hhh ({} char(10),{} char(10), {} char(10));".format(b2[0],b2[1],b2[2]))
#     else:
#         a.execute('insert into hhh values("{}","{}","{}");'.format(b2[0],b2[1],b2[2]))
# a.execute('desc hhh;')
# aa1=a.fetchall()
# for i in aa1:
#     print(i[0])
# a.execute('select * from hhh;')
# aa=a.fetchall()
# print(aa)
#
# import  pymysql
# a=pymysql.connect(host="192.168.0.87",port=3306,user="root",password="123456")
# b=a.cursor()
# b.execute("show databases;")
# c=b.fetchall()
# b.exceute("use  mysql;")
# print(c)

from selenium import webdriver
from time import sleep
a=webdriver.Chrome()
a.get("https://qzone.qq.com/")
a.switch_to_frame('login_frame')
# a.find_element_by_css_selector('#switcher_plogin').click()
# a.find_element_by_xpath('//*[@id="u"]').send_keys("1678665473")
# sleep(1)
# a.find_element_by_xpath('//*[@id="p"]').send_keys("zwy423510++")
sleep(2)
a.find_element_by_xpath('//*[@id="img_out_1678665473"]').click()
sleep(1)
a.find_element_by_xpath('//*[@id="aMyFriends"]').click()
sleep(1)
a.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/ul/li[1]/span').click()
a.find_element_by_xpath('//*[@id="mecarewho_list"]/li[5]/div[2]/div[1]/a/img').click()
a.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[4]/a').click()
b=["踏着祥云踩着梦 那是我的盖世英雄。",
   "其实你根本就不是我喜欢的类型 只是碰巧撞进了我的心。",
 "别人口中的你有多坏我从未相信。",
"不愿意醒来时，台灯投射在墙上只有我孤独的身影。",
   "爱是一种遇见，不能等待，也不能准备",
   "女人总爱找茬跟男人闹，是希望闹过之后他能心存歉意，对她更好些。进入恋爱之前，女人都可以淑女，一旦自认抓牢了男人，她开始对他刁蛮任性。她不是脾气不好，她只是用“发脾气”来证明自己的拥有。当女人开始生出折腾他的欲望，说明，她真的爱上了",
   "世界这么大，能遇见，不容易。",
   "我打算爱你很久很久 没有想要放弃的念头",
   "找不到坚持下去的理由，那就找一个重新开始的理由，生活本来就这么简单。避免失望的最好办法，就是不寄希望于任何人、任何事。人生是一场相逢，又是一场遗忘，最终我们都会成为岁月里的风景。",
   "你的微笑像是子弹先是击穿我的胸膛 再射入心脏。"]
for i in range(len(b)):
    a.find_element_by_xpath('/html/body').send_keys("{}".format(b[i]))
    sleep(2)
    a.find_element_by_xpath('//*[@id="btnPostMsg"]')
