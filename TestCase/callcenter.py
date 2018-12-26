#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = "wang ting ting"
import sys

sys.path.append(".")
from selenium import webdriver
from Element.BwbLogin import *
from WebServiceLayer.IM import on_line_chat_flow,client_people_input_content,service_chat
import unittest
from Element.WebDriverWait import is_visible_xpath
from WebServiceLayer.Call import talking


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.bangwo8.com/login.php")

    #    '''调用登录模块'''
    def gnwayauto_login(self):
        username = 'mystest3'  # 'wangtt-auto'
        password = 'mystest3'  # '123456'
        Login().user_login(self.driver, username, password)

        # 等待设置按钮的出现
        # 一直等待某元素可见，默认超时10秒
        is_visible_xpath(self.driver, "//a[@title='设置']")

    def test_online_chat(self):
        self.gnwayauto_login()
        # on_line_chat_flow(self)
        # client_people_input_content(self)
        # service_chat(self)
        talking(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    '''#main()方法使用TestLoader类我来所示所有包含在该模块中以“test”命名开头的方法，并执行'''
    unittest.main()
