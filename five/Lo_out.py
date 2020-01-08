class login_out:
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element_by_id("inputEmail3").send_keys(username)
        self.driver.find_element_by_id("inputPassword3").send_keys(password)
        self.driver.find_element_by_xpath("//button[@class='btn btn-default']").click()

    def logout(self):
        self.driver.find_element_by_link_text('个人资料').click()
        self.driver.find_element_by_link_text('退出登录').click()