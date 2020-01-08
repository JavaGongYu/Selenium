import unittest
from poium import Page, PageElement
from selenium import webdriver


class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_='su')
.





class TestBaidu(unittest.TestCase):
    """百度搜索测试用例"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url='http://www.baidu.com'

    def baidu_search(self,key):
        page = BaiduPage(self.driver)
        self.driver.get(self.url)
        page.search_input=key
        page.search_button.click()

    def test_baidu_search_case1(self):
        key='selenium'
        self.baidu_search(key)

    def test_baidu_search_case2(self):
        key = 'python'
        self.baidu_search(key)

    def test_baidu_search_case3(self):
        key = 'blog'
        self.baidu_search(key)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main':
    unittest.main(verbosity=2)