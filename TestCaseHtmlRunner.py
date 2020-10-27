import unittest
from LyyPackage.TestCase import Test
from LyyPackage.HTMLTestRunner import HTMLTestRunner

class Test_runner(unittest.TestCase):
    def test_suit(self):
        mysuit = unittest.TestSuite()
        case_list = []
        for i in range(1, 16):
            case_list.append('test_' + str(i).rjust(3, '0'))

        for case in case_list:
            mysuit.addTest(Test(case))

        with open('report.html','wb') as f:
            HTMLTestRunner(
                stream = f,
                title = '测试结果-李泳玉',
                description = '对于进销存管理系统的一些测试',
                verbosity = 2
            ).run(mysuit)

if __name__ == '__main__':
    unittest.main()