#!/usr/bin/python
#-*- coding:utf-8 -*-
# 发邮件
# import smtplib
# import email.mime.multipart as aa
# import email.mime.text as bb
# cc=aa.MIMEMultipart()
# cc['Subject']='你好啊'
# cc['From']='weitao_423510@163.com'
# cc['To']='1678665473@qq.com'
# dd=""""你好呀，很高兴认识你"""
# aaa=bb.MIMEText(dd)
# cc.attach(aaa)
# att1 = bb.MIMEText(open('day1.py', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="day1.py"'
# ee=smtplib.SMTP_SSL('smtp.163.com',465)
# ee.login('weitao_423510@163.com','a423510')
# ee.sendmail('weitao_423510@163.com','1678665473@qq.com',cc.as_string())
# ee.close()
#

# def  asd(a,b):
#     a=[int(i) for i in a]
#     b=int(b)
#     for j in a:
#         for q in a:
#          if j+q==b and j!=q and j > q:
#              print(j,q,b)
# asd([0,1,2,3,4,5,6,7,8,9,10,11,12],12)

# import  xlwt
# f=xlwt.Workbook('a1.xls')
# sheet=f.add_sheet('test')
# ff=open('a.txt','r')
# aa= ff.readlines()
# for i in range(len(aa)):
#     b=aa[i].split(',')
#     for j in range(4):
#         sheet.write(i,j,b[j])
# f.save('a1.xls')
# def asd(x,y,q):
#    for x in range(101):
#         for y in range(101):
#             for q in range(101):
#                 if 2*x+1*y+0.5*q==100  and x+y+q==100:
#                     print(x,y,q)
#
# asd('x','y','q')

# import os
# print(os.getcwd())
# b=os.popen('ipconfig')
# print(b.read())
# os.removedirs(r'aaa\bbb\ccc')

# import paramiko
# a=paramiko.SSHClient()
# a.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# a.connect(hostname='192.168.0.87',port='22',username='root',password='123456')
# b=a.exec_command('ls -al /home')
# print(b[1].read().decode())

# import paramiko
# aa=paramiko.Transport(('192.18.0.87',22))
# aa.connect(username='root',password='123456')
# c=paramiko.SFTPClient.from_transport(aa)
# c.get()


# import socket
# s=socket.socket()
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.87',3000))


# import xlrd
# f=xlrd.open_workbook(r'C:\Users\weit\Desktop\2019-1-12日报位涛.xlsx')
# sheet=f.sheets()[0]
# c=sheet.row_values(0)
# print(c)

# import time
# a=input(">>>")
# a=a.split('-')
# b=[int(i) for i in a]
# if b[0]%4==0 and  b[0]%100!=0:
#     print('闰年')
# elif b[0]%100==0:
#     print('世纪年')
# else:
#     print('普通年')
# c=time.strptime('{}-{}-{}'.format(b[0],b[1],b[2]),'%Y-%m-%d')
# print('第{}天'.format(c[-2]))
# print('星期{}'.format(c[-3]+1))


# a=input('>>>')
# a=int(a)
# b=[str(i) for i in range(10)]+['a','b','c','d','e','f']
# c=''
# while True:
#     q = a%16
#     c = b[q] + c
#     a = a //16
#     if a == 0:
#         break
# print(c)

# import smtplib
# import email.mime.multipart as  aa
# import email.mime.text as bb
# cc= aa.MIMEMultipart()
# ww=['1678665473@qq.com','572086992@qq.com','songzf_1996@163.com']
# cc['Subject']=('nihao')
# cc['From']=('weitao_423510@163.com')
# cc['To']=','.join(ww)
# txt=""""nihaoa"""
# aaa=bb.MIMEText(txt)
# cc.attach(aaa)
# ee=bb.MIMEText(open('day1.py','rb').read(),'base64','utf-8')
# ee["content-type"]='application/octet-stream'
# ee['Content-Disposition']='attachment.filename"nihao"'
# cc.attach(ee)
# dd=smtplib.SMTP_SSL('smtp.163.com',465)
# dd.login('weitao_423510@163.com','a423510')
# dd.sendmail('weitao_423510@163.com',ww,cc.as_string())
# dd.close()
# for i in range(100):
#     import smtplib
#     import email.mime.multipart as  aa
#     import email.mime.text as bb
#     cc=aa.MIMEMultipart()
#     cc['Subject']=('hello')
#     cc['From']=('1678665473@qq.com')
#     cc['To']=('b2b_thailand@samsung.com ')
#     txt=""""ria,nm"""""
#     aaa=bb.MIMEText(txt)
#     cc.attach(aaa)
#     dd=smtplib.SMTP_SSL('smtp.qq.com',465)
#     dd.login('1678665473@qq.com','qxkawwcrymxzccgd')
#     dd.sendmail('1678665473@qq.com','b2b_thailand@samsung.com',cc.as_string())
#     #dd.sendmail('weitao_423510@163.com','1678665473@qq.com',cc.as_string())
#     dd.close()

# 服务器 基于tcp的
# import socket
# while True:
#     s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     s.bind(('192.168.0.76',3000))
#     client,addr=s.recvfrom(1024)
#     # reg=client.recv(1)
#     print(client.decode('utf-8'))
#     msg='welcome'
#     s.sendto(msg.encode('utf-8'),addr)

# def aaa():
#     a=0
#     for i in range(101):
#         a=a+i
#     print(a)
# aaa()

# a=16
# b=[str(i) for i in range(10)]+['a','b','c','d','e','f']
# c=''
# while True:
#     d = a % 16
#     c = c + b[d]
#     a = a // 16
#     if a == 0:
#        break
# print(c[::-1])


# def asd(x):
#     x=input(">>>")
#     x=int(x)
#     a=0
#     for i in range(2,x+1):
#        for j in range(2,x+1):
#            if i%j==0 :
#               break
#        if  i==j:
#           a=a+i
#     print(a)
# asd('x')

# import re
# a='vas121341v23q35jbj5b23j7233bkj2b675'
# b=re.compile('[0-9][0-9]+')
# c=b.findall(a)
# print(c)
# for i in c:
#   if  int(i[0])==int(i[1])-1:
#       print(i)

# a='12354'
# a=a[::-1]
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j) == a[i]:
#             c=j*10**i
#             b=b+c
# print(b)

# def asd(x,y,z):
# #     for i in range(z):
# #         if z <= len(x):
# #            x.remove(x[y])
# #         elif z > len(x):
# #             for i in range(len(x)-y):
# #               x.remove(x[y])
# #     print(x)
# #
# # asd([1,2,3,4,5,6,7,8],1,10)

# for i in range(1,10):
#     for j in range(1,10):
#         if  j <= i:
#             print('{}x{}={}'.format(i,j,i*j),end='\t')
#     print()

# import  time
# a=input(">>>")
# a=a.split('-')
# b=[int(i) for i in a]
# if b[0]%4==0 and b[0]%100!=0:
#     print("润年")
# elif b[0]%100==0:
#     print("世纪年")
# else:
#     print("普通年")
# b=time.strptime('{}-{}-{}'.format(b[0],b[1],b[2]),'%Y-%m-%d')
# print('星期{}'.format(b[6]+1))
# print('第{}天'.format(b[7]))