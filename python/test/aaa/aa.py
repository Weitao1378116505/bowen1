# import  socket
# while True:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(('192.168.0.92',3000))
#     ee = input(">>>")
#     sock.send(ee.encode('utf-8'))
#     ww = sock.recv(1024)
#     aa=ww.decode('utf-8')
# #     print(aa)
# import pymysql
# a=pymysql.connect(host='192.168.0.87',port=3306,user='root',passwd='123456')
# conn=a.cursor()

# import os
# a=os.getcwd()
# print(a)
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('192.168.0.97',3000))
while True:
    a,b=sock.recvfrom(1024)
    print(a.decode('utf-8'))
    m='welecome'
    sock.sendto(m.encode('utf-8'),b)