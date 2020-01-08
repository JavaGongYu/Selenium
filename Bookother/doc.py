"""
name：第一个selenium脚本
author：Gy
date:2019-11-21
"""
# coding:utf-8

from selenium import webdriver # 导入selenium下webdriver模块
from time import sleep #导入time下sleep

driver = webdriver.Chrome() #使用谷歌浏览器进行测试
# driver = webdriver.Firefox() #使用火狐浏览器进行测试
driver.get("http://www.baidu.com") # 被测网址

driver.find_element_by_id("kw").send_keys("www.3wyuming.xyz") # 找到输入框输入关键字
driver.find_element_by_id("su").click() # 点击搜索

sleep(5) # 休眠
driver.close() #关闭浏览器
#driver.quit()

