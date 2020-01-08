from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

s_w =driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

all_h = driver.window_handles

for handle in all_h:
    if handle != s_w:
        driver.switch_to_window(handle)
        print(driver.title)
        driver.find_element_by_name('userName').send_keys('username')
        driver.find_element_by_name('phone').send_keys('13790000000')
        time.sleep(2)
        driver.close()

driver.switch_to_window(s_w)
print(driver.title)
