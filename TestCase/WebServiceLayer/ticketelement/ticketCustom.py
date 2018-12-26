#-*- coding: UTF-8 -*-
#from nose.tools import assert_equal
#import assertEqual
from selenium import webdriver
import time
from WebServiceLayer.ticketelement.ticketWait import now_show,not_show
import traceback


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
        driver.find_element_by_css_selector(".btn.btn-default.title_fontsize3").click()
        time.sleep(3)
        now_show(driver,"[class='table table-hover']")
        driver.find_element_by_css_selector("tbody>tr:nth-child(2)>td>a").click()
        driver.find_element_by_css_selector("[name='title']").send_keys(data1)
        driver.find_element_by_css_selector("[name='btnSubmit']").click()
        now_show(driver,".mail-box-header tbody>tr:last-child")
        '''
        try:
            assertEqual(
                driver.find_element_by_css_selector(".mail-box-header tbody>tr:last-child>td:nth-child(2)").text,
                data1, "保存标题错误")
            assertEqual(
                driver.find_element_by_css_selector(".mail-box-header tbody>tr:last-child>td:nth-child(3)").text,
                "文本", "类型显示错误")
        except:
            f = open("c:log.txt", 'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
        '''
        # 跳出iframe
        driver.switch_to_default_content()







