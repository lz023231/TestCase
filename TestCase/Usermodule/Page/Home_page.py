# -*- coding: UTF-8 -*-

class HomePage:

    def __init__(self,driver):
        self.driver = driver


    def click_tool(self):
        # 点击主页面左侧工作台设置
        self.driver.find_element_by_xpath('//*[@id="side-menu-bottom"]/li[2]/a').click()

    def click_user(self):
        # 点击客户管理
        self.driver.find_element_by_xpath("//*[@id='userPage']").click()

    def switch_iframe(self):
    # 定位添加客户管理的表单并切换
        iframe1 = self.driver.find_element_by_xpath("//*[@id='rightContentIfr']")
        self.driver.switch_to.frame(iframe1)






