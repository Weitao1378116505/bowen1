#!/usr/bin/python
#-*- coding:utf-8 -*-


# def asd():
#     print('hello')
# asd()
# if __name__=='__main__':
#     for i in range(10):
#          print(i)

# try:
#     a=123+123
#     print(a)
# except Exception as e:
#     print(e)
# else:
#     print('123')
# finally:
#     print('222')

# import  xlwt
# f = xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# for i in range(1,101):
#     sheet.write(i-1,0,i)
#     sheet.write(i-1,1,'你真狗')
# f.save('aaa.xls')
# import  xlwt
# f = xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# for i in range(1,10):
#    for j in range(1,i+1):
#        if j <= i :
#            k=i*j
#            sheet.write(i-1,j-1,'{}x{}={}'.format(i, j, k))
# f.save('aa.xls')

# import  xlrd
# f=xlrd.open_workbook('aaa.xls')
# b=f.nsheets
# c=f.sheet_names()
# print(c)
# for i in range(len(c)):
# sheet=f.sheet_by_name('python_test')
# b=sheet.ncols
# for i in range(b):
#    c=sheet.col_values(i)
#    print(c)
# for i in range(14,20):
#   b = sheet.cell(i,0).value
#   print(b)
# import  xlwt
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('test1')
# c=[]
# with open('a.txt','r') as  f:
#     a=f.readlines()
#     for i in range(len(a)):
#         w=a[i]
#         b=w.split(',')
#         c.append(b)
# for i in range(len(a)):
#     for j in range(len(b)):
#       sheet.write(i,j,c[i][j])
# ff.save('cj.xls')

# 追加
# from  xlutils.copy import copy
# import xlrd
# f=xlrd.open_workbook('cj.xls')
# sheet1=f.sheets()[0]
# bb=sheet1.nrows
# new_f = copy(f)
# sheet=new_f.get_sheet(0)
# with open('aa.txt','r') as  f:
#     c=[]
#     a=f.readlines()
#     for i in range(len(a)):
#         w=a[i]
#         b=w.split(',')
#         c.append(b)
# for i in range(len(a)):
#     for j in range(len(b)):
#       sheet.write(i+bb,j,c[i][j])
# new_f.save('cj.xls')

# import time
# a=input("输入年月日")
# a=a.split('-')
# b=[int(i) for i in a]
# if b[0]%4==0 and b[0]%400!=0:
#    print('{}年是润年'.format(b[0]))
# elif b[0]%400==0:
#    print('{}年是世纪年'.format(b[0]))
# else:
#    print('这是一个普通的年')
# c=time.strptime('{}-{}-{}'.format(b[0],b[1],b[2]),'%Y-%m-%d')
# print('那天是星期{}'.format(c[6]+1))
# print('那天是这一年的第{}天'.format(c[7]))

# 判断前一天是？？？？
# import time
# a=input("输入年月日")
# a=a.split('-')
# a=[int(i) for i in a]
# b=[5,7,8,10,12]
# if a[1]==2 and a[2]<=28:
#     a[2]=a[2]-1
#     if a[2]==0:
#         a[1]=a[1]-1
#         a[2]=31
# elif a[1]==3 and a[2]<=31:
#     a[2]=a[2]-1
#     if a[2]==0:
#         a[1]=a[1]-1
#         a[2]=28
#         if a[1]==1:
#             a[0]=a[0]-1
# elif a[1] in  b and a[2]<=31:
#     a[2]=a[2]-1
#     if a[2]==0:
#         a[1]=a[1]-1
#         a[2]=30
#         if a[1]==1:
#             a[0]=a[0]-1
# elif a[1]==1 and a[1]<=31:
#      a[2] = a[2] - 1
#      if a[2] == 0:
#         a[1] = 12
#         a[2] = 31
#         if a[1] == 12:
#             a[0] = a[0]-1
# else:
#     a[2]=a[2]-1
#     if a[2]==0 or a[1]==0:
#         a[1]=a[1]-1
#         a[2]=31
#         if a[1]==0:
#             a[0]=a[0]-1
# if a[0]%4==0 and a[0]%400!=0:
#    print('{}年是润年'.format(a[0]))
# elif a[0]%400==0:
#    print('{}年是世纪年'.format(a[0]))
# else:
#    print('这是一个普通的年')
# d=time.strptime('{}-{}-{}'.format(a[0],a[1],a[2]),'%Y-%m-%d')
# print('那天是星期{}'.format(d[6]+1))
# print('那天是这一年的第{}天'.format(d[7]))

#判断前一天
# import time
# a=input("输入年月日")
# a=a.split('-')
# b=[int(i) for i in a]
# if b[0]%4==0 and b[0]%400!=0:
#    print('{}年是润年'.format(b[0]))
# elif b[0]%400==0:
#    print('{}年是世纪年'.format(b[0]))
# else:
#    print('这是一个普通的年')
# b=tuple(b)
# c=time.mktime((b[0],b[1],b[2],0,0,0,0,0,0))
# d=time.localtime(c-86400)
# print('那天是星期{}'.format(d[6]+1))
# print('那天是这一年的第{}天'.format(d[7]))

#从Excel表中读取内容添加到文件中
# import xlrd
# f =xlrd.open_workbook('cj.xls')
# sheet=f.sheets()[0]
# b=sheet.nrows
# print(b)
# f=open(r'b.txt','w+',encoding='utf-8')
# for i in range(0,b):
#     c=sheet.row_values(i)
#     print(c)
#     c=','.join(c)
#     f.write(c)
#     #f.write('\n')
# f.close()

# def aa(self):
#     print(111)
#
#
# def bb(self):
#     print(222)


# class qwe():
#     def aaa(self):
#         print('qwead')

# 建立客户端 tcp的
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.connect(('192.168.0.76',3000))
# msg='hello'
# s.send(msg.encode('utf-8'))
# ww=s.recv(1024)
# print(ww.decode('utf-8'))


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host=(('192.168.0.76',3000))
# msg='hello'
# s.sendto(msg.encode('utf-8'),host)
# ww=s.recv(1024)
# print(ww.decode('utf-8'))