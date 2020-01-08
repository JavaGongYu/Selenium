import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt,data,file_data,unpack

@ddt # 此处修饰 请注意
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.url='http://www.baidu.com'

    def baidu_search(self,search_key):
        self.driver.get(self.url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    @file_data('data_file.json') # 文件参数化
    def test_search(self,search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()