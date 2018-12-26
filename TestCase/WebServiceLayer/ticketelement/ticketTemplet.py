#from nose.tools import assert_equal
#-*- coding: UTF-8 -*-
from  Element.WebDriverWait import is_visible_xpath
from selenium import webdriver
import time
from WebServiceLayer.ticketelement.ticketWait import now_show,not_show
from selenium.webdriver.common.keys import Keys
class tickettemplets():
    # 工单模板入口
    def ticket_ticketmoudle(self,driver):
        driver.find_element_by_xpath("//a[contains(text(),'工单模板')]").click()
        #driver.find_element_by_xpath("//a[contains(text(),'工单模板')]").click()
        time.sleep(2)
        is_visible_xpath(driver,".btn.btn-default.title_fontsize3")
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe#rightContentIfr"))
        driver.find_element_by_css_selector(".btn.btn-default.title_fontsize3").click()
        time.sleep(3)
        now_show(driver,"name='e1pov_act'")

    # 添加模板
    def ticket_add_ticketmoudle(self,driver,data2):
        driver.find_element_by_css_selector("[name='e1pov_act']").click()
        not_show(driver,"[name='ticketTemplateName']")
        not_show(driver,"[name='ticketTemplateDescription']")
        not_show(driver,"[name='availabilityPart']")
        driver.find_element_by_css_selector("[name='ticketTemplateName']").send_keys(data2)
        driver.find_element_by_css_selector("[name='ticketTemplateDescription']").send_keys(data2)
        driver.find_element_by_css_selector("[name='availabilityPart']").send_keys(data2)
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
        # 更新模板
    #def ticket_update_ticketmoudle(obj):







