import unittest
from leap_year import LeapYear

class TestLeapYear(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(">>>>>>>>>闰年测试开始<<<<<<<<<")

    @classmethod
    def tearDownClass(cls) -> None:
        print(">>>>>>>>>闰年测试结束<<<<<<<<<")

    def test_2000(self):
        ly = LeapYear(2000)
        self.assertEqual(ly.answer(),"2000是闰年")

    def test_2004(self):
        ly = LeapYear(2004)
        self.assertEqual(ly.answer(),"2004是闰年")

    def test_2017(self):
        ly = LeapYear(2017)
        self.assertEqual(ly.answer(),"2017不是闰年")

    def test_2100(self):
        ly = LeapYear(2100)
        self.assertEqual(ly.answer(),"2100不是闰年")

if __name__=='__main__':
    unittest.main()