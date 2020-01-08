from eight.baidu_page import BaiduPage
import unittest
class TestBaidu(unittest.TestCase):
    def test_baidu_search(self):
        page = BaiduPage(self.driver)
        page.get("http://www.baidu.com")
        page.search_input="selenium"
        page.search_button.click()