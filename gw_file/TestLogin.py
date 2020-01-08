from selenium import webdriver
from time import sleep
from gw_file.Login import Login_s

driver = webdriver.Chrome()
driver.get("http://172.31.1.171:8055/")
sleep(5)

Test  = Login_s(driver)

Test.login_in()

sleep(5)

Test.login_out()

driver.close()