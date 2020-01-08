from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.3wyuming.xyz")

print(driver.get_cookies())

driver.add_cookie({'name':'key_aaaaa','value':'value_bbbb'})
for cookie in driver.get_cookies():
    print("%s>>>>>>%s"%(cookie['name'],cookie['value']))