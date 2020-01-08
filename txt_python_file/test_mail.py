from selenium import webdriver
from time import sleep
from module import Mail

driver = webdriver.Chrome()
driver.get("http://www.3wyuming.xyz")
sleep(2)

mail = Mail(driver)
mail.login()

sleep(5)

mail.logout()

