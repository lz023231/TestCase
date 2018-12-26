#-*- coding: UTF-8 -*-
#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
from WebServiceLayer.Ticketcircuit.ticketWait import now_show,not_show
from Element.TicketElement.custom import tikcet_delete_zidingyi


class ticketcustom():
    #工单自定义字段的入口
    def ticket_zidingyi(self,driver):
        driver.find_element_by_xpath("//a[contains(text(),'工单自定义字段')]").click()
        time.sleep(2)
        #title1 = get_title()
        #assertEqual(self.title1, '工单字段', 'pass')
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe#rightContentIfr"))
        now_show(driver,".btn.btn-default.title_fontsize3")

    #添加自定义字段—文本类型的
    def ticket_add_zidingyi(self,driver,data1):
        print(data1)
        driver.find_element_by_css_selector(".btn.btn-default.title_fontsize3").click()
        time.sleep(3)
        now_show(driver,"[class='table table-hover']")
        driver.find_element_by_css_selector("tbody>tr:nth-child(2)>td>a").click()
        driver.find_element_by_css_selector("[name='title']").send_keys(data1)
        driver.find_element_by_css_selector("[name='btnSubmit']").click()
        now_show(driver,".mail-box-header tbody>tr:last-child")
        # 跳出iframe
        driver.switch_to_default_content()

    #删除某个自定义字段
    def tikcet_delete_zidingyi(self,driver,ziduanname):
        zidingyi1 = str(ziduanname).strip()
        print(zidingyi1)
        elements = driver.find_elements_by_css_selector("tbody>tr>td input[type='checkbox']")
        print(type(elements))
        templetnumber = len(elements)
        print(templetnumber)
        for index in range(int(templetnumber)):
            # index
            print(index+1)
            target_elem = driver.find_element_by_css_selector("tbody>tr:nth-child("+str(index+1)+")>td:nth-child(2)")
            driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            custom_value = driver.find_element_by_css_selector("tbody>tr:nth-child("+str(index+1)+")>td:nth-child(2)").text
            print(custom_value)
            custom_value1 = str(custom_value).strip()
            print(custom_value1)
            #这里只判断了字段的名称 并未增加字段类型以及其他的判断
            if custom_value1 == zidingyi1:
                driver.find_element_by_css_selector("tbody>tr:nth-child("+str(index+1)+")>td:nth-child(4)>a:nth-child(2)").click()
                print("进判断不")
        #获取弹出框的text
        message = driver.switch_to_alert().text
        print(message)
        deletemessage = str(message).strip()
        try:
            assert deletemessage == "删除须知：1.一旦删除，该字段的历史数据将无法再找回！2.如果跟外部系统对接了该字段，将导致数据无法回传！确定删除吗？"
        except Exception as e:
            print("删除字段提示异常", format(e))
        #点击确定按钮，正常删除
        driver.switch_to_alert().accept()
        #抓取删除成功的提示
        now_show(driver,"[id = 'div_tip']")
        #再次检查这里面是没有字段内容的
        elements = driver.find_elements_by_css_selector("tbody>tr>td input[type='checkbox']")
        print(type(elements))
        templetnumber = len(elements)
        print(templetnumber)
        for index in range(int(templetnumber)):
            # index
            print(index+1)
            target_elem = driver.find_element_by_css_selector("tbody>tr:nth-child("+str(index+1)+")>td:nth-child(2)")
            driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            custom_value = driver.find_element_by_css_selector("tbody>tr:nth-child("+str(index+1)+")>td:nth-child(2)").text
            print(custom_value)
            custom_value1 = str(custom_value).strip()
            print(custom_value1)
            #这里只判断了字段的名称 并未增加字段类型以及其他的判断
            if custom_value1 == zidingyi1:
                print("删除的仍然在这个自定义列表中")
        driver.switch_to_default_content()








