# import re
# import requests
# import time
#
# songID = []
# songName = []
# for n in range(0,1):
#     url = 'http://www.htqyy.com/top/musiclist/hot?pageIndex={}&pageSize=20'.format(n)
#     print(url,end='\n')
#     html = requests.get(url)
#     resultID = re.findall('sid="(.*?)">',html.text)
#     resultName =re.findall('<a href="/(.*?)/(.*?)" target="play" title="(.*?)" sid="(.*?)">',html.text)
#     songID.extend(resultID)
#     songName.extend(resultName)
# print(songID)
# print(songName)
#
# for m in range(0,len(songID)):
#     songUrl='http://f2.htqyy.com/play7/{}/mp3/1'.format(songID[m])
#     print(songUrl,end='\n')
#     print('正在下载第{}首'.format(m+1))
#     response = requests.get(songUrl).content
#     f = open("D:\\music\\{}.mp3".format(songName[m][2]),"wb")
#     f.write(response)
#     f.close()




#  爬虫：模仿浏览器，根据自己制定的规则批量下载指定的资源
# 分类：聚焦爬虫，搜索爬虫
# 聚焦爬虫：只针对某个网站进行爬虫
# 搜索爬虫：针对全网络进行爬取(搜索引擎）
# 模仿浏览器的模块：requests,urllib,urllib2,3,scrapy
# 过滤文件的内容，过滤网页资源：re,BeautifulSoup,xpath
# 对服务器进行请求，将得到的响应数据过滤并保存
# 压力 ： 开发人员：反爬：防止爬虫程序，批量下载资源
# 常见的反爬机制
#   1：通过请求headers判断
#   2：ip地址被封   频繁的转换公网ip(西刺代理)
#   3：验证码
#   4：数据混淆
#   5：行为分析
# 爬虫本身不违法，做商业活动就违法了
# 成本和你的付出是一样的
# 网页：静态网页：所有的资源都在html文件上
#       动态网页：资源不再html上（ ajax(XHR)    JavaScript(js) ） 里面是 json
#  json：是一种轻量级的数据传输格式
#   将字符串格式转化成字典
#  qqq = json.loads(hhh)
#   将字典转换成字符串
#  uuu = json.dumps(qqq)









# import requests
# import re
# class FreeBuf():
#     def send_请求(self,j):
#         url='https://www.freebuf.com/page/{}'.format(j)
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
#         }
#     #  发送请求
#         res = requests.post(url,headers=head)
#     # 读取结果 1:text 以文本的方式接收 2:content(url)以字节方式接收，字节
#     #     print(res.text)
#         hh=res.content.decode('utf-8')
#         return hh
#     def guolv(self,x):
#         cc=[]
#         patt=re.compile('<div class="news-info">(.*?)<dd>',re.S)
#         aa=patt.findall(x)
#         for i in aa:
#             bb=re.findall('title="(.*?)"',i)
#             cc.extend(bb)
#         return cc
#     # 爬虫第三步：保存
#     def save(self,y):
#         with open("q.txt","a",encoding="utf-8") as f:
#             for i in y:
#                 f.write(i+"\n")
# fr = FreeBuf()
# for j in range(1,5):
#     hh=fr.send_请求(j)
#     yy=fr.guolv(hh)
#     fr.save(yy)



# import requests
# import re
# for i in range(1,10):
#     url = 'https://www.freebuf.com/page/{}'.format(i)
#     res = requests.post(url)
#     hh = res.content.decode('utf-8')
#     patt=re.compile('<div class="news-info">(.*?)<dd>',re.S)
#     aa = patt.findall(hh)
#     cc = []
#     for i in aa:
#                 bb=re.findall('title="(.*?)"',i)
#                 cc.extend(bb)
#     with open("q.txt", "a", encoding="utf-8") as f:
#                 for i in cc:
#                     f.write(i+"\n")
#

#!/usr/bin/python
#-*- coding:utf-8 -*-
# import requests
# import re
# url='http://movie.douban.com/top250'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res = requests.post(url,headers=head)
# html = res.content.decode('utf-8')
# print(html)
# a=[]
# bb = re.compile('<img width="100" alt=(.*?)')
# aa = bb.findall(html)
# a.extend(aa)
# cc = re.compile(r'src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/(.*?).webp"')
# dd = cc.findall(html)
# b=0
# for i in dd:
#     j='https://img3.doubanio.com/view/photo/s_ratio_poster/public/'+ i + '.webp'
#     msg = requests.get(j,headers=head)
#     hh = msg.content
#     with open('{}.jpg'.format(a[b]),'wb') as f:
#         f.write(hh)
#     b += 1



# import re
# import requests
# url='http://movie.douban.com/top250'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res = requests.get(url,headers=head)
# p=res.content.decode('utf-8')
# patt=re.compile(r'<img width="100" alt="(.*?)" src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class="">')
# c=patt.findall(p)
#
# for i in c:
#     j=r"https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg".format(i[1],i[2])
#     aa = requests.get(j)
#     hh = aa.content
#     with open(r'C:\Users\weit\Desktop\tupian\{}.jpg'.format(i[0]),'wb') as f:
#         f.write(hh)


# 小小表情包
# import re
# import requests
# for q in range(52500,52514):
#     url='https://www.fabiaoqing.com/bqb/detail/id/{}.html'.format(q)
#     head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
#     res = requests.get(url,headers=head)
#     p=res.content.decode('utf-8')
#     patt=re.compile(r'<img class="bqbppdetail lazy" data-original="http://(.*?).jpg" title="(.*?)"')




# a=['a',[1,2,3],'b','c','d','e','f','g']
# # a.sort()
# # a.reverse()
# b=a.copy()
# import copy
# c=copy.deepcopy(a)
# a[1].append(4)
# print(b)

# a={'a':1,'b':2}
# b=a.items()
# print(b)

# import xlwt
# a=xlwt.Workbook('q.xls')
# sheet=a.add_sheet('women')
# sheet.write(0,0,'qunima')
# a.save('q.xls')

# from xlutils.copy import copy
# import xlrd
# f=xlrd.open_workbook('aa.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# a=f.sheets()[0]
# b=a.nrows
# c=a.ncols
# sheet.write(b,c,12345)
# new_f.save('a1.xls')


# from xlutils.copy import copy
# import xlrd
# f=xlrd.open_workbook('aaa.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# a=f.sheets()[0]
# b=a.nrows
# c=a.ncols
# sheet.write(b,c,123)
# new_f.save('a2.xls')

# import time
# # a=time.localtime()
# # b=time.strftime('%Y_%m_%d' '%H:%M:%S')
# # c=time.strptime('{}-{}-{}'.format(2012,3,12),'%Y-%m-%d')
# a=(2019,4,5,18,23,45,12,21,34)
# b=time.mktime(a)
# print(b)

# import pymysql
# conn=pymysql.connect(host='192.168.0.87',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use test')
# m.execute('show tables')
# a=m.fetchall()
# print(a)

# import os
# b=os.getcwd()
# print(b)

# import pymysql
# conn=pymysql.connect(host='192.168.0.87',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use test')
# m.execute('desc cj')
# a=m.fetchall()
# c=[]
# for i in range(len(a)):
#     c.append(a[i][0])
# f=open('q.txt','w+',encoding='utf-8')
# for j in range(len(c)):
#     f.write("{} ".format(c[j]))
# f.write('\n')
# m.execute('select * from cj;')
# d=m.fetchall()
# m.execute('select * from cj;')
# for w in range(len(d)):
#     ff=m.fetchone()
#     for e in range(len(ff)):
#         f.write("{}  ".format(ff[e]))
#     f.write('\n')
# f.close()



# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.18',3000))
# s.listen(4)
# while  True :
#     a,b=s.accept()
#     reg=a.recv(1024)
#     print(reg.decode('utf-8'))
#     msg='welcome'
#     a.send(msg.encode('utf-8'))

# a='1232'
# b=a[::-1]
# c=0
# for i in range(len(a)):
#     for j in range(10):
#         if b[i]==str(j):
#             d=j*10**i
#             c+=d
# print(c)
# w=input(">>>")
# a=w.split(',')
# a=[1,2,3,4,5,6,7,8,9,9,8,8,8,8,8,8,8,7,6,5]
# b=a.count(max(a))
# c=[]
# q=[]
# for i in range(b):
#     c.append(max(a))
#     a.remove(max(a))
# d=a.count(max(a))
# for j in range(d):
#     q.append(max(a))
# print(c)
# print(q)
# import xlwt
# f=open('a.txt','r')
# a=f.readlines()
# print(a)
# ff=xlwt.Workbook('ww.xls')
# sheet=ff.add_sheet('test')
# for i in range(len(a)):
#     b=a[i].split(',')
#     print(b)
#     for j in range(len(b)):
#         sheet.write(i,j,b[j])
# ff.save('ww.xls')



# import socket#tcp
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.87',3000))
# s.listen(3)
# while True:
#     a,b=s.accept()
#     c=a.recv(1024)
#     print(c.decode('utf-8'))
#     d='hello'
#     a.send(d.encode('utf-8'))
#
#
# import socket #tcp
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.connect(('192.168.0.87',3000))
# msg='hello'
# s.send(msg.encode('utf-8'))
# a=s.recv(1024)
# print(a.decode('utf-8'))
#
#
#
# import socket#udp
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.0.87',3000))
# while  True:
#     a.b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     c='nihao'
#     s.send(c.encode('utf-8'),b)
#
#
#
#
# import socket #udp
# while Ture:
#     s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     host=('192.168.0.87',3000)
#     a='jjj'
#     s.sendto(a.encode('utf-8'))
#     b=s.recv(1024)
#     print(b.decode('utf-8'))


# import paramiko
# a=paramiko.SSHClient()
# a.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# a.connect(hostname='192.168.0.87',port=22,username='root',password='123456')
# b,c,d=a.exec_command('ls -al /home')
# print(c.read().decode('utf-8'))
# a.close()

# import paramiko
# a=paramiko.Transport(('192.168.0.87',22))
# a.connect(username='root',password='123456')
# b=paramiko.SFTPClient.from_transport(a)
# b.get()
# b.put()
# a.close()
