from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.3wyuming.xyz:8080/Diary')

driver.find_element_by_name('userName').send_keys("gongyu")
driver.find_element_by_name("password").send_keys('jack')
driver.find_element_by_css_selector('[type="submit"]').click()

sleep(2)

driver.close()