#!/usr/bin/python
#-*- coding: UTF-8 -*-
__author__ = "wang ting ting"


import time

# 入口渠道设置
def ru_kou_qu_ao_click(self):
    # 入口渠道设置定位
    self.driver.find_element_by_xpath("//div[contains(text(),'入口渠道设置') and @class='dd-handle dd-title']").click()
    time.sleep(2)

#在线聊天下的选项
class OnlineChat():
    # 在线聊天定位
    def online_chat_click(self, obj):
        obj.driver.find_element_by_css_selector("#nestable ol li:nth-child(1) ol li:nth-child(1) div a").click()
        time.sleep(2)
    #预览效果定位
    def previewresult_click(self, obj):
        obj.driver.switch_to.frame(obj.driver.find_element_by_css_selector("iframe#rightContentIfr"))
        obj.driver.find_element_by_css_selector("a#btn-success").click()
        obj.driver.switch_to.default_content()
