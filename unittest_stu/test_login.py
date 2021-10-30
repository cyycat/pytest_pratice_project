import unittest
import logging
logging.basicConfig(level=logging.INFO)

def setUpModule():
    print('setUpModule >>>>>>>>>>>>>>开始')
def tearDownModule():
    print("tearDownModule >>>>>>>>>>>>>>结束")


class Login(unittest.TestCase):


    def test_case_login_01(self):
        logging.info("start run test_case_login_01")
        self.assertIn("test", "testing", msg="判断包含")
        logging.info("end run test_case_login_01")

    def test_case_login_02(self):
        logging.info("start run test_case_login_02")
        self.assertEqual(1, 1, msg="判断相等")
        logging.info("end run test_case_login_02")

    # 直接跳过，不执行
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # 条件符合，跳过不执行
    @unittest.skipIf(1+1==2, reason="条件符合，跳过不执行")
    def test_case_login_03(self):
        logging.info("start run test_case_login_03")
        self.assertIs("test", "test")
        logging.info("end run test_case_login_03")

    # 条件符合，才执行
    @unittest.skipUnless(1+1==2, "条件符合，才执行")
    def test_windows_support(self):
        logging.info("test_windows_support")

    # 预期失败
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(0, 0, "broken")


    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        # for i in range(0, 6):
        #     # self.assertEqual(i % 2, 0)
        #     with self.subTest(i=i):    # subTest()上下文管理器，解决执行一次失败后会继续执行，并将诊断错误打印出来
        #         self.assertEqual(i % 2, 0)
        i = 10
        self.subTest(i=i)
        self.assertEqual(i%3, 0)

        j = 20
        self.subTest(j=j)
        self.assertEqual(j % 3, 0)




if __name__ == '__main__':
    unittest.main()

    # 命令行执行
    # python -m unittest test_login.py
    # python -m unittest test_login.py interfaceTwo/test_search.py
    # python -m unittest test_login.Login.test_case_01
