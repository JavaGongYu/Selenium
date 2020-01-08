import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt,data,file_data,unpack

@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.url = "http://www.baidu.com"

    def baidu_search(self,search_key):
        self.driver.get(self.url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    # 参数化使用方式一
    @data(['case1','selenium'],['case2','unittest'],['case3','ddt'],['case4','python'])
    @unpack
    def test_search1(self,case,search_key):
        print('第一组测试用例：',case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+'_百度搜索')

    # 参数化使用方式二
    @data(('case1', 'selenium'), ('case2', 'unittest'), ('case3', 'ddt'), ('case4', 'python'))
    @unpack
    def test_search2(self, case, search_key):
        print('第二组测试用例：', case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    # 参数化读取JSON文件
    @file_data('ddt_data_file.json')
    def test_search3(self,search_key):
        print('第三组测试用例:',search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    # 参数化读取Yaml文件
    @file_data('ddt_data_file.yaml')
    def test_search4(self, case):
        search_key = case[0]["search_key"]
        print('第四组测试用例:', search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()