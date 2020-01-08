from yuming import wangye
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.3wyuming.xyz")
sleep(2)

t1 = wangye(driver)

with(open("./date_file/user_info.txt",'r')) as user_file:
     data = user_file.readlines()
users = []
for line  in data:
    user = line[:-1].split(":")
    users.append(user)

