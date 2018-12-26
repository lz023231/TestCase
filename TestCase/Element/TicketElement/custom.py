#-*- coding: UTF-8 -*-
#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
'''
#添加某个自定义字段 ziduanleiixng是删除的字段类型
from WebServiceLayer.Ticketcircuit.ticketWait import now_show,not_show
def ticket_add_zidingyi(obj, driver, ziduanleiixng):
    zidingyi1 = str(ziduanleiixng).strip()
    print(zidingyi1)
    elements = driver.find_elements_by_css_selector("table[class='table table-hover'']>tbody>tr")
    print(type(elements))
    templetnumber = len(elements)
    print(templetnumber)
    for index in range(int(templetnumber)):
        # index
        print(index + 1)
        target_elem = driver.find_element_by_css_selector("tbody>tr:nth-child(" + str(index + 1) + ")>td:nth-child(2)")
        driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        custom_value = driver.find_element_by_css_selector(
            "tbody>tr:nth-child(" + str(index + 1) + ")>td:nth-child(2)").text
        print(custom_value)
        custom_value1 = str(custom_value).strip()
        print(custom_value1)
        # 这里只判断了字段的名称 并未增加字段类型以及其他的判断
        if custom_value1 == zidingyi1:
            driver.find_element_by_css_selector(
                "tbody>tr:nth-child(" + str(index + 1) + ")>td:nth-child(4)>a:nth-child(2)").click()
            print("进判断不")
'''
#删除某个自定义字段 ziduanname是删除的字段名称
def tikcet_delete_zidingyi(obj, driver, ziduanname):
    zidingyi1 = str(ziduanname).strip()
    print(zidingyi1)
    elements = driver.find_elements_by_css_selector("tbody>tr>td input[type='checkbox']")
    print(type(elements))
    templetnumber = len(elements)
    print(templetnumber)
    for index in range(int(templetnumber)):
        # index
        print(index + 1)
        target_elem = driver.find_element_by_css_selector("tbody>tr:nth-child(" + str(index + 1) + ")>td:nth-child(2)")
        driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        custom_value = driver.find_element_by_css_selector(
            "tbody>tr:nth-child(" + str(index + 1) + ")>td:nth-child(2)").text
        print(custom_value)
        custom_value1 = str(custom_value).strip()
        print(custom_value1)
        # 这里只判断了字段的名称 并未增加字段类型以及其他的判断
        if custom_value1 == zidingyi1:
            driver.find_element_by_css_selector(
                "tbody>tr:nth-child(" + str(index + 1) + ")>td:nth-child(4)>a:nth-child(2)").click()
            print("进判断不")
    # 获取弹出框的text
    message = driver.switch_to_alert().text
    print(message)
    deletemessage = str(message).strip()
    try:
        assert deletemessage == "删除须知：1.一旦删除，该字段的历史数据将无法再找回！2.如果跟外部系统对接了该字段，将导致数据无法回传！确定删除吗？"
    except Exception as e:
        print("删除字段提示异常", format(e))
    # 点击确定按钮，正常删除
    driver.switch_to_alert().accept()
    # 抓取删除成功的提示
    now_show(driver, "[id = 'div_tip']")
    # 再次检查这里面是没有字段内容的
    elements = driver.find_elements_by_css_selector("tbody>tr>td input[type='checkbox']")
    print(type(elements))
    templetnumber = len(elements)
    print(templetnumber)
    for index in range(int(templetnumber)):
        # index
        print(index + 1)
        target_elem = driver.find_element_by_css_selector("tbody>tr:nth-child(" + str(index + 1) + ")>td:nth-child(2)")
        driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        custom_value = driver.find_element_by_css_selector(
            "tbody>tr:nth-child(" + str(index + 1) + ")>td:nth-child(2)").text
        print(custom_value)
        custom_value1 = str(custom_value).strip()
        print(custom_value1)
        # 这里只判断了字段的名称 并未增加字段类型以及其他的判断
        if custom_value1 == zidingyi1:
            print("删除的仍然在这个自定义列表中")