from calculator import Calculator
import unittest
class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(">>>>>>>>>计算测试开始<<<<<<<<<")

    @classmethod
    def tearDownClass(cls) -> None:
        print(">>>>>>>>>计算测试结束<<<<<<<<<")

    def test_add(self):
        self.assertEqual(Calculator(3,5).add(),8,'加法错误')

    def test_sub(self):
        self.assertEqual(Calculator(7,2).sub(),5,'减法错误')

    def test_mul(self):
        self.assertEqual(Calculator(3,3).mul(), 10,'乘法错误')

    def test_div(self):
        self.assertEqual(Calculator(6,2).div(),3,'除法错误')

if __name__ == '__main__':
    unittest.main()