import  unittest

class MyTest(unittest.TestCase):

    @unittest.skip('直接跳过测试')
    def test_skip(self):
        print('aaa')

    @unittest.skipIf(3 > 2,'条件为真跳过测试')
    def test_skip_if(self):
        print('bbb')

    @unittest.skipUnless(3 > 2,'条件为真，执行测试')
    def test_skip_unless(self):
        print('ccc')

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2, 2)

if __name__=='__main__':
    unittest.main()