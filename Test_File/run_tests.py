import unittest
import time
from HTMLTestRunner import HTMLTestRunner

suit = unittest.defaultTestLoader.discover('./test_case',pattern='test_baidu.py')

if __name__ == "__main__":
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    name = './test_report/' + now_time + '.result.html'
    wenjian = open(name,'wb')
    ht = HTMLTestRunner(stream=wenjian,title="测试报告",description="Windows 10 ，Chorme浏览器")
    ht.run(suit)
    wenjian.close()