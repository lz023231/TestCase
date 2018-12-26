# -*- coding: UTF-8 -*-
import time
import random

# 客户管理添加客户名字
def username():
    # a=time.strftime("%Y%m%d%H%M%S", time.localtime())
    a = time.strftime("%m%d%H%M%S", time.localtime())
    return a

# 客户管理添加名字
list1 = ["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","d","s","a","a","z","x","c","v","b","n","m"]
list2 = ['163',"qq",'139']
def name():
    # 随机从列表中取出两位
    a = random.sample(list1,2)
    # 把随机取得列表转为字符串
    str1 = ''.join(a)

    return str1

# 手机号
def number():
    # a=time.strftime("%Y%m%d%H%M%S", time.localtime())
    number1 = time.strftime("%m%d%H%M", time.localtime())
    number2 = random.randint(151,189)
    number3 = str(number2) + number1
    return number3

def email():
    number_email = number()
    number_email2 = random.sample(list2,1)
    number_email3 = "".join(number_email2)
    # print(number_email3)
    email1 = number_email + "@" + number_email3 + ".com"
    # print(email1)

    return email1

def now_time():
    a = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print(a)
    return a


def scl_time():
    # 带-的时间格式
    time1 = time.strftime("%Y-%m-%d",time.localtime())
    print(time1)
    return time1

