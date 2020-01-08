from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(5)

driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text('搜索设置').click()
sleep(2)

driver.find_element_by_class_name('prefpanelgo').click()

alert = driver.switch_to_alert()

alert_text = alert.text
print(alert_text)

sleep(2)

alert.accept()
