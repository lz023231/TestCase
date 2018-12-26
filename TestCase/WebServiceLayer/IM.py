#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "wang ting ting"
from Element.OtherElement import setup_element_click,get_title
from Element.RuKouQuDaoSetup import ru_kou_qu_ao_click,OnlineChat
from Element.imElement import client_bution_click,client_ren_gong_click,client_input_click,client_input_content,client_send,service_clickOnLineService,service_clickLineUp,service_getInfo,service_end,client_get_winid,service_sendInfo,client_get_serviceSendInfo
import Element.imElement



def switch_window(obj, num):
    #获取所有窗口信息
    windows = obj.driver.window_handles
    print(windows)
    # 切换到第二个窗口，即新打开的web客户端
    obj.driver.switch_to.window(windows[num])


#从在线聊天-桌面网站接入-预览效果，打开web客户端
def on_line_chat_flow(obj):
    setup_element_click(obj)
    ru_kou_qu_ao_click(obj)
    OnlineChat().online_chat_click(obj)
    OnlineChat().previewresult_click(obj)
    #切换到“预览窗口”
    switch_window(obj, -1)


def client_people_input_content(obj):
    client_bution_click(obj)
    client_ren_gong_click(obj)
    #client_ke_fu_zu_click(obj)
    client_input_click(obj)
    client_input_content(obj,Element.imElement._sendmessage)
    client_send(obj)
    # client_get_winid(obj)
    switch_window(obj, 0)
    get_title(obj)


def service_chat(obj):
    service_clickOnLineService(obj)
    service_clickLineUp(obj)
    service_getInfo(obj)
    service_sendInfo(obj)
    switch_window(obj, 1)
    client_get_serviceSendInfo(obj)
    switch_window(obj,0)
    service_end(obj)















