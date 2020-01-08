from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://saudi.souq.com/sa-en/auth_portal.php?action=index")
driver.maximize_window()
sleep(2)

driver.find_element_by_id("email").send_keys("guzongren@outlook.com")
driver.find_element_by_id("siteLogin").click()
sleep(2)

driver.find_element_by_id("password").send_keys("123456wp")
driver.find_element_by_id("siteLogin").click()
sleep(2)

new_window = "window.open('https://sell.souq.com/fbs-inventory');"
driver.execute_script(new_window)

driver.implicitly_wait(2)

driver.find_element_by_xpath("//*[@id='main']/section/div[2]/div[4]/div[1]/div/div/div[3]/div[1]/div[1]/div/ng-include/div/div/div[3]/select").click()
driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[4]/div[1]/div/div/div[3]/div[1]/div[1]/div/ng-include/div/div/div[3]/select/option[5]').click()


