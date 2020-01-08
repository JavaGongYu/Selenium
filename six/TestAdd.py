import unittest
from six.test_case.calculator import Calculator

class TestAdd(unittest.TestCase):

    def test_add_int(self):
        self.assertEqual(Calculator(3,5).add(),8,'整数相加失败')

    def test_add_decimals(self):
        self.assertEqual(Calculator(1.4,2.6).add(),4,'小数相加失败')

    def test_add_string(self):
        self.assertEqual(Calculator("7","5").add(),12,'字符串相加失败')

if __name__=='__main__':
    unittest.main()