#!/usr/bin/python
#-*- coding: UTF-8 -*-
__author__ = "wang ting ting"
from selenium.webdriver.common.keys import Keys

class Login():
    #帮我吧首页登录
    def user_login(self, driver, username, password):
        #输入用户名
        driver.find_element_by_id("psname").clear()
        driver.find_element_by_id("psname").send_keys(username)
        #tab键
        driver.find_element_by_id("psname").send_keys(Keys.TAB)
        #输入密码
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys(password)
        driver.find_element_by_id("pwd").send_keys(Keys.TAB)
        #输入验证码（公司内网不限制）
        driver.find_element_by_name("vsn").clear()
        driver.find_element_by_name("vsn").send_keys(username)
        #点击登录按钮
        #driver.find_element_by_css_selector("div.bw8_login_btn > input[type="button"]").click()
        driver.find_element_by_name("vsn").send_keys(Keys.TAB)
        driver.find_element_by_name("vsn").send_keys(Keys.TAB)
        driver.find_element_by_name("vsn").send_keys(Keys.TAB)
        driver.find_element_by_name("vsn").send_keys(Keys.ENTER)








        
        


       
