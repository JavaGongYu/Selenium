import unittest

suits = unittest.defaultTestLoader.discover('./test_case',pattern='test*.py')

if __name__=='__main__':
    unittest.TextTestRunner().run(suits)