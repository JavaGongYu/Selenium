from time import sleep

"""
@class:登录退出

@date:2019-11-29

@author:G
"""
class Login_s:

    def __init__(self,driver):
        self.driver = driver

    def login_in(self):
        self.driver.find_element_by_name("username").send_keys("gongyu")
        self.driver.find_element_by_name("password").send_keys("a123123")
        sleep(5)
        self.driver.find_element_by_id('login').click()

    def login_out(self):
        sleep(5)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_link_text('[退出]').click()