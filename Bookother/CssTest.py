from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.3wyuming.xyz")
sleep(2)

driver.find_element_by_css_selector("#inputEmail3").send_keys("Admin")
driver.find_element_by_css_selector("#inputPassword3").send_keys("A123123")
driver.find_element_by_xpath("//button[@class='btn btn-default']").click()

print(driver.get_cookies())

driver.add_cookie({'name':'key_aaaaa','value':'value_bbbb'})
for cookie in driver.get_cookies():
    print("%s>>>>>>%s"%(cookie['name'],cookie['value']))

sleep(2)

driver.close()
