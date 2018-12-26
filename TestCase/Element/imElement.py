#!/usr/bin/python
#-*- coding: UTF-8 -*-
__author__ = "wang ting ting"
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from Element.WebDriverWait import is_visible_css
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# from Element.OtherElement import to_switch_ifrome


global _sendmessage
_sendmessage=u'客户发送的消息'
global _serviceSendMessage
_serviceSendMessage=u'客服发送的消息'
#web客户端点击“咨询客服”
def client_bution_click(obj):
    time.sleep(5)
    obj.driver.find_element_by_css_selector("#bw8-chatWrap > div > span").click()

#点击转人工服务(需求切换iframe)
def client_ren_gong_click(obj):
    time.sleep(2)
    #切换iframe
    obj.driver.switch_to.frame(obj.driver.find_element_by_css_selector("iframe#bw8-chatIframe"))
    time.sleep(3)
    obj.driver.find_element_by_css_selector("a#bw8_whole_footer_artificial").click()
    time.sleep(3)

#点击选择第一个客服组
def client_ke_fu_zu_click(obj):
    is_visible_css(obj.driver,"ul.bw8_skill_middle_ul li a")
    obj.driver.find_element_by_css_selector("ul.bw8_skill_middle_ul li a")

#在输入框内点击
def client_input_click(obj):
    is_visible_css(obj.driver,".w8_footer_text_import")
    obj.driver.find_element_by_css_selector(".bw8_footer_text_import").click()

#在输入框内输入内容
def client_input_content(obj, inputContent):
    is_visible_css(obj.driver,".bw8_footer_text_import")
    obj.driver.find_element_by_css_selector(".bw8_footer_text_import").send_keys(inputContent)

#点击发送按钮
def client_send(obj):
    obj.driver.implicitly_wait(5)
    obj.driver.find_element_by_css_selector("input.bw8_btn_send_btn_input.bw8_btn_enabled.skin_chat_win").click()
    obj.driver.implicitly_wait(5)
    client_get_winid(obj)

#获取客户端的winid="u2_233621_382455118052"
def client_get_winid(obj):
    time.sleep(10)
    global  _clientWinid
    clientWinid = obj.driver.find_element_by_css_selector("div.bw8_chat_content_footet.bw8_chat_content_footet_narrow.bw8_chat_chat_win_chat.dhn_fl").get_attribute("winid")
    _clientWinid = str(clientWinid)
#获取客户端最后一条消息
def client_get_serviceSendInfo(obj):
    #is_visible_css(obj.driver,".bw8_ai_chat > div:last-child .chat_qqface_format")
    # 切换iframe
    obj.driver.switch_to.frame(obj.driver.find_element_by_css_selector("iframe#bw8-chatIframe"))
    time.sleep(5)
    client_message1 = obj.driver.find_element_by_css_selector(".bw8_ai_chat > div:last-child .chat_qqface_format").text
    client_message = str(client_message1).strip()
    print (client_message)
    try:
        assert client_message == _serviceSendMessage
        print("客户端获取的内容和客服端输入的一致")
    except Exception as e:
        print("client_message:"+client_message)
        print("客户端获取的内容和客服端输入的不一致",format(e))


#点击左侧的“在线客服”图标
def service_clickOnLineService(obj):
    obj.driver.implicitly_wait(5)
    obj.driver.find_element_by_css_selector(".icon-chatOnline a").click()
    print("点击左侧的“在线客服”图标：成功")
    obj.driver.implicitly_wait(5)
#点击“当前有*个客户正在排队”
def service_clickLineUp(obj):
    time.sleep(10)
    print("点击“当前有*个客户正在排队:之前")
    obj.driver.switch_to.frame(obj.driver.find_element_by_css_selector("iframe#rightContentIfrIM"))
    print("切换ifrome")
    obj.driver.implicitly_wait(5)
    obj.driver.find_element_by_css_selector("span.showText").click()
    print("点击“当前有*个客户正在排队:成功")
    obj.driver.implicitly_wait(5)
    time.sleep(5)

#获取客服端当前会话数（主动）
def service_get_count_num(obj):
    time.sleep(5)
    count = obj.driver.find_element_by_css_selector("span .chat_online_num").text
    time.sleep(6)
    print (count.strip())
    #一下获取每一个当前会话客服的winid
    for index in range(int(count.strip())):
        # print (index + 1)
        winid_value = obj.driver.find_element_by_css_selector("body > div:nth-child(2) > div.sider_left > div > div.chat-conversation-history > div:nth-child(1) > div.conversation-history-content > div > ul > li:nth-child("+str(index+1)+")").text
        service_winid_value1 = winid_value.split('(')[1].split(')')[0]
        service_winid_value = str(service_winid_value1)
        print (_clientWinid)
        if service_winid_value == _clientWinid:
            obj.driver.find_element_by_css_selector("body > div:nth-child(2) > div.sider_left > div > div.chat-conversation-history > div:nth-child(1) > div.conversation-history-content > div > ul > li:nth-child(" + str(index + 1) + ")").click



#获取客户端发送的消息
def service_getInfo(obj):
    service_get_count_num(obj)
    print("获取客户端发送的消息")
    time.sleep(10)
    error_mes = obj.driver.find_element_by_css_selector("div.text.customtext").text
    print(error_mes)
    try:
        assert error_mes == _sendmessage
        print("客端获取的内容和客户端输入的一致")
    except Exception as e:
        print("客端获取的内容和客户端输入的不一致",format(e))

#客服端发消息
def service_sendInfo(obj):
    is_visible_css(obj.driver,"div[winid="+ _clientWinid +"] .typeahead__holde")
    obj.driver.find_element_by_css_selector("div[winid="+ _clientWinid +"] .typeahead__holde").send_keys(_serviceSendMessage)
    obj.driver.find_element_by_css_selector("div[winid="+ _clientWinid +"] .send-btn").send_keys(Keys.ENTER)



#结束会话
def service_end(obj):
    time.sleep(10)
    #上面切过一次，此处切到iframe是为了窗口切换之后使用
    obj.driver.switch_to.frame(obj.driver.find_element_by_css_selector("iframe#rightContentIfrIM"))
    obj.driver.find_element_by_css_selector("div[winid="+ _clientWinid +"] div.chat-close-bar").click()









