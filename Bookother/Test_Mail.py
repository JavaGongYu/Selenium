from selenium import webdriver
from time import sleep
from yuming import wangye

driver = webdriver.Chrome()
driver.get("http://www.3wyuming.xyz")
sleep(2)

diaoyong  = wangye(driver)

diaoyong.login()

sleep(5)

diaoyong.loginout()

