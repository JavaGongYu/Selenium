from selenium import webdriver

webdriver = webdriver.Firefox()
webdriver.implicitly_wait(10)
webdriver.maximize_window()
webdriver.get("http://www.baidu.com")
keyword = webdriver.find_element_by_id("kw")
keyword.clear()
keyword.send_keys("山东")
keyword.submit()
products = webdriver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
print("Found " + str(len(products)) + "products:")
for product in products:
    print(product.text)
webdriver.close()
