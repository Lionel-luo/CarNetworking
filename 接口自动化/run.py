import unittest
from 接口自动化.test_case.case import test_notoken
from 接口自动化.test_case.case import test_token

suite = unittest.TestSuite()
suite.addTest(test_notoken.TestNotoken('test_login'))
suite.addTest(test_notoken.TestNotoken('test_forget'))
suite.addTest(test_notoken.TestNotoken('test_news'))
suite.addTest(test_token.TestToken('test_password'))
suite.addTest(test_token.TestToken('test_star'))
suite.addTest(test_token.TestToken('test_serve'))

if __name__ == '__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
