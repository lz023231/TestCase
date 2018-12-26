
#-*- coding: UTF-8 -*-
from WebServiceLayer.Ticketcircuit.ticketWait import now_show,not_show


#输入模板内容
def shurumobanxinxi(obj,driver,mobanmingcheng,mobanmiaoshu):
    driver.find_element_by_css_selector("[name='e1pov_act']").click()
    not_show(driver,"[name='ticketTemplateName']")
    not_show(driver,"[name='ticketTemplateDescription']")
    not_show(driver,"[name='availabilityPart']")
    driver.find_element_by_css_selector("[name='ticketTemplateName']").send_keys(mobanmingcheng)
    driver.find_element_by_css_selector("[name='ticketTemplateDescription']").send_keys(mobanmiaoshu)
    #选择可见范围，默认是当前客服
    #driver.find_element_by_css_selector("[name='availabilityPart']").send_keys(data2)
    not_show(driver,"[id ='selectColumn']")


#模板中添加某字段
def ticket_add_templet_ziduan(obj,driver,csslujing,ziduanname,ziduanleiixng):
    ziduanname1 = str(ziduanname).strip()
    ziduanleiixng1 = str(ziduanleiixng).strip()
    driver.find_element_by_css_selector("[id ='selectColumn']").click()
    not_show(driver, "[id='div_columnInfo']")
    target_elem = driver.find_element_by_css_selector(csslujing)
    driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
    #选择你想要的那个字段
    driver.find_element_by_css_selector(csslujing).click()
    driver.find_element_by_css_selector("[onclick ='showTableList()']").click()
    #添加的字段在模板列表中展示
    customnametext1 = driver.find_element_by_css_selector("tbody[class='info']>tr>td:last-child").text
    customname = str(customnametext1).strip()
    # 选择字段的时候  有添加的这个字段名称
    try:
        assert customname == ziduanname1
        print("添加字段成功")
    except Exception as e:
        print("添加字段不成功", format(e))
    driver.find_element_by_css_selector("[name='btnSubmit']").click()
    # 判断选择字段后出现在模板列表中
    customname1text1 = driver.find_element_by_css_selector(
        "table[class='table']>tbody[class='info']>tr:last-child>td:first-child").text
    customname1 = str(customname1text1).strip()
    try:
        assert customname1 == ziduanleiixng1
        print("添加字段成功")
    except Exception as e:
        print("添加字段不成功", format(e))
    driver.switch_to_default_content()

#遍历查找模板名称进入模板编辑页面
def ticket_jinru_moumoban(obj,driver,mobanname):
    elements = driver.find_elements_by_css_selector("tr>td[class='temName']")
    print(type(elements))
    templetnumber = len(elements)
    for index in range(int(templetnumber)):
        # index
        print(index + 3)
        templet_value = driver.find_element_by_css_selector("tbody>tr:nth-child('+str(index+3)+')>td[class='temName']").text
        templet_value_name = str(templet_value)
        print (templet_value_name)
        if templet_value_name == mobanname:
            driver.find_element_by_css_selector("tbody>tr:nth-child('+str(index+3)+')>td[class='text_right_img']>a:nth-child(2)>img").click()
    now_show(driver, "[name='ticketTemplateName']")
#添加模板中的字段


