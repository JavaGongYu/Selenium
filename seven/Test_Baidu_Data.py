import csv
import codecs
import unittest
from time import sleep
from itertools import islice
from selenium import webdriver

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.url='http://www.baidu.com'
        cls.test_data = []
        with codecs.open('baidu_data.csv','r','utf_8_sig') as f:
            data = csv.reader(f)
            for line in islice(data,1,None):
                cls.test_data.append(line)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def baidu_search(self,search_key):
        self.driver.get(self.url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def test_search_selenium(self):
        self.baidu_search(self.test_data[0][1])

    def test_searcg_unittest(self):
        self.baidu_search(self.test_data[1][1])

    def test_search_python(self):
        self.baidu_search(self.test_data[2][1])

    def test_search_blog(self):
        self.baidu_search(self.test_data[3][1])

if __name__=='__main__':
    unittest.main(verbosity=2)