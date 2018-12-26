#from nose.tools import assert_equal
#-*- coding: UTF-8 -*-
from  Element.WebDriverWait import is_visible_xpath
from selenium import webdriver
import time
from WebServiceLayer.Ticketcircuit.ticketWait import now_show,not_show
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class tickettemplets():
    # 工单模板入口
    def ticket_ticketmoudle(self,driver):
        driver.find_element_by_xpath("//a[contains(text(),'工单模板')]").click()
        #driver.find_element_by_xpath("//a[contains(text(),'工单模板')]").click()
        time.sleep(2)
        is_visible_xpath(driver,".btn.btn-default.title_fontsize3")
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe#rightContentIfr"))
        # driver.find_element_by_css_selector(".btn.btn-default.title_fontsize3").click()
        # time.sleep(3)
        # now_show(driver,"name='e1pov_act'")

    # 添加模板
    def ticket_add_ticketmoudle(self,driver,data2):
        driver.find_element_by_css_selector("[class='btn btn-default title_fontsize3']").click()
        not_show(driver,"[name='ticketTemplateName']")
        not_show(driver,"[name='ticketTemplateDescription']")
        not_show(driver,"[name='availabilityPart']")
        driver.find_element_by_css_selector("[name='ticketTemplateName']").send_keys(data2)
        driver.find_element_by_css_selector("[name='ticketTemplateDescription']").send_keys(data2)
        #driver.find_element_by_css_selector("[name='availabilityPart']").send_keys(data2)
        not_show(driver,"[id ='selectColumn']")


    #添加模板字段
    def ticket_add_custom(self,driver,datacustomname):
        newdatacustomname = str(datacustomname).strip()
        driver.find_element_by_css_selector("[id ='selectColumn']").click()
        not_show(driver,"[id='div_columnInfo']")
        #页面滑动到底部 因为添加的会在最后一个现实
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        driver.find_element_by_css_selector("#div_columnInfo>div:nth-last-child(2)>input[type='checkbox']").click()
        driver.find_element_by_css_selector("[onclick ='showTableList()']").click()
        customnametext1=driver.find_element_by_css_selector("tbody[class='info']>tr>td:first-child").text
        customname = str(customnametext1).strip()
        #选择字段的时候  有添加的这个字段名称
        try:
            assert customname == newdatacustomname
            print("添加字段成功")
        except Exception as e:
            print("添加字段不成功", format(e))
        driver.find_element_by_css_selector("[name='btnSubmit']").click()
        #判断选择字段后出现在模板列表中
        customname1text1 = driver.find_element_by_css_selector("table[class='table']>tbody[class='info']>tr:last-child>td:first-child").text
        customname1 = str(customname1text1).strip()
        try:
            assert customname1 == newdatacustomname
            print("添加字段成功")
        except Exception as e:
            print("添加字段不成功", format(e))
        driver.switch_to_default_content()

    #第二次进入模板判断之前的文本字段时候存在
    def tikcet_tickettemplet_tow(self,driver,data1):
        mobanname1 = str(data1).strip()
        elements =driver.find_elements_by_css_selector("tr>td[class='temName']")
        print(type(elements))
        templetnumber=len(elements)
        for index in range(int(templetnumber)):
            #index
            print(index+3)
            templet_value = driver.find_element_by_css_selector("tbody>tr:nth-child("+str(index+3)+")>td[class='temName']").text
            templet_value_name = str(templet_value)
            print (templet_value_name)
            if templet_value_name == data1:
                driver.find_element_by_css_selector("tbody>tr:nth-child('+str(index+3)+')>td[class='text_right_img']>a:nth-child(2)>img").click()
        now_show(driver,"[name='ticketTemplateName']")
        templetname=driver.find_element_by_css_selector("[name='ticketTemplateName']").get_attribute("value")
        templetdescr=driver.find_element_by_css_selector("name='ticketTemplateDescription'").get_attribute("value")
        newtempletname = str(templetname).strip()
        newtempletdescr = str(templetdescr).strip()
        try:
            assert newtempletname == mobanname1
            print("打开模板正常")
        except Exception as e:
            print("模板标题不正确，打开错误", format(e))
        try:
            assert newtempletdescr == mobanname1
            print("模板描述显示正常")
        except Exception as e:
            print("模板描述显示错误", format(e))

    # def tikcet_tickettemplet_update(self):
    #
    def tikcet_tickettemplet_delete(self,driver,mobanname):
        zidingyi1 = str(mobanname).strip()
        print(zidingyi1)
        elements = driver.find_elements_by_css_selector("tbody>tr>td.temName")
        print(type(elements))
        templetnumber = len(elements)-1
        print(templetnumber)
        for index in range(int(templetnumber)):
            # index
            print(index)
            target_elem = driver.find_element_by_css_selector("table[class='footable table table-stripped toggle-arrow-tiny table-hover'] > tbody > tr:nth-child("+str(index+3)+")")
            driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            custom_value =driver.find_elements_by_css_selector("tbody>tr>td.temName")[index].text
            print(custom_value)
            custom_value1 = str(custom_value).strip()
            print(custom_value1)
            # 这里只判断了字段的名称 并未增加字段类型以及其他的判断
            if custom_value1 == zidingyi1:
                #tbody>tr>td.text_right_img>a:nth-child(3)
                driver.find_elements_by_css_selector("tbody>tr>td.text_right_img>a:nth-child(3)")[index].click()
                print("进判断不")
                driver.switch_to_alert().accept()
                # 抓取删除成功的提示
                now_show(driver, "[id = 'div_tip']")
            # 再次检查这里面是没有字段内容的
        elements = driver.find_elements_by_css_selector("tbody>tr>td.temName")
        print(type(elements))
        templetnumber = len(elements)-1
        print(templetnumber)
        for index in range(int(templetnumber)):
            # index
            print(index)
            target_elem = driver.find_element_by_css_selector("table[class='footable table table-stripped toggle-arrow-tiny table-hover'] > tbody > tr:nth-child("+str(index+3)+")")
            driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
            custom_value = driver.find_elements_by_css_selector("tbody>tr>td.temName")[index].text
            print(custom_value)
            custom_value1 = str(custom_value).strip()
            print(custom_value1)
            # 这里只判断了字段的名称 并未增加字段类型以及其他的判断
            if custom_value1 == zidingyi1:
                # tbody>tr>td.text_right_img>a:nth-child(3)
                driver.find_elements_by_css_selector("tbody>tr>td.text_right_img>a:nth-child(3)")[index].click()
                print("进判断不")
        driver.switch_to_default_content()






