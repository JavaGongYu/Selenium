from selenium import webdriver
from time import sleep
from gw_file.Login import Login_s
from gw_file.kehuguanli import khgl

driver = webdriver.Chrome()
driver.get("http://172.31.1.171:8055/")
driver.maximize_window()

sleep(5)

Test  = Login_s(driver)

Test.login_in()

sleep(5)

khTest=khgl(driver)
khTest.kehuguanl()
sleep(2)

Test.login_out()

driver.close()


