#-*- coding: UTF-8 -*-
import time
from WebServiceLayer.ticketelement.ticketWait import now_show



class tikcet_rukou():
  def ticket_rukou_click(self,driver):
    # 工单设置进入子目录
      driver.find_element_by_css_selector("[title='设置']").click()
      driver.find_element_by_xpath("//div[contains(text(),'工单设置') and @class='dd-handle dd-title']").click()
      time.sleep(2)
      now_show(driver,"li[class='dd-item']>ol[class='dd-list submenu']")