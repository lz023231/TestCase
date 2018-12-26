#-*- coding: UTF-8 -*-
import sys
reload(sys)
#import importlib
#importlib.reload(sys)
#importlib.setdefaultencoding( "utf-8" )
import time
from WebServiceLayer.Ticketcircuit.ticketWait import now_show,not_show
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#滑动页面直到元素出现
        #target = driver.find_element_by_css_selector("form[name='createTicket_act'] span[class='setting_icon']")
        #driver.execute_script("arguments[0].scrollIntoView();", target)
class add_new_ticket():
    #新建工单—新布局
    def new_ticket(self,driver,mobanname):
        newmobanname = str(mobanname).strip()
        driver.find_element_by_css_selector("[class='add_addition']").click()
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe[class='newIframe']"))
        now_show(driver, "[name='descript']")
        driver.find_element_by_css_selector("[name='subject']").click()
        driver.find_element_by_css_selector("[name='subject']").send_keys(mobanname)
        driver.find_element_by_css_selector("[name='descript']").click
        driver.find_element_by_css_selector("[name='descript']").send_keys(mobanname)
        #滑动到某元素出现的位置
        target_elem = driver.find_element_by_css_selector("form>div:nth-child(4)>div.layout_content_left_top_header>div")
        driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        #进行模板的选择：进行模板的搜索选中
        driver.find_element_by_css_selector("form>div:nth-child(4) > div.layout_content_left_top_header>div>span.setting_icon").click()
        now_show(driver,".modal.fade.in .modal-dialog .modal-content")
        driver.find_element_by_css_selector(".modal.fade.in .modal-dialog .modal-content a[class='chosen-single']").click()
        time.sleep(10)
        locator=(By.CSS_SELECTOR,"#ticketTemplate>div>div>div.modal-body>div>div>div>div>div>ul")
        WebDriverWait(driver,20).until(EC.presence_of_element_located(locator))
        now_show(driver,"#ticketTemplate>div>div>div.modal-body>div>div>div>div>div>ul")
        driver.find_element_by_css_selector("div[id='ticketTemplate']  div.modal-body  input[type='text']").send_keys(newmobanname)
        time.sleep(5)
        driver.find_element_by_css_selector("div[id='ticketTemplate']  div.modal-body  input[type='text']").send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_css_selector("[name='submitTicketTemplate']").click()
        #ul[class="ul_first_last ticketTemplateInfo"]>li:nth-last-child(1)>div>input
        #模板中添加的字段名称是自己添加的字段名称
        time.sleep(5)
        ziduantext1=driver.find_element_by_css_selector("ul[class='ul_first_last ticketTemplateInfo']>li:nth-last-child(1)>div>div:first-child").text
        print(ziduantext1)
        zitext1=str(ziduantext1).strip()
        print(zitext1)
        print(type(zitext1))
        print(type(newmobanname))
        try:
            assert zitext1 == newmobanname
            print("模板中添加的字段名称是自己添加的字段名称")
        except Exception as e:
            print("模板中添加的字段名称不是自己添加的字段名称，模板中字段名称显示错误", format(e))
        now_show(driver, "ul[class='ul_first_last ticketTemplateInfo']>li:nth-last-child(1)>div>input")
        driver.find_element_by_css_selector("ul[class='ul_first_last ticketTemplateInfo']>li:nth-last-child(1)>div>input").click()
        driver.find_element_by_css_selector("ul[class='ul_first_last ticketTemplateInfo']>li:nth-last-child(1)>div>input").send_keys(mobanname)
        driver.find_element_by_css_selector("[id='submitForTicket']")


    #进入模板编辑页面的判断
    def answer_ticket(self,driver,mobannamedata):
        #工单的标题和描述的判断
        newmobannamedata = str(mobannamedata).strip()
        ticketname=driver.find_element_by_css_selector("input[name='subject']").get_attribute("value")
        print(ticketname)
        # ticketdes=driver.find_element_by_css_selector("[class='col-sm-12 file_li_content_title']").text
        # print(ticketdes)
        #模板名称的判断
        text3=driver.find_element_by_css_selector("[class='ticketTempName']").text
        mobantext3=str(text3).strip()
        try:
            assert mobantext3 == newmobannamedata
            print("编辑页面工单模板是选择的模板名称")
        except Exception as e:
            print(mobantext3)
            print(newmobannamedata)
            print("编辑页面工单模板不是选择的模板名称，模板名称显示错误", format(e))
        text4 = driver.find_element_by_css_selector("ul[class='ul_first_last ticketTemplateInfo']>li:nth-last-child(1)>div>div:first-child").text
        print(text4)
        mobantext4=str(text4).strip()
        try:
            assert mobantext4 == newmobannamedata
            print("编辑页面工单模板中的字段显示正常")
        except Exception as e:
            print(mobantext4)
            print(newmobannamedata)
            print("编辑页面工单模板中的字段显示异常 不是添加的字段名称", format(e))
        textwenbentext=driver.find_element_by_css_selector("ul[class='ul_first_last ticketTemplateInfo'] li:nth-last-child(1) input").get_attribute("value")
        textwenbenvalue = str(textwenbentext).strip()
        try:
            assert textwenbenvalue == newmobannamedata
            print("工单编辑页面字段数据保存正常")
        except Exception as e:
            print(textwenbenvalue)
            print(newmobannamedata)
            print("工单编辑页面字段数据保存异常", format(e))
        driver.switch_to_default_content()
