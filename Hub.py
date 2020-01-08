from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver  = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME.copy())
driver.get("http://www.baidu.com")

driver.quit()