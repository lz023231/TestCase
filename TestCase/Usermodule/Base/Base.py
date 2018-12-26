# -*- coding: UTF-8 -*-
from selenium.webdriver.support.select import Select
from Name import now_time

now_time= now_time()

class BasePage:
    "主要是把几个常用的selenium方法封装到BasePage这个类中"

    # "back()  forward() get() quit()"

    def __init__(self, driver):
        "一个构造函数，param参数driver"

        self.driver = driver

        # 登陆方法
    def Login(self,number, password, cold):


        self.driver.find_element_by_xpath('//*[@id="bw_header"]/div/div[3]/a[1]').click()
        self.driver.find_element_by_xpath("//*[@id='psname']").clear()
        self.driver.find_element_by_xpath("//*[@id='psname']").send_keys(number)
        self.driver.find_element_by_id('pwd').send_keys(password)

        self.driver.find_element_by_xpath("//*[@type = 'safecode']").send_keys(cold)

        self.driver.find_element_by_xpath('//*[@class="bw8_login_btn"]/input').click()

    # 进入企业信息
    def current_mode(self):
        # 点击头像
        self.driver.find_element_by_xpath("//*[@id='rightPanelDiv']/div[1]/nav/div[2]/ul/li[3]/a").click()
        # 点击企业信息
        self.driver.find_element_by_xpath("//*[@id='rightPanelDiv']/div[1]/nav/div[2]/ul/li[3]/ul/li[2]/a").click()

    def information_switch_iframe1(self):
        information =self.driver.find_element_by_id("rightContentIfr")
        self.driver.switch_to.frame(information)

    def print_current_mode(self):
        # 获取当前模式并打印
        mode = self.driver.find_element_by_xpath("//table/tbody/tr[8]/td[2]/select/option[@selected='selected']")
        return mode.text

    def click_2b(self):
        # 切换2b
        current = self.driver.find_element_by_xpath("//select[@name='userMode']")
        Select(current).select_by_index(0)

    def click_2c(self):
        current = self.driver.find_element_by_xpath("//select[@name='userMode']")
        Select(current).select_by_index(1)

    # 点击确定
    def click_sure(self):
        self.driver.find_element_by_xpath("//input[@class='button def btn btn-primary btn-sm' and @value = '确定']").click()


    def img(self):
        self.driver.get_screenshot_as_file("C://Users//HP//PycharmProjects//untitled5//%s_错误.img" % now_time)


    def js(self):
        # 上下滑动滚动条
        js = "window.scrollTo(100,650)"

        self.driver.execute_script(js)

    def switch_home_iframe(self):
        # 切换到原始表单
        self.driver.switch_to.parent_frame()



    def refresh(self):
        # 刷新页面
        self.driver.refresh()


    # 获取当前页面标题
    def title(self):
        self.driver.title()

    def back(self):
        "浏览器后退"

        self.driver.back()

    def forward(self):
        "浏览器前进"

        self.driver.forward()


    def quitBrowser(self):
        self.driver.quit()



