#!/usr/bin/python
#-*- coding: UTF-8 -*-
from selenium.webdriver.support.select import Select
import time
from Element.WebDriverWait import is_visible_xpath
import autoit
import random

def callcenter(self):
    # 启动sip电话
    autoit.run(r"C:\MicroSIP-3.15.1\microsip.exe")
    time.sleep(10)
    # 判断窗口是否存在
    judge = autoit.win_exists("MicroSIP - auto")
    print judge
    if judge == 1:
        pass
    else:
        autoit.control_click("Update Available", "[CLASS:Button;INSTANCE:2]")
    autoit.win_activate("MicroSIP - auto")
    #进入呼叫中心工作台
    is_visible_xpath(self.driver,"//*[@title='呼叫中心']")
    self.driver.find_element_by_xpath("//*[@title='呼叫中心']").click()
    self.driver.switch_to.frame('rightContentIfrCallCenter')
    # 点击外呼按钮拨打一通电话（外呼挂断）
    is_visible_xpath(self.driver, "//div[@id='hungUp']")
    callphone='14442698463'
    self.driver.find_element_by_id("inputPassword").send_keys(callphone)
    self.driver.find_element_by_id("tupian_dianhua").click()
    #sip接听电话
    autoit.win_wait("Incoming call")
    autoit.control_click("Incoming call", "[CLASS:Button;INSTANCE:3]")
    # 点击外呼按钮拨打一通电话（外呼接听）
    is_visible_xpath(self.driver, "//div[@id='hungUp']")
    callphone = '14442698463'
    self.driver.find_element_by_id("inputPassword").send_keys(callphone)
    self.driver.find_element_by_id("tupian_dianhua").click()
    # sip接听电话
    autoit.win_wait("Incoming call")
    autoit.control_click("Incoming call", "[CLASS:Button;INSTANCE:2]")
    #等待外呼弹屏出现
    time.sleep(5)
    is_visible_xpath(self.driver,"//div[@id='hungUp']")
    #挂断电话
    self.driver.find_element_by_id("hungUp").click()
    time.sleep(5)
    # 判断窗口是否存在
    judge1 = autoit.win_exists("MicroSIP - auto")
    print judge1
    if judge1 == 1:
        autoit.win_close("MicroSIP - auto")
    else:
        pass
    self.driver.switch_to.default_content()

def summary(self):
    # 等待当前页面元素
    self.driver.switch_to.frame('rightContentIfrCallCenter')
    is_visible_xpath(self.driver,"//button[@id='templateList']")
    #点击选择固定的模板
    self.driver.find_element_by_id("templateList").click()
    self.driver.find_element_by_xpath("//a[@value='23']").click()
    #填写服务总结
    Example='This is the service summary automated test'
    self.driver.find_element_by_xpath("// textarea[ @ style = 'border:1px solid #ccc']").send_keys(Example)
    #填写正整数
    integer=random.randint(0,1000)
    print(integer)
    self.driver.find_element_by_xpath("//input[@name='eavColumnT1260900']").send_keys(integer)
    #勾选复选框
    self.driver.find_element_by_xpath("//input[@name='eavColumnT1439934']").click()
    #选择日期
    # today = datetime.date.today()
    # today1=print(today)
    # self.driver.find_element_by_xpath("//input[@name='eavColumnT1260939']").send_keys(today1)
    #选择一个级联字段的值
    sel=self.driver.find_element_by_xpath("//select[@name='cc1793982[s2]']")
    Select(sel).select_by_value("o26")
    sel2=self.driver.find_element_by_xpath("//select[@name='cc1793982[s3]']")
    Select(sel2).select_by_value("o30")
    sel3 = self.driver.find_element_by_xpath("//select[@name='cc1793982[s4]']")
    Select(sel3).select_by_value("o31")
    #点击提交服务总结
    self.driver.find_element_by_id("customerSubmit").click()
    element=is_visible_xpath(self.driver,"//div[@onclick='autoCreateTicket.closeTicketModal()']")
    if element==False:
        pass
    else:
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@onclick='autoCreateTicket.closeTicketModal()']").click()
    #等待服务总结提交完成
    is_visible_xpath(self.driver,"//div[@id='div_tip']")
    self.driver.switch_to.default_content()

def comparison(self):
    #查找电话时间
    self.driver.switch_to.frame('rightContentIfrCallCenter')
    is_visible_xpath(self.driver,"//a[@id='callDetail']")
    self.driver.find_element_by_id("callDetail").click()
    #获取打电话的开始时间
    time.sleep(5)
    is_visible_xpath(self.driver,"//span[@id='beginTime']")
    call_time = self.driver.find_element_by_xpath("//span[@id='beginTime']").text
    print(call_time)
    self.driver.switch_to.default_content()
    #进入统计页面
    is_visible_xpath(self.driver,"//a[@title='统计&监控']")
    self.driver.find_element_by_xpath("//a[@title='统计&监控']").click()
    #等待时长
    time.sleep(60)
    #进入呼叫中心服务记录
    is_visible_xpath(self.driver,"//*[@id='statistical']/li[3]")
    self.driver.find_element_by_xpath("//*[@id='statistical']/li[3]").click()
    #查看服务记录
    self.driver.switch_to.frame('rightContentIfr')
    is_visible_xpath(self.driver,"//div[@class='row topSpace']/div/div/ul/li[1]")
    self.driver.find_element_by_xpath("//div[@class='row topSpace']/div/div/ul/li[1]").click()
    #获取第一个聊天记录的产生时间
    is_visible_xpath(self.driver,"//*[@id='listData']/tbody/tr[1]/td[3]")
    call_time2=self.driver.find_element_by_xpath("//*[@id='listData']/tbody/tr[1]/td[3]").text
    call_time3 = call_time[5:19]
    print(call_time3,call_time2)
    if call_time2==call_time3:
        pass
    else:
        raise AssertionError





