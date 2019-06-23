#!/usr/bin/python
#-*- coding:utf-8 -*-
#print("hello",123,1234232)
#a=input('请输入密码：')
#print(a)
#a=1
#b=2
#print(a,b)
#a,b,c=1,2,4
#print(a,b+3)
#a=123.12
#c=a+b
#print(c,type(c))
#a='qwesaasdwqe'
#print(a[3::6 ])
#='aweqerweft'
#b=a.replace('a','')
#=a.split('we')
#='='.join(a)
#rint(type(c),c)
#b='ad{a1}adaw{b2}'.format(a1=90,b2='aaa')
#print(b)
#a='hello %s,我今年%s岁了'
#b=a % (')
#print(b)
 #a='awqedas'
#b=a.index('w')
#print(b)
#a='awqaedaas'
#b=a.count('a')
#print(b)·
#bowen=[1,2,3,'大','小','多']
# bowen.sort()
#  aa=[23,42,7,3,4,5]
#  print(aa[:3])
# aa.sort()
# aa.reverse()
# import copy
# a=[1,2,3]
# bowen=['大',a,'小','多']
# ff=copy.deepcopy(bowen)
# bowen.append(100)
# a.append(1222)
# print(bowen)
# print(ff)
# a=(1,2,3)
# b=a.index(2)
# print(b)
# aa = [23, 42, 7, 3, 4, 5]
# print(aa[2:])
# a={'name','1','xiao','nasdw','adad'}
# b={'1','2','312'}
# c = b-a
# print(c)
# a=1222
# b='sad'
# a=str(a)
# print(a+b)

# if a  >= 90 :
#     print('优秀')
# elif  a >= 80 and a < 90:
#     print('良好')
# elif  a >= 60 and a < 80:
#     print('一般')
# else:
#     print('差劲')
# a=input('输入数字')
# a = int(a)
# if  a%2==0:
#     if  a%3==0:
#         print("hello world")
#     if  a%3!=0:
#         print('hello')
# elif  a%3==0:
#     print('world')
# else:
#     print(123)
# i=input("输入")
# i=int(i)
#  a = 0
# b=100
# for i in range(100):
#  if  i%2==0:
#    a=a-i
#  elif i%2==1:
#    a=a+i
# print(a)
# for i in range(3):
#     for j in range(4):
#         print('aaa')
#     print('bbb')

#


#质数之和
# b=input('输入')
# # b=int(b)
# # a=0
# # for i in range(2,b):
# #     for j in range(2,b):
# #          if i%j==0:
# #            break
# #     if i==j:
# #          a=a+i
# # print(a)
#因数之和等于本身
# for i in range(2,1001):
#     a=0
#     for j in range(1,1000):
#       if j<i and i%j==0:
#         a=a+j
#     if a==i:
#      print(i)

# b='abdxadadd'
# b.replace('a','abc')
#购物车
# a=input('输入金额')
# a=int(a)
# b=[('1','name','电脑','price','1999'),('2','name','鼠标','price','10'),('3','name','游艇','price','20'),('4','name','美女','price','998')]
# print(b)
# d = []
# while True:
#    c=input("输入产品号1,2,3,4,选购完成输入(5)\n")
#    c=int(c)
#    if c==1:
#        d.append(b[0][2])
#        d.append(b[0][4])
#        print('{}加入购物车成功'.format(b[0][2]))
#    elif c==2:
#        d.append(b[1][2])
#        d.append(b[1][4])
#        print('{}加入购物车成功'.format(b[1][2]))
#    elif c==3:
#        d.append(b[2][2])
#        d.append(b[2][4])
#        print('{}加入购物车成功'.format(b[2][2]))
#    elif c==4:
#        d.append(b[3][2])
#        d.append(b[3][4])
#        print('{}加入购物车成功'.format(b[3][2]))
#    else:
#      break
# e=input('是够查看购物车:(y)(n)')
# if e=='y':
#    print('购物车有:{}'.format(d))
#    while True:
#        v=input('输入序号移除商品，退出(n)\n')
#        if v != 'n':
#         v=int(v)
#         d.remove(d[v-1])
#         d.remove(d[v-1])
#         print("购物车:{}，退出(no)".format(d))
#        else:
#            if v == 'n':
#                break
#            print("购物车:{}".format(d))
# r=input("是否购买(y)(n)")
# if  r=='y':
#   y=[]
#   k=0
#   for i in range(1,len(d)):
#       if i%2==1:
#           y.append(d[i])
#   l=[int(l) for l in y]
#   for j in range(0,len(y)):
#     k = k +l[j]
#   if a >= k :
#       print("购买成功,余额剩余{}元".format((a-k)))
#   elif  a< k:
#       print("余额不足,余额剩余{}元,商品需要{}元".format(a,k))
#       while True:
#           o=input('是否充值:(y)(n)')
#           if o=='y':
#               p=input('充值金额')
#               p=int(p)
#               a=a+p
#               print('充值{}元成功,余额有{}元'.format(p,a))
#               print('继续充值输入(y)，退出充值输入(n)')
#           if o=='n':
#               break
#   p=input("是否购买(y)(n)")
#   if p=='y':
#       if a >= k:
#           print("购买成功,余额剩余{}元".format((a-k)))
#       elif a < k:
#           print("余额不足,余额剩余{}元".format(a))













# a = [1,2,3,4,5,6,1,2,3,4,5,6]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# a=input("输入三边")
# a=a.split(',')
# b=[int(i)  for i in a]
# if b[0]+b[1] > b[2] and b[0]+b[2] > b[1] and b[1]+b[2] > b[0]:
#     print("这是一个三角形")
#     if b[0]**2+b[1]**2 == b[2]**2 or b[0]**2+b[2]**2 == b[1]**2 or b[1]**2+b[2]**2 == b[0]**2:
#         print("这是一个直角三角形")
#     elif b[0]**2+b[1]**2 > b[2]**2 and b[0]**2+b[2]**2 > b[1]**2 and b[1]**2+b[2]**2 > b[0]**2:
#         print("这是一个锐角三角形")
#     elif b[0]**2+b[1]**2 < b[2]**2 or b[0]**2+b[2]**2 < b[1]**2 or b[1]**2+b[2]**2 < b[0]**2:
#         print("这是一个钝角三角形")
# else:
#     print("这不是一个三角形")


# from day1 import asd
# #import random
# asd()






# f=open('a.txt','r')
# b=f.readlines()
# for i in range(len(b)):
#     if b[i].startswith('abc'):
#         print(b[i])
# f.close()

# f=open('b.txt','w+',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,10):
#         if j <= i:
#             f.write("{}x{}={},".format(i,j,i*j))
#             if j==i:
#                  f.write('\n')
# f.close()

# def aa():
#     global a
#     a=123
#     print(a)
# aa()
#
#
#
# print(a)

# a=0
# for i in range(2,101):
#     for j in range(2,101):
#         if i%j==0:
#             break
#     if i==j:
#      a=a+j
# print(a)

# a=[1,2,3,4,5,6,7,7,6,7,6]
# a.sort()
# a=a[::-1]
# b=a.count(max(a))
# c=[]
# for i in range(b):
#     c.append(max(a))
#     a.remove(max(a))
# print(c)
# q=[]
# d=a.count(max(a))
# for i in range(d):
#     q.append(max(a))
# print(q)


# import xlwt
# f=xlwt.Workbook
# sheet=f.add_sheet('test')
# def asd(a,b,c):
#     a=list(a)
#     if b+c >= len(a):
#         for i in range(b,len(a)):
#             a.remove(a[b])
#         print(a)
#     else:
#         for j in range(b,b+c):
#             a.remove(a[b])
#         print(a)
# asd([1,2,3,4,5,6,7,8],2,3)


# def asd(a):
# # #     a=list(a)
# # #     c=[]
# # #     for  i in a:
# # #         if i not in c:
# # #             c.append(i)
# # #     print(c)
# # # asd([1,2,3,4,5,6,1,2,3,4,5])

# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('aa.xls')
# s=f.sheets()[0]
# a=s.nrows
# print(a)
# b=s.ncols
# print(b)
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in range(10):
#     sheet.write(a+i,0,'qwe')
# new_f.save('aa.xls')





# 连接数据库
# import  pymysql
# conn = pymysql.connect(host='192.168.0.87',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
#创建游标
# m=conn.cursor()
#执行sql语句  显示数据库的个数
#m.execute('create database python_test1;')
# m.execute('show databases;')
# print(m.fetchall())
# m.execute('use python_test1;')
#m.execute('create table biao(name char(20),age int,sex char(20));')
#m.execute('show tables')
# 读取上一个sql语句的结果
# for i in range(20):
#     m.execute('insert into biao values("小比","{}","女");'.format(i))
# m.execute('delete from biao;')
# b=m.fetchall()
# b=m.fetchmany(2)
#每次只读取一条数据
# b=m.fetchone()
# c=m.fetchone()
# print(b)
# conn.close()#断开数据库
#b=m.fetchmany(3)#默认读取一个数据，传入的参数是几，就是读取几行数据

# import xlrd
# import  pymysql
# conn = pymysql.connect(host='192.168.0.87',
#                        port=3306,
#                        user='root',
#                        passwd='123456',
#                        charset='utf8')
# m=conn.cursor()
# m.execute('use python_test1;')
# f=xlrd.open_workbook('cj.xls')
# sheet=f.sheets()[0]
# for i in range(sheet.nrows):
#     b=sheet.row_values(i)
#     if i ==0:
#         m.execute('create table  cj({} char(20),{} int,{} char(20),{} char(20),{}char(20));'.format(b[0],b[1],b[2],b[3],b[4]))
#     else:
#         m.execute('insert into cj values("{}","{}","{}","{}","{}");'.format(b[0],b[1],b[2],b[3],b[4]))
# m.execute('select * from cj;')
# c=m.fetchall()
# print(c)

# import  pymysql
# conn = pymysql.connect(host='192.168.0.87',
#                        port=3306,
#                        user='root',
#                        passwd='123456',
#                        charset='utf8')
# m=conn.cursor()
# m.execute('use python_test1;')
# f = open('a.txt','r')
# a=f.readlines()
# for i in range(len(a)):
#     b=a[i].split(',')
#     if i == 0:
#        m.execute('create table  aa({} char(20),{} char(20),{} int,{} char(20),{} char(20),{}char(20));'.format(b[0],b[1],b[2],b[3],b[4],b[5]))
#     else:
#        m.execute('insert into aa values("{}","{}","{}","{}","{}","{}");'.format(b[0],b[1],b[2],b[3],b[4],b[5]))
# m.execute('select * from aa;')

# 从数据库中提取数据到txt中
# import  pymysql
# f=open('bb.txt','w+',encoding='utf-8')
# conn = pymysql.connect(host='192.168.0.87',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use python_test1;')
# m.execute('desc aa')
# d=m.fetchall()
# ff=[]
# for i in range(len(d)):
#     ff.append(d[i][0])
# ff=' '.join(ff)
# f.write(ff)
# f.write('\n')
# m.execute('select * from aa;')
# c=m.fetchall()
# b=len(c)
# m.execute('select * from aa;')
# for i in range(b):
#     e = m.fetchone()
#     for j in range(0,len(d)):
#         f.write('{} '.format(e[j]))
#         if j == len(d):
#             f.write(e[j])
#             f.write('\n')
# f.close()

#从数据库中提数据到Excel中
# import xlwt
# import  pymysql
# f=xlwt.Workbook('cc.xls')
# sheet=f.add_sheet('test1')
# conn = pymysql.connect(host='192.168.0.87',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use python_test1;')
# m.execute('desc aa')
# d=m.fetchall()
# for i in range(len(d)):
#     sheet.write(0, i, '{}'.format(d[i][0]))
# m.execute('select * from aa;')
# c=m.fetchall()
# b=len(c)
# m.execute('select * from aa;')
# for q in range(1,b+1):
#     e = m.fetchone()
#     for j in range(len(d)):
#         sheet.write(q,j,'{}'.format(e[j]))
# f.save('cc.xls')

#     # 客户端 基于tcp 的
# import  socket
# while True:
#     # 创建一个套接字（具有发送和接收功能的）
#     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     # 连接服务器
#     sock.connect(('192.168.0.18',3000))
#     # 将 qq当做请求 发送给服务器
#     ee=input(">>>")
#     sock.send(ee.encode('utf-8'))
#     # 接受响应
#     ww=sock.recv(1024)
#     print(ww.decode('utf-8'))
#

# 客户端 基于udp的
# import socket
# while True:
#     s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     host=('192.168.0.121',3000)
#     msg=input(">>>")
#     s.sendto(msg.encode('utf-8'),host)
#     # 接收响应
#     reg=s.recv(1024)
#     print(reg.decode('utf-8'))

# import  socket
# while True:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(('192.168.0.18',3000))
#     ee = input(">>>")
#     sock.send(ee.encode('utf-8'))
#     ww = sock.recv(1024 (ww.decode('utf-8'))


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # s.bind(("192.168.0.87",3000))
# s.listen(4)
# while True:
#     a,b=s.accept()
#     d=a.recv(1024)
#     print(d.decode('utf-8'))
#     c="welcome"
#     a.send(c.encode('utf-8'))
from time import  sleep
from appium import webdriver
# 面向对象
# class  Tim(object):
#     # 初始化属性
#     def __init__(self):
#         self.des = {
#             "platformName": "Android",
#             "platformVersion": "8.1.0",
#             "deviceName": "6286c4da",
#             "appPackage": "com.tencent.tim",
#             "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#             "noReset": "True",
#             "unicodekeyboard": "unicod"
#         }
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
#         sleep(2)
    # def dian_zan(self):
    #     self.a=dr.find_element_by_accessibility_id('好友动态').click()
    #     sleep(2)
    #     dr.find_elements_by_class_name('android.widget.ImageView')[1].click()


# 调用类
# if __name__=='__main__':
#     yasuo=Tim()
#     yasuo.dian_zan()

#     def get_wenzi(self):
#         # a=self.dr.find_element_by_id("com.tencent.tim:id/ivTitleName").text
#         # print(a)
#         self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
#         sleep(1)
#         self.dr.find_element_by_accessibility_id('好友动态').click()
#         sleep(2)
#         # dr.find_elements_by_class_name('android.widget.ImageView')[1].click()
#
#         # 发送物理按键，模拟人点击物理按键
#     def an_jian(self):
#         self.dr.keyevent(4)
#         # 点击返回键
#
# Tim().get_wenzi()
# Tim().an_jian()
# 调用类
#
# if __name__=='__main__':
#     yasuo = Tim()
#     yasuo.get_wenzi()
#     yasuo.an_jian()


"""
电话键

KEYCODE_CALL 拨号键 5
KEYCODE_ENDCALL 挂机键 6
KEYCODE_HOME 按键Home 3
KEYCODE_MENU 菜单键 82
KEYCODE_BACK 返回键 4
KEYCODE_SEARCH 搜索键 84
KEYCODE_CAMERA 拍照键 27
KEYCODE_FOCUS 拍照对焦键 80
KEYCODE_POWER 电源键 26
KEYCODE_NOTIFICATION 通知键 83
KEYCODE_MUTE 话筒静音键 91
KEYCODE_VOLUME_MUTE 扬声器静音键 164
KEYCODE_VOLUME_UP 音量增加键 24
KEYCODE_VOLUME_DOWN 音量减小键 25

控制键

KEYCODE_ENTER 回车键 66
KEYCODE_ESCAPE ESC键 111
KEYCODE_DPAD_CENTER 导航键 确定键 23
KEYCODE_DPAD_UP 导航键 向上 19
KEYCODE_DPAD_DOWN 导航键 向下 20
KEYCODE_DPAD_LEFT 导航键 向左 21
KEYCODE_DPAD_RIGHT 导航键 向右 22
KEYCODE_MOVE_HOME 光标移动到开始键 122
KEYCODE_MOVE_END 光标移动到末尾键 123
KEYCODE_PAGE_UP 向上翻页键 92
KEYCODE_PAGE_DOWN 向下翻页键 93
KEYCODE_DEL 退格键 67
KEYCODE_FORWARD_DEL 删除键 112
KEYCODE_INSERT 插入键 124
KEYCODE_TAB Tab键 61
KEYCODE_NUM_LOCK 小键盘锁 143
KEYCODE_CAPS_LOCK 大写锁定键 115
KEYCODE_BREAK Break/Pause键 121
KEYCODE_SCROLL_LOCK 滚动锁定键 116
KEYCODE_ZOOM_IN 放大键 168
KEYCODE_ZOOM_OUT 缩小键 169

组合键

KEYCODE_ALT_LEFT Alt+Left
KEYCODE_ALT_RIGHT Alt+Right
KEYCODE_CTRL_LEFT Control+Left
KEYCODE_CTRL_RIGHT Control+Right
KEYCODE_SHIFT_LEFT Shift+Left
KEYCODE_SHIFT_RIGHT Shift+Right

基本

KEYCODE_0 按键'0' 7
KEYCODE_1 按键'1' 8
KEYCODE_2 按键'2' 9
KEYCODE_3 按键'3' 10
KEYCODE_4 按键'4' 11
KEYCODE_5 按键'5' 12
KEYCODE_6 按键'6' 13
KEYCODE_7 按键'7' 14
KEYCODE_8 按键'8' 15
KEYCODE_9 按键'9' 16
KEYCODE_A 按键'A' 29
KEYCODE_B 按键'B' 30
KEYCODE_C 按键'C' 31
KEYCODE_D 按键'D' 32
KEYCODE_E 按键'E' 33
KEYCODE_F 按键'F' 34
KEYCODE_G 按键'G' 35
KEYCODE_H 按键'H' 36
KEYCODE_I 按键'I' 37
KEYCODE_J 按键'J' 38
KEYCODE_K 按键'K' 39
KEYCODE_L 按键'L' 40
KEYCODE_M 按键'M' 41
KEYCODE_N 按键'N' 42
KEYCODE_O 按键'O' 43
KEYCODE_P 按键'P' 44
KEYCODE_Q 按键'Q' 45
KEYCODE_R 按键'R' 46
KEYCODE_S 按键'S' 47
KEYCODE_T 按键'T' 48
KEYCODE_U 按键'U' 49
KEYCODE_V 按键'V' 50
KEYCODE_W 按键'W' 51
KEYCODE_X 按键'X' 52
KEYCODE_Y 按键'Y' 53
KEYCODE_Z 按键'Z' 54
"""

