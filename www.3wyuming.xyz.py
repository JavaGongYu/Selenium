from selenium import webdriver
from time import sleep

driver = webdriver.Chrome() #启动浏览器
driver.get("http://www.3wyuming.xyz") #被测网址

driver.maximize_window() #浏览器最大化
driver.implicitly_wait(2) #休眠
'''
print("title:"+driver.title)
print("URL:"+driver.current_url)

size = driver.find_element_by_id("s").size #获取输入框s的size
print("输入框Size:"+str(size))
driver.find_element_by_id("s").send_keys("发帖") #在输入框s中键入
'''
for i in range(10):
    print("第"+str(i+1)+"次")
    print("Title:"+driver.title)
    print("URL:"+driver.current_url)
    print(" ")
    driver.find_element_by_id("inputEmail3").send_keys("Admin") #在输入框inputEmail3键入
    driver.find_element_by_id("inputPassword3").send_keys("A123123") #在输入框inputPassword3键入
    #print("密码框属性："+driver.find_element_by_id("inputPassword3").get_attribute('id')) #获取元素属性值
    driver.find_element_by_xpath("//button[@class='btn btn-default']").click() #点击按钮
    print("Title:" + driver.title)
    print("URL:" + driver.current_url)
    print(" ")
    driver.find_element_by_link_text('个人资料').click()
    print("Title:" + driver.title)
    print("URL:" + driver.current_url)
    print(" ")
    driver.find_element_by_link_text('退出登录').click()
    print("Title:" + driver.title)
    print("URL:" + driver.current_url)
    print(" ")

