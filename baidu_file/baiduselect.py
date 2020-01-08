from time import sleep
from  selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
link = driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)
sel = driver.find_element_by_xpath("//select[@id='nr']")

Select(sel).select_by_value('20')
sleep(2)

Select(sel).select_by_visible_text("每页显示50条")
sleep(2)

Select(sel).deselect_by_index(0)
sleep(2)