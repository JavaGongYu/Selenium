from time import sleep

"""
@class:客户管理相关操作

@date:2019-11-29

@author:G
"""

class khgl():

    def __init__(self,khgldriver):
        self.driver = khgldriver

    def kehuguanl(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector('[data-index="1"]').click()
        self.driver.switch_to.frame(1) # 客户管理
        self.driver.find_element_by_xpath("//a[@id='add']/i").click()
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2) # 新增信息
        self.driver.find_element_by_id("nameEn").send_keys('Test001')
        self.driver.find_element_by_id("departName").send_keys("测试")
        self.driver.find_element_by_id("countryOfEnterprise").send_keys("中国")
        self.driver.find_element_by_id("corporateCreditLevel").send_keys("A")
        self.driver.find_element_by_id("checkCreditLevel").send_keys("A")
        self.driver.find_element_by_id("registeredAddress").send_keys("T省e市s区t街道")
        self.driver.find_element_by_id("contactName").send_keys("Test")
        self.driver.find_element_by_id("contactWay").send_keys("0531110")
        sleep(3)
        self.driver.find_element_by_id('qualification').click()
        self.driver.find_element_by_id('addSome').click()
        self.driver.find_element_by_id('qualificationCode').send_keys('Test001')
        self.driver.find_element_by_id('qualificationName').send_keys('Test')
        self.driver.find_element_by_id('qualificationType').send_keys('Test')
        registrationTime = "document.getElementById('registrationTime').removeAttribute('readonly')"
        self.driver.execute_script(registrationTime)
        qualificationStartTime = "document.getElementById('qualificationStartTime').removeAttribute('readonly')"
        self.driver.execute_script(qualificationStartTime)
        qualificationEndTime = "document.getElementById('qualificationEndTime').removeAttribute('readonly')"
        self.driver.execute_script(qualificationEndTime)
        self.driver.find_element_by_id('registrationTime').send_keys("2019-11-29")
        self.driver.find_element_by_id('qualificationStartTime').send_keys('2019-11-29')
        self.driver.find_element_by_id('qualificationEndTime').send_keys('2019-11-29')
        self.driver.find_element_by_css_selector("[i-id='ok']").click()
        sleep(3)
        self.driver.find_element_by_id("saveDepart").click()
        sleep(3)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_link_text("供应商管理").click()
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_xpath("//tr[@id='1097']/td[3]/div/span").click()#span[2]删除操作 span 为编辑
        self.driver.find_element_by_xpath("//span[contains(.,'OFF')]")
        self.driver.find_element_by_id("saveDepart").click() #保存
        # 删除弹窗确定按钮
        # self.driver.find_element_by_xpath("/html/body/div[3]/div/table/tbody/tr[3]/td/div[2]/button[2]").click()
    def kehuguanli(self):
        self.driver.find_element_by_link_text("客户管理").click()

    def fuwushang(self):
        self.driver.find_element_by_link_text("物流服务商").click()