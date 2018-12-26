#!/usr/bin/python
#-*- coding: UTF-8 -*-
__author__ = "wang ting ting"
import sys
sys.path.append(".")
from selenium import webdriver
from Element.BwbLogin import *
from WebServiceLayer.IM import on_line_chat_flow,client_people_input_content,service_chat
from Element.WebDriverWait import is_visible_xpath
import unittest
#HTMLTestRunner.py文件放C:\Python27\Lib下
import HTMLTestRunner
import time



class LoginTest(unittest.TestCase):

    def setUp(self):
        '''初始化登录'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.bangwo8.com/login.php")



   # '''调用登录模块'''
    def gnwayauto_login(self):
        '''调用登录模块'''
        username = 'gnwayauto'
        password = 'gnwayauto'
        Login().user_login(self.driver, username, password)
        #等待设置按钮的出现
        # 一直等待某元素可见，默认超时10秒
        is_visible_xpath(self.driver, "//a[@title='设置']")

    def test_online_chat(self):
        '''web在线聊天功能'''
        self.gnwayauto_login()
        on_line_chat_flow(self)
        client_people_input_content(self)
        service_chat(self)


    #
    # def tearDown(self):
    #     self.driver.quit()


if __name__ =='__main__':

# # '''#main()方法使用TestLoader类我来所示所有包含在该模块中以“test”命名开头的方法，并执行'''
#     unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(LoginTest("test_online_chat"))
    # 按照一定的格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 定义报告输出路径
    filePath = './report/' + now + 'result.html'
    fp = open(filePath, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='帮我吧测试报告', description='测试用例结果')
    # 运行测试用例
    runner.run(testunit)
    # 关闭报告文件
    fp.close()
    print file





