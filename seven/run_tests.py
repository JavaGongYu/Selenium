import unittest
import time
import yagmail
from HTMLTestRunner import HTMLTestRunner

def send_email(report):
    server = yagmail.SMTP(user='15554421975@163.com',password='gy961117',host="smtp.163.com")
    server.send('15554421975@163.com', '自动化测试报告', '请查看附件',report)
    print("邮件已发送...")

if __name__=='__main__':
    tear_dir = './test_case'
    suits = unittest.defaultTestLoader.discover(tear_dir, pattern='test*.py')
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    html_report='./test_report/'+ now_time +'.result.html'
    fp = open(html_report,'wb')
    ht = HTMLTestRunner(stream=fp,title="百度搜索测试报告",description='Windows 10， Chorme 浏览器')
    ht.run(suits)
    fp.close()
    send_email(html_report)