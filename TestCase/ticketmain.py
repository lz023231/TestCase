#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = "wang ting ting"
import sys

sys.path.append(".")
# from TestCase.Element.BwbLogin import *
# from WebServiceLayer.IM import on_line_chat_flow,client_people_input_content,service_chat
from selenium import webdriver
from Element.BwbLogin import Login
from Element.WebDriverWait import is_visible_xpath
from WebServiceLayer.Ticketcircuit.ticketCustom import ticketcustom
from WebServiceLayer.Ticketcircuit.tikcetrukou import tikcet_rukou
from WebServiceLayer.Ticketcircuit.ticketTemplet import tickettemplets
from WebServiceLayer.Ticketcircuit.addTicket import add_new_ticket
import random
import unittest
import time
from Element.OtherElement import setup_element_click


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Python27\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.bangwo8.com/login.php")

    #    '''调用登录模块'''
    def gnwayauto_login(self):
        username = 'ceshi1007'
        password = 'ceshi1007'
        Login().user_login(self.driver, username, password)
        # 等待设置按钮的出现
        # 一直等待某元素可见，默认超时10秒
        is_visible_xpath(self.driver, "//a[@title='设置']")

    # 自定义字段的添加，模板添加以及字段在模板中的使用
    def test_ticket_zidingyi(self):
        self.gnwayauto_login()
        tikcet_rukou().ticket_rukou_click(self.driver)
        ticketcustom().ticket_zidingyi(self.driver)
        #data1=random.randrange(0, 101, 2)
        data1 = random.randint(1, 10000)  # 更加完善随机的数据
        # 添加自定义字段
        ticketcustom().ticket_add_zidingyi(self.driver, data1)
        #添加模板并将添加的文本字段添加到模板里面
        tickettemplets().ticket_ticketmoudle(self.driver)
        tickettemplets().ticket_add_ticketmoudle(self.driver, data1)
        tickettemplets().ticket_add_custom(self.driver, data1)
        time.sleep(20)  # 一切发生的太快  获取不到添加的模板名称
        # 创建工单
        add_new_ticket().new_ticket(self.driver, data1)
        # 进入编辑页面进行判断
        add_new_ticket().answer_ticket(self.driver, data1)
        #点击设置按钮
        setup_element_click(self)
        #点击进入工单和自定义字段
        tikcet_rukou().ticket_rukou_click(self.driver)
        ticketcustom().ticket_zidingyi(self.driver)
        ticketcustom().tikcet_delete_zidingyi(self.driver,data1)
        #点击进入工单模板
        tickettemplets().ticket_ticketmoudle(self.driver)
        tickettemplets().tikcet_tickettemplet_delete(self.driver,data1)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    '''#main()方法使用TestLoader类我来所示所有包含在该模块中以“test”命名开头的方法，并执行'''
    unittest.main()




