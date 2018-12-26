#-*- coding: UTF-8 -*-
#查询器
import time
from selenium.webdriver.support.select import Select
from WebServiceLayer.ticketelement.ticketWait import now_show,not_show


class querierlist():
    def add_querier(self,driver,customname,queriername,querierdescription):
        driver.find_element_by_css_selector()
        driver.find_element_by_xpath("//a[contains(text(),'工单查询器')]").click()
        #进入iframe id="rightContentIfr"
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe#rightContentIfr"))
        time.sleep(2)
        not_show(driver,"[class='glyphicon glyphicon-plus']")
        driver.find_element_by_css_selector("[class='glyphicon glyphicon-plus']").click()
        text5=driver.find_element_by_css_selector("[class='glyphicon glyphicon-plus']").text
        print(text5)
        now_show(driver,"[name='ticketName']")
        now_show(driver,"[name='ticketDescription']")
        driver.find_element_by_css_selector("[name='ticketName']").click()
        driver.find_element_by_css_selector("[name='ticketName']").send_keys(queriername)
        driver.find_element_by_css_selector("[name='ticketDescription']").click()
        driver.find_element_by_css_selector("[name='ticketDescription']").send_keys(querierdescription)
        now_show(driver,"[id='RequiredPOVItem']")
        #判断满足任意以下条件中有添加的文本字段
        driver.find_element_by_css_selector("[name='RequiredPSelect[0]']").click()
        s=driver.find_element_by_css_selector("[name='RequiredPSelect[0]']")
        Select(s).select_by_visible_text(customname)#通过文本值定位
        #[name="OptionalPSelect[0]"]
        #判断满足任意以下条件中有添加的文本字段
        s = driver.find_element_by_css_selector("[name='OptionalPSelect[0]']")
        Select(s).select_by_visible_text(customname)  # 通过文本值定位
        #等待元素出现#form-group_container1 > div:nth-last-child(1)
        target_elem1 = driver.find_element_by_css_selector("#form-group_container1>div:nth-last-child(1)")
        driver.execute_script("return arguments[0].scrollIntoView();", target_elem1)
        #获取最后文本的值是什么
        wenbenshuju=driver.find_element_by_css_selector("#form-group_container1>div:nth-last-child(1)>span:nth-child(2)").text
        try:
            assert wenbenshuju==customname
            print("选择正确")
        except Exception as e:
            print(e)
        #获取这个选择字段的类型
        webenleixing=driver.find_element_by_css_selector("#form-group_container1>div:nth-last-child(1)>span:nth-child(3)")
        try:
            assert wenbenshuju == "文本"
            print("类型正确")
        except Exception as e:
                print(e)
        #选取这个文本字段在查询器中展示
        driver.find_element_by_css_selector("#form-group_container1>div:nth-last-child(1)>input[type='checkbox']").click()
        driver.find_element_by_css_selector("[id='selectColumnSubmint']").click()
        #获取视图选择后的判断
        wenbenshuju1=driver.find_element_by_css_selector("tbody[class='info']>tr:last-child>td:first-child").text
        try:
            assert wenbenshuju1 == customname
            print("类型正确")
        except Exception as e:
                print(e)
        webenleixing1=driver.find_element_by_css_selector("tbody[class='info'']>tr:last-child>td:nth-child(2)").text
        try:
            assert webenleixing1 == "文本"
            print("类型正确")
        except Exception as e:
                print(e)
        driver.find_element_by_css_selector("[name='btnSubmit']").click()
        time.sleep(5)
        chaxunqiname=driver.find_element_by_css_selector("div[class='col-lg-12 animated fadeInRight']>div:nth-child(3) tbody>tr:nth-child(1)>td:nth-child(2)").text
        querierdescriptionname=driver.find_element_by_css_selector("div[class='col-lg-12 animated fadeInRight']>div:nth-child(3) tbody>tr:nth-child(1)>td:nth-child(3)").text
        try:
            assert chaxunqiname == queriername
            print("查询器标题保存没问题")
        except Exception as e:
                print(e)
        time.sleep(5)
        try:
            assert querierdescriptionname == querierdescription
            print("查询器描述保存没问题")
        except Exception as e:
                print(e)
        time.sleep(5)
        #获取获取查询器的个数  现在只获取数字  但是现在获取的是全部的信息
        querier = driver.find_element_by_css_selector("#page-wrapper>div>div:nth-child(2)>table>tbody>tr:nth-child(1)> td").text
        queriercount=querier[7:8]#这里得再调整一下
        print (queriercount)
        #获取活动的查询器的名称 进行遍历对比
        for index in range(int(queriercount.strip())):
            # print (index + 1)
            #这里得做一次处理取出错不包括空格的数据 但是现在获取的是有空格的信息
            querier_value = driver.find_element_by_css_selector("div[class='col-lg-12 animated fadeInRight']>div:nth-child(3) tbody>tr:nth-child('+ str(index+1)+')>td:nth-child(2)").text
            service_winid_value = querier_value.split('(')[1].split(')')[0]
            try:
                assert service_winid_value ==chaxunqiname
            except Exception as e:
                print(e)
                print("新建的查询器未出现在活动的列表中")

        # 获取失效的查询器的个数  只获取数字  但是现在获取的是全部的信息
        querier1 = driver.find_element_by_css_selector("#page-wrapper>div>div:nth-child(2)>table>tbody>tr:nth-child(1)> td").text
        queriercount1 = querier1[7:8]  # 这里得再调整一下
        # 获取非活动的查询器的名称 进行遍历对比
        for index in range(int(queriercount1.strip())):
                # print (index + 1)
                # 这里得做一次处理取出错不包括空格的数据 但是现在获取的是有空格的信息
            querier_value = driver.find_element_by_css_selector("div[class='col-lg-12 animated fadeInRight']>div:nth-child(3) tbody>tr:nth-child('+ str(index+1)+')>td:nth-child(2)").text
            service_winid_value = querier_value.split('(')[1].split(')')[0]
            try:
                assert service_winid_value != chaxunqiname
            except Exception as e:
                print(e)
                print("新建的查询器出现在非活动的列表中")

    def shixiao_querier(self, driver, customname, queriername, querierdescription):
        driver.find_element_by_css_selector











