# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from Usermodule.Base.Base import BasePage
from Usermodule.Base.Name import username,name,number,email
from Usermodule.Page.Home_page import HomePage
from Usermodule.Page.User_page import UserPage
import unittest

username = username()
name = name()
numeber = number()
email = email()

class TestCase(unittest.TestCase):


# 实例化驱动并登陆
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.bangwo8.com")
        self.driver.implicitly_wait(10)
        BasePage(self.driver).Login("cszhanghaojie3", "123456", "0")

# 判断是否是二b模式，是则打印无需切换，否则切换为2b模式
    def test01(self):


        try:
            # 进入企业信息
            BasePage(self.driver).current_mode()
            # 切换表单
            BasePage(self.driver).information_switch_iframe1()
            currentmode = BasePage(self.driver).print_current_mode()
            if currentmode == "2b":
                print("无需切换")
            else:
                # 切换2b
                BasePage(self.driver).click_2b()
                BasePage(self.driver).click_sure()
                # BasePage(self.driver).switch_home_iframe()
                #
                # time.sleep(2)
                # BasePage(self.driver).refresh()

        except NoSuchElementException as errors:
            print("定位元素异常(1):%s" % errors)

# """添加公司成功"""
    def test02(self):

        try:

            HomePage(self.driver).click_tool()
            HomePage(self.driver).click_user()
            HomePage(self.driver).switch_iframe()
            UserPage(self.driver).click_add_user()
            UserPage(self.driver).input_user("cs公司")
            UserPage(self.driver).input_user(username)
            UserPage(self.driver).input_user(name)
            time.sleep(3)
            UserPage(self.driver).click_Save_company()

            company = UserPage(self.driver).company()

            assert company in "cs公司"

        except AssertionError as error:
            print("断言异常:%s" % error)
        except NoSuchElementException as errors:
            print("定位元素异常(2):%s" % errors)

# 添加公司重复
    def test03(self):
        """添加公司名重复"""
        try:
            HomePage(self.driver).click_tool()
            HomePage(self.driver).click_user()
            HomePage(self.driver).switch_iframe()
            UserPage(self.driver).click_add_user()
            UserPage(self.driver).input_user("测试公司")

            UserPage(self.driver).click_Save_company()
            BasePage(self.driver).switch_home_iframe()
            prmept = UserPage(self.driver).prompt()

            assert prmept == "此公司已存在！"

        except AssertionError as error:
            print("断言异常:%s" %  error)
        except NoSuchElementException as errors:
            print("定位元素异常(3):%s" % errors)

# 添加联系人成功
    def test04(self):

        """添加联系人成功"""
        try:
            HomePage(self.driver).click_tool()
            HomePage(self.driver).click_user()
            HomePage(self.driver).switch_iframe()
            UserPage(self.driver).one_company_name()
            UserPage(self.driver).click_add_Contacts()
            BasePage(self.driver).switch_home_iframe()
            UserPage(self.driver).switch_iframe()
            # 分三步输入联系人姓名
            UserPage(self.driver).input_Contacts_name("联系人")
            UserPage(self.driver).input_Contacts_name(username)
            UserPage(self.driver).input_Contacts_name(name)
            # 职位
            UserPage(self.driver).input_Contact_position("跳梁小丑")
            # 手机号
            UserPage(self.driver).input_Contact_number(numeber)
            # 标签
            UserPage(self.driver).input_Contact_Label("自动化添加")
            UserPage(self.driver).input_Contact_Telephone("010-12580")
            # 邮箱
            UserPage(self.driver).input_Contact_email(email)
            # qq
            UserPage(self.driver).input_Contact_qq(numeber)
            # 备注
            UserPage(self.driver).input_Contact_Remarks(u"自动化测试")
            # 点击保存
            UserPage(self.driver).click_Save_Contact()


        except AssertionError as error:
            print("断言异常:%s" %  error)
        except NoSuchElementException as errors:
            print("定位元素异常(4):%s" % errors)


# 删除联系人




    def tearDown(self):
        time.sleep(3)
        BasePage(self.driver).quitBrowser()




if __name__ == '__main__':
    unittest.main()


