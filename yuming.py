class wangye:
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        self.driver.find_element_by_id("inputEmail3").send_keys("Admin")
        self.driver.find_element_by_id("inputPassword3").send_keys("A123123")
        self.driver.find_element_by_xpath("//button[@class='btn btn-default']").click()

    def loginout(self):
        self.driver.find_element_by_link_text('个人资料').click()
        self.driver.find_element_by_link_text('退出登录').click()