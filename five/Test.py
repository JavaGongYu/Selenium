from time import sleep
from selenium import webdriver
from five.Lo_out import login_out

with(open("../date_file/user_info.txt",'r')) as user_file:
     data = user_file.readlines()
users = []
for line  in data:
    user = line[:].split(":")
    users.append(user)

driver = webdriver.Chrome()
driver.get("http://www.3wyuming.xyz")


driver.implicitly_wait(2)

lo_out_test = login_out(driver)

lo_out_test.login(users[3][0],users[3][1])
print(users[3][0],users[3][1])

sleep(5)

lo_out_test.logout()

lo_out_test.login("GongYu",'A123123')

sleep(5)

lo_out_test.logout()
