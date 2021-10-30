import unittest
import os

if __name__ == '__main__':
    # 方式一：
    # suite = unittest.TestSuite()
    # suite.addTests([Login("test_case_login_01"), Login("test_fail")])
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # # 方式二：loadTestsFromModule
    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # tests = loader.loadTestsFromModule(test_add)
    # suite.addTest(tests)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # # 方式三：loadTestsFromTestCase
    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # tests = loader.loadTestsFromTestCase(search_case.Search)
    # suite.addTest(tests)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 方式四：
    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # tests = loader.loadTestsFromName("interfaceTwo.search_case.Search")
    # suite.addTest(tests)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.discover(os.path.abspath("."), pattern="test_*")
    suite.addTest(tests)
    result = unittest.TestResult()
    result = suite.run(result)

    print(result.skipped)











