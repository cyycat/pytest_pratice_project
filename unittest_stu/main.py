import os
import unittest
from unittest_stu.interfaceTwo.search_case import Search
from unittest_stu.test_login import Login
# from HTMLTestRunner_PY3 import HTMLTestRunner
from unittest_stu.HTMLTestRunner_cn import HTMLTestRunner


### 方式一：分组测试
def suite():
    suite = unittest.TestSuite()
    suite.addTest(Search('test_case_search_01'))
    suite.addTest(Search('test_case_search_02'))
    print(suite.countTestCases())
    return suite


### 方式二：TestLoader  3种方式加载测试用例，并添加至TestSuite测试套件内
# 1、loadTestsFromName         加载测试类
test_class = ["interfaceTwo.search_case.Search"]
# 2、loadTestsFromTestCase     加载测试类
test_cases = [Login]
# 3、loadTestsFromModule       加载模块
from unittest_stu import test_add


def load_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for i in test_class:
        # 1、loadTestsFromName         加载测试类名称
        tests = loader.loadTestsFromName(i)
        suite.addTests(tests)

    for test_case in test_cases:
        # 2、loadTestsFromTestCase     加载测试类
        tests = loader.loadTestsFromTestCase(test_case)
        suite.addTest(tests)

    # 3、loadTestsFromModule       加载模块
    suite.addTest(loader.loadTestsFromModule(test_add))
    return suite


### 方式三：discover 发现模式匹配文件，
def discover_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    tests = loader.discover(os.path.abspath("."), pattern="test_login*")
    # tests2 = loader.discover(os.path.abspath("."), pattern="*_case.py")
    suite.addTest(tests)
    # suite.addTest(tests2)
    return suite


if __name__ == '__main__':
    # I、通过TextTestRunner().run()执行case
    runner = unittest.TextTestRunner()
    ## 组织case：
    ## 方式一
    # runner.run(suite())
    ## 方式二
    # runner.run(load_tests())
    ## 方式三
    # runner.run(discover_tests())


    # # II、通过TestSuite().run()执行case
    # # 获取测试结果信息
    # result = discover_tests().run(unittest.TestResult())
    # print(f"测试结果为：{result}")
    # print(f"skipped的case有：{result.skipped}")

    tests = discover_tests()
    with open("./unittest_stu/report.html", "wb") as report_file:
        # report_runner = HTMLTestRunner(stream=report_file, title="我的测试报告", description="描述文案内容")
        report_runner = HTMLTestRunner(title="带截图的测试报告", description="小试牛刀",
                               stream=report_file, verbosity=2, retry=1,
                               save_last_try=True)

        report_runner.run(tests)
