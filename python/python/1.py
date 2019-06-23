#!/usr/bin/python
#-*- coding:utf-8 -*-

#
# a=0
# for i in range(2,101):
#     for j in range(2,101):
#         if i%j==0:
#             break
#     if j==i:
#       a=a+i
# print(a)

# a=input("输入一个数")
# a=int(a)
# b=1
# c=0
# for  i in range(1,a+1):
#     a=a*i
#     c=c+a
# print(c)

# a=0
# for i in range(2,101):
#     for j in range(2,101):
#         if i%j==0:
#             break
#     if i==j:
#      a=a+j
#  print(a)

# a=input('输入一个数')
# a=int(a)
# b=1
# c=0
# for i in range(1,a+1):
#     b=i*b
#     c=c+b
# print(c)

# a=input('aaa')
# c=(a[::-1])
# if a==c:
#  print('yes')
# else:
#  print('no')

# a=7
# b=2
# c=a//b,a%b
# print(c)
# while a>2:
#     print('hello')
#     a-=1















# a = 0
# i = 0
# while i <= 100:
#    a = a + i
#    i = i + 1
#print(a)
# while True:
#    a=input('输入成绩')
#    a=a.split(',')
#    for i,j in enumerate(a):
#        a[i]=int(j)
#    b=sum(a)//len(a)
#    if a[c] < 0:
#     break
#    print('平均数为{}'.format(b))
#    for k  in a:
#        if k < b:
#          print('低于平均数的{}'.format(k))


# 去重
# a=[12,29,24,32,12,29,24]
# for i in a:
#   b=a.count(i)
#   if b>1:
#       for j in range(b-1):
#         a.remove(i)
# a.sort()
# print(a)
# 去重
# a = [12, 29, 24, 32, 12, 29, 24,24]
# b = [ ]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# f = open('a.txt','a',encoding='utf-8')
# for i in range(1, 10):
#     for j in range(1, i+1):
#          f.write('{}x{}={}\t'.format(i, j, i * j))
#     f.write('\n')
# f.close(  )
#写入质数之和
#f = open('a.txt', 'w', encoding='utf-8')
#a=0
# for i in range(2,101):
#      for j in range(2,101):
#          if i%j==0:
#            break
#      if i==j:
#       a=a+i
# f.write('{}'.format(a))
# f.close()
# f = open('a.txt', 'r', encoding='utf-8')
# b = f.read()
# #c = f.readline()
# print(b)
# f.close()



# f = open('a.txt','r',encoding='utf-8')
# for i in range(1,21):
#     if i<15:
#      f.readline()
#     else:
#         print(f.readline())
# for q in range(0,c):
#     d.append(a[q])
# print(d)
# f=a[1]
# for w in range(1,c+1):
#     a.remove(f)
# e=a.count(max(a))
# r=[]
# for j in range(0,e):
#     r.append(a[j])
# print(r)

# f=open('a.jpg','rb')
# b = f.read()
# c=open('b.png','wb')
# c.write(b)
# print(b)
# f.close()
# with open('a.txt','r',encoding='utf-8') as ff:
#     a=ff.read()
#     print(a)


# b=44
# def a():
#     global b
#     b=21
#     print(b)
# a()
# print(b)
# def snd(x):
#     print('hello')
#     print(x)
#
# snd('123131')

# def aaa(b):
#     a=0
#     for i in range(1,b+1):
#         a += i
#     return a
# for i in range(10,41,10):
#     c=aaa(i)+2
#     print(c)

# def aaa(x,y,b):
#     if b=='+':
#        a=x+y
#     elif b=='-':
#        a=x-y
#     elif b=='*':
#        a=x*y
#     elif b=='/':
#        a=x/y
#     print(a)
# aaa(2,4,'*')

# a = lambda x , y : x + y
# b = lambda x , y : x - y
# c = lambda x , y : x * y
# q = lambda x , y : x / y
# while True:
#    s = input('..')
#    if '-'in  s:
#         d = s.split('-')
#         print(b(int(d[0]),int(d[1])))
#    elif '+' in  s:
#         d = s.split('+')
#         print(a(int(d[0]),int(d[1])))
#    elif '*' in s:
#         d = s.split('*')
#         print(c(int(d[0]),int(d[1])))
#    elif '/' in s:
#         d = s.split('/')
#         print(q(int(d[0]),int(d[1])))
#    else:
#         break

# def qq(x,y,z):
#     c=list(x)
#     d=y+z
#     if y+z > len(c):
#       d=len(c)
#     for i in range(y,d):
#         c.pop(y)
#     d=''.join(c)
#     print(d)
# qq('abcdefghigk',3,2)



#购物车




#1：99乘法表
#a=[1,2,44]
# for i,j in enumerate(a):
#     print(i,j)
# for i in range(1,10):
#     for j in range(1,10):
#      if j<=i:
#           print('{}x{}={}'.format(i,j,i*j),end='\t')
#     print(     )

#2：质数之和
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

# 3：阶层之和
# a=input("输入一个数")
# a=int(a)
# b=1
# c=0
# for i in range(1,a+1):
#     b=i*b
#     c=b+c
# print(c)

#4：判断三角形 方法一
# a=input('第一边长')
# b=input('第二边长')
# c=input('第三边长')
# a=int(a)
# b=int(b)
# c=int(c)
# if a+b>c and a+c>b and b+c>a:
#     print('这是三角形')
# else:
#     print('这不是三角形')
#判断三角形 方法二
# a=input('输入三角形的各个边长')
# # a=a.split(',')
# # a=[int(i) for i in a]
# # if a[0]+a[1]>a[2] and a[0]+a[2]>a[1] and a[1]+a[2]>a[0]:
# #     print("这是一个三角形")
# # else:
# #     print("这不是一个三角形")
#5：判断以什么开头，什么结尾





#6：去重并排序
# a=input('输入')
# b=a.split(',')
# c=[]
# for i in b:
#      if i not in c:
#       c.append(i)
# print(c)
# c.sort()
# print(c)
#7:判断字符串是否回文
# a=input('输入')
# if a[::-1]==a:
#     print('yes')
# else:
#     print('no')
#8 ：冒泡选择法
# a=input('输入')
# a=a.split(',')
# a=[int(i) for i in a]
# b=len(a)
# #print(a)
# for q in range(1,b):
#      for j in range(0,b-1):
#          if a[j] > a[j+1]:
#              t=a[j]
#              a[j]=a[j+1]
#              a[j+1]=t
# print(a)
# 8：选择法排序
# a=input('输入')
# a=a.split(',')
# a=[int(i) for i in a]
# b=len(a)
# for q in range(0,b-1):
#  #####   for j in range(q+1,b):
#        if  a[q] > a[j]:
#          t=a[q]
#          a[q]=a[j]
#          a[j]=t
# print(a)
#9：三次猜数字
# import random
# a = random.randrange(1,10)
# for c in range(3):
#     b = input('猜数字')
#     b = int(b)
#     c = int(c)
#     if b > a:
#      print('大了大了')
#      print('还有{}次机会'.format(2-c))
#     elif b < a:
#      print('小了小了')
#      print('还有{}次机会'.format(2-c))
#     elif b == a:
#      print('恭喜 答对了')
#      print('游戏结束')
#      break
# else:
#     print('菜')
#10：水仙花之和
# for i in range(100,1000):
#      a=i//100
#      b=i//10%10
#      c=i%10
#      if a**3+b**3+c**3==i:
#           print(i)

#11 打印第一大 第二大的数
# a=input("输入")
# b=a.split(',')
# c=b.count(max(b))
# d=[]
# for i in range(1,c+1):
#    d.append(max(b))
#    b.remove(max(b))
# q=b.count(max(b))
# e=[]
# for j in range(1,q+1):
#      e.append(max(b))
# print('第一大的数是{}'.format(d))
# print('第二大的数是{}'.format(e))

#11 打印第一大 第二大的数(用函数)
# def asd(a):
#     a.sort()
#     b=a.count(max(a))
#     print(a[-b:])
#     for i in range(1,b+1):
#          a.remove(max(a))
#     c=a.count(max(a))
#     print(a[-c:])
# asd([1,2,3,4,5,6,6,6,6])






#12：不用int将字符串变成整数
# a = '123'
# b = a[::-1]
# c = 0
# for i in range(len(a)):
#     for j in range(10):
#        if str(j) == b[i]:
#           c +=j*10**i
# print(c)

# 13：任意四个数组成三位数
# a=input('输入一个数')
# a=a.split(',')
# c=[int(i) for i in a]
# w=[]
# for j in range(0,len(c)):
#     for k in range(0,len(c)):
#         for l in range(0,len(c)):
#             if c[j] != c[k] and c[j] != c[l] and c[k] != c[l]:
#                 q = c[j]*100 + c[k]*10 + c[l]
#                 if q not in w:
#                     w.append(q)
# print(w)

#14.将列表中的元素向左挪一位
# A=[1,2,3,4,5]
# for i in range(len(A)):##左移
#     A.insert(len(A),A[0])
#     A.remove(A[0])
#     print(A)
#
#15:十进制数转16进制
# dec = int(input("输入数字："))
#
# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))
# a = input('输入')
# a = int(a)
# ff = [str(i) for i in range(10)]+['a','b','c','d','e','f']
# c = ''
# while True:
#     b = a % 16
#     c = c + ff[b]
#     a = a // 16
#     if a == 0:
#         break
# print(c[::-1])
#16：一个数的因为等于他本身
#for i in range(2,1001):
#     a=0
#     for j in range(1,1000):
#       if j<i and i%j==0:
#         a=a+j
#     if a==i:
#      print(i)

#17:将列表中最大的放在最后一位，最小的放在第一位
# a=input("输入")
# a=a.split(',')
# a=[int(i) for i in a]
# b=len(a)
# for j in range(0,b-1):
#     for q in range(j+1,b):
#         if a[j] < a[q]:
#             t=a[j]
#             a[j]=a[q]
#             a[q]=t
# print(a)

#18:一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a=input("输入")
# b=int(a)
# c=[1,2,3,4,6,7,8,9,10]
# for i in range(len(c)):
#     if b==c[i]:
#        c.insert(i,b)
#        break
#     elif b<c[i] and b> c[i-1]:
#         c.insert(i,b)
#         break
#     elif b > c[i]:
#         c.append(b)
#         break
#     elif b < c[i]:
#         c.insert(0,b)
#         break
# print(c)
#18 输入一个数放到正确位置
# a=input("输入")
# b=int(a)
# c=[1,2,3,4,6,7,8,9,10]
# c.append(b)
# for i in range(0,len(c)):
#     for j in range(i+1,len(c)):
#         if c[i] > c[j]:
#             t=c[i]
#             c[i]=c[j]
#             c[j]=t
# print(c)

#19:用100元买100只鸡，公鸡2元
# x=2
# y=1
# z=0.5
# for i in range(0,101):
#     for j in range(0,101):
#         for q in range(0,101):
#             if i+j+q==100 and x*i+y*j+z*q==100:
#              print('公鸡{}个,母鸡{}个,小鸡{}个'.format(i,j,q))

#20：函数，传参数a，b
# def qq(a,b):
#     for i in range(0,len(a)):
#         for j in range(0,len(a)):
#             if j != i  and a[i]+a[j]==b and i > j:
#                 print((a[i]),a[j])
# qq((1,2,3,4,5,6,7),5)
#21：统计文件.cpp有多少行，
# f = open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# for i in a:
#     if '#' in i:
#         a.remove(i)
# for j in  a:
#     if  j=='\n':
#         a.remove(j)
# b=len(a)
# print(a,'\n','统计有{}行'.format(b))
# f.close()
#22:输入成绩，显示低于平均数的
# while True:
#    a=input('输入成绩')
#    a=a.split(',')
#    a=[int(i) for i in a ]
#    b=sum(a)//len(a)
#    if a[0] < 0:
#        break
#    print('平均数为{}'.format(b))
#    c=[k for k  in a if k<b]
#    print('低于平均数的{}'.format(c))



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
#    elif c==5:
#         break
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
# while True:
#    r=input("是否购买(y)(n)")
#    if  r=='y':
#        y=[]
#        k=0
#        for i in range(1,len(d)):
#            if i%2==1:
#                y.append(d[i])
#        l=[int(l) for l in y]
#        for j in range(0,len(y)):
#             k = k +l[j]
#        if a >= k :
#             print("购买成功,余额剩余{}元".format((a-k)))
#             break
#        elif  a< k:
#             print("余额不足,余额剩余{}元,商品需要{}元".format(a,k))
#             while True:
#                 o=input('是否充值:(y)(n)')
#                 if o=='y':
#                    p=input('充值金额')
#                    p=int(p)
#                    a=a+p
#                    print('充值{}元成功,余额有{}元'.format(p,a))
#                    print('继续充值输入(y)，退出充值输入(n)')
#                 if o=='n':
#                     break





# def asw(x):
#    a=0
#    for i in range(x):
#        a += i
#    return a
#
# print(asw(101))

# def asd(a):
#     if  a[0]+a[1]>a[2] and a[0]+a[2]>a[1] and a[1]+a[2]>a[0]:
#         print('是三角形')
#         if a[0]**2+a[1]**2==a[2]**2 or a[0]**2+a[2]**2==a[1]**2 and a[1]**2+a[2]**2==a[0]**2:
#             print('直角三角形')
#         elif a[0]**2+a[1]**2 > a[2]**2 and a[1]**2+a[2]**2 > a[0]**2 and a[0]**2+a[2]**2 > a[1]**2:
#             print('锐角三角形')
#         elif a[0]**2+a[1]**2<a[2]**2 or a[0]**2+a[2]**2<a[1]**2  or a[2]**2+a[1]**2==a[0]**2:
#             print('钝角三角形')
#     else:
#         print('不是三角形')
# asd([5,5,9])


# a='123'
# b=a[::-1]
# c=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j) == b[i]:
#             print(j)
#             c += j*10**i
# print(c)

# a = input('输入')
# a = int(a)
# ff = [str(i) for i in range(10)]+['a','b','c','d','e','f']
# c = ''
# while True:
#     b = a % 16
#     c = c + ff[b]
#     a = a // 16
#     if a == 0:
#         break
# print(c[::-1])
