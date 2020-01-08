import time
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__=='__main__':
    suits = unittest.defaultTestLoader.discover("./", pattern='Test_Baidu_Data.py')
    shijian = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open('./test_report/'+ shijian +'.result.html','wb')
    ht = HTMLTestRunner(stream=fp, title="百度搜索测试报告", description='Windows 10， Chorme 浏览器')
    ht.run(suits)
    fp.close()