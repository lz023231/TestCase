# -*- coding: UTF-8 -*-
class UserPage:

    def __init__(self,driver):
        self.driver = driver



    def click_add_user(self):
        # 点击添加公司
        self.driver.find_element_by_id("btn_addd").click()

    def input_user(self,name):
    # 输入公司名称
        self.driver.find_element_by_id("newCompanyName").send_keys(name)

    def one_company_name(self):
        # 点击排在第一的客户名称
        self.driver.find_element_by_xpath("//*[@data-index='0']/td[2]/a").click()


    def click_Save_company(self):
        # 点击保存公司
        self.driver.find_element_by_xpath("//*[@id='myModal4']/div/div/div[3]/button[2]").click()


    def company(self):
        # 定位编辑公司页面的公司名称
        companyname  = self.driver.find_element_by_id("companyName")
        return companyname.text


    def prompt(self):
        # 添加公司重复提示
        tips = self.driver.find_element_by_xpath('//*[@id="div_tip"]')
        return tips.text

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# """下面方法为定位联系人页面元素方法"""

    def click_add_Contacts(self):
        """点击添加联系人"""
        self.driver.find_element_by_id("createContacter").click()


    def switch_iframe(self):
        """编辑公司页面切换到添加联系人框表单"""
        a = self.driver.find_element_by_id("IVREdit")
        self.driver.switch_to.frame(a)

    def input_Contacts_name(self,name1):
        """联系人姓名"""
        self.driver.find_element_by_xpath("//*[@class='form-horizontal']/div[1]/input[2]").send_keys(name1)

    def input_Contact_position(self,name2):
        """联系人职位"""
        self.driver.find_element_by_xpath("//*[@class='form-horizontal']/div[2]/input[2]").send_keys(name2)

    def input_Contact_number(self,number1):
        """手机号"""
        self.driver.find_element_by_xpath('//input[@type="textfield" and @name = "mobile"]').send_keys(number1)

    def input_Contact_Label(self,label):
        """标签"""
        self.driver.find_element_by_xpath('//*[@id="tags1"]/div/p/span/span[1]/span/ul/li/input').send_keys(label)
        self.driver.find_element_by_xpath('//*[@id="tags1"]/div/p/span/span[1]/span/ul/li/input').click()

    def input_Contact_Telephone(self,number2):
        """联系人电话号码"""
        self.driver.find_element_by_xpath('//input[@type="textfield" and @name = "phone"]').send_keys(number2)

    def input_Contact_email(self,email):
        self.driver.find_element_by_xpath('//input[@type="textfield" and @name = "email"]').send_keys(email)

    def input_Contact_qq(self,qq):
        """联系人qq"""
        self.driver.find_element_by_xpath('//input[@type="textfield" and @name="QQ"]').send_keys(qq)

    def input_Contact_Remarks(self,remarks):
        """联系人备注"""
        self.driver.find_element_by_xpath('//input[@type="textfield" and @name="note"]').send_keys(remarks)

    def click_Save_Contact(self):
        """点击联系人保存"""
        self.driver.find_element_by_xpath("//button[text()='保存']").click()






