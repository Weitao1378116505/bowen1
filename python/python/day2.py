#!/usr/bin/python
#-*- coding:utf-8 -*-

# 与操作系统交互的模块
# import  os
#获取当前所在的目录
# print(os.getcwd())
# 切换目录
# os.chdir(r'D:\AppStore')
# print(os.getcwd())
# 执行cmd命令
# b=os.popen('route print')
# print(b.read())
# 读取所有文件（默认是当前目录，可以加路径）
# print(os.listdir(r'D:\AppStore'))

# 创建目录
# os.mkdir('aaa')
# 删除空目录
# os.rmdir('aaa')
#创建递归目录
# os.makedirs(r'aaa\bbb\cccc')
# 删除递归目录
# os.removedirs(r'aaa\bbb\ccc')
#判断是否是普通文件
# b=os.path.isfile(  )
#判断是否是目录文件
# b=os.path.isdir(  )

# 将目录和文件名分开
# os.path.split(r'路径\文件名')
# # 将文件名和后缀名分开
# os.path.splitext(r'路径\文件名')

#判断以.py结尾的文件
# a=os.listdir(r'c:\开大\html')
# for i in range(len(a)):
#    b=os.path.isfile(r'c:\开大\html\{}'.format(a[i]))
#    c=[]
#    if b is True:
#        c.append(a[i])
#        # print(a[i])
#        for j in range(len(c)):
#            d=os.path.splitext(r'c:\开大\html\{}'.format(c[j]))
#            if d[-1]=='.py':
#              print(c[j])
#

# 封装了ssh协议，可以实现远程控制
# import paramiko
# # # 创建一个ssh客户端
# with paramiko.SSHClient() as ssh123:
# # # 跳过从kno_host文件中验证
#      ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #     # 连接主机
#      ssh123.connect(hostname='192.168.0.87',port=22,username='root',
#                        password='123456')
#     # 执行命令
#      while True:
#        q=input("输入")
#        a,b,c = ssh123.exec_command('{}'.format(q))
#     # 第一个变量：标准输入的命令
#     # 第二个变量：命令的输出
#     # 第三个变量；命令的报错
#        print(b.read().decode())
#     # 断开连接
#     # ssh123.close()
#        if q=='exit':
#            break

# import paramiko
# # 建立一个传输通道
# aa=paramiko.Transport(('192.168.0.87',22))
# # 连接主机
# aa.connect(username='root',password='123456')
# # 使用ssh协议创建一个传输文件的功能
# c = paramiko.SFTPClient.from_transport(aa)
# # 下载文件，从Linux上传文件到windows上
# #c.get('/home/11','1.sh')
# # 上传文件
# c.put('day1.py','/etc/day1.py')
# # 断开连接
# aa.close()

# for i in range(100)

# 发送邮件 smtp pop3 imap
# import smtplib
# import email.mime.multipart as mu  #制作邮件
# import  email.mime.text as text # 对邮件正文进行处理
# # 创建一个空邮件
# message = mu.MIMEMultipart()
# # 标题
# message['Subject'] = 'python_test'
# # 发件人
# message['From'] = 'weitao_423510@163.com'
# #收件人
# ww='songzf_1996@163.com'
# message['TO'] = 'songzf_1996@163.com'
# # 正文
# txt = """"hello！你牛逼啊！你好牛逼啊！你真牛逼啊"""
# # 对正文进行处理
# aaa = text .MIMEText(txt)
# # 将处理后的正文添加到邮件里
# message.attach(aaa)
# # 添加附件
# att1 = text.MIMEText(open('day1.py', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="day1.py"'
# message.attach(att1)
# # 定义服务器的服务器
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# # 登录服务器 用户名，密码 ，不是邮箱密码，是授权码
# smtp123.login('weitao_423510@163.com','a423510')
# # 发送邮件  写 发件人，收件人，邮件
# smtp123.sendmail('weitao_423510@163.com',ww,message.as_string())
# # 断开连接
# smtp123.close()

# 创建服务器 基于tcp的
# import  socket
# while True:
#     # 创建一个套接字（具有发送和接收功能的）
#     # SOCK_STREAM 指tcp
#     # socket.AF_INET 指iPV4
#     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     # 绑定ip地址
#     s.bind(('192.168.0.121',3000))
#     # 监听
#     s.listen(3) # 3代表当达到处理极限的时候，最大的等待个数
#     # 接受端建立客户的连接
#     client,addr=s.accept()#第一个结果是建立的连接，第二个结果是客户端的ip和端口号
#     # 接受客户端发送的数据
#     reg=client.recv(1024)  #1024指每次接受的最大数据,单位（B）字节
#     print(reg.decode('utf-8'))
#     msg = input('>>>')
#     # 给客户端发送响应
#     client.send(msg.encode('utf-8'))


# 创建服务器  基于udp的
# import  socket
#  创建一个套接字
##  iPv4  SOCK_DGRAM指的是UDP
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.0.121',3000)) # # 绑定ip地址
# while True:
#     # 接受客户端的请求
#     # 第一个变量：是客户端的请求数据
#     # 第二个变量；是客户端的ip和端口号
#     client,addr= s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     msg=input('>>>')
#     s.sendto(msg.encode('utf-8'),addr)  #发送响应



# 正则表达式
# 自己写的正大表达式对于python来说不认识
# 需要将正则表达式转换成python能够识别的正则表达式
# 贪婪模式：尽可能多的去匹配符合条件的内容 例： c=re.re.compile('123(,*)789')
# 非贪婪模式：尽可能少的去匹配符合条件的内容(?) 例：# b = re.compile('123(.*?)789')
# import  re
#将字符串转换成正则表达式
# a='123nishaleba789w123omen789xiayu'
#将字符串转换成正则表达
# b = re.compile('12.*313')
# b = re.compile('123(.*?)789')
#拿着编译后的正则到字符串中去查找
#查找所有符合条件的字符，结果是个列表
# c = b.findall(a)
# findall除了查找，本身还具有编译的能力
# c = re.findall('123(.*?)789',a)
# 替换，将字符串中的某些字符替换成其他的
# a=['qe12331qeqe','12314adada1314','13121adada']
# for i in a:
    # 第一个参数：通过正则表达式过滤出被替换的字符
    # 第二个参数：替换成想要的字符
    # 第三个字符：要被替换的字符串的取值范围
    # c=re.sub('[0-9]+','abc',i)
    # print(c)


# . 匹配任意一个字符，除了换行符之外的
#   加上拥有匹配换行符的能力，在表达式后加  ,re.S
# import  re
# with open('b.txt','r+') as a:
#     b=a.read()
# c=re.compile('123(.*)789',re.S)
# d=c.findall(b)
# print(d)

# chr将数字转化为asill表中对应的字符
# a=[chr(i) for i in range(97,103)]
# print(a)
# ord 将asill表中的字符转化成对应的数字
# print(ord('_'))

# a,b=divmod(100,17)
# print(a,b)


#1 面向对象：将函数进行分类和封装，使开发更高效
# 定义一个类 class  类名：   相当于把同一类的函数放在一起
#  属性 ，方法(函数)   默认首字母大写
# 2:调用  类名().函数名()
# self 不是函数的参数  self是类的实例：方便在类的内部去调用其他函数
# 将类名()赋值给一个对象
# a=Asd()
# a叫  类的实例(也叫做对象) 是方便在类的外部调用其他函数
# 3:继承  一个类继承另一个类
#    多继承：一个类可以继承多个类，类之间没有任何关系
# 4:多态 （方法重写）
# 继承的类中某个函数不满足需求，在本类中自定义一个跟继承的类中函数名相同的函数
# 5:私有方法（函数）
   # 不可被继承的，不能再类的外部调用的
   # 在函数名左边加两个下划线
# 6: 类的专有方法
#  函数名左右有两个下划线的
#  专有方法是python内部固定的
#  只有是个类，具有所有的专有方法
#  专有方法是不需要调用，会自动执行的
#  属性：一个类的所有的函数都具有的特点，调用属性用self.属性名
#  面向对象：优点：可扩展，易维护，可重复使用
#  面向过程：优点：性能好
#  面向过程：通过代码和逻辑一步一步实现要达到的目的
#  面向对象：将函数进行分类和封装，使开发更高效
# from day1 import qwe
# class Asd():
#     def __init__(self): # 初始化属性
#         self.a=4
#         self.b=5
#         # self.bb()
#     def __bb__(self):
#         print(222)
# q=Asd()
# print(q)
# # 括号中写要继承的类
# # 新的类会继承旧的类型中的所有函数
# class www(qwe,Asd):
#     def aaa(self):
#         print('qwead')
#         print('hello')
#     pass
# # a.aa()
# # a.bb()
# class aa( ):
#     # name='压缩'
#     # xueliang=2000
#     def __init__(self,name,xueliang):
#         self.name= name
#         self.xueliang= xueliang
#     def daguai(self):
#         self.xueliang -= 500
#         # self.xueliang -= x
#         # self.xueliang -= y
#         print('{}剩{}'.format(self.name,self.xueliang))
#     def jiaxue(self):
#         self.xueliang += 500
#         print('{}剩{}'.format(self.name, self.xueliang))
#
# q=aa('诺手',1000)
# # w=aa('盖伦',5000)
# q.daguai(10,20)
# q.jiaxue()
# # w.daguai(20,30)
