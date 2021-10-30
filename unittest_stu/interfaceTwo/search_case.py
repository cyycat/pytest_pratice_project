import unittest
import logging
logging.basicConfig(level=logging.INFO)

class Search(unittest.TestCase):

    def setUp(self):
        logging.info("setUp...")

    def test_case_search_01(self):
        logging.info("start run test_case_search_01")
        self.assertTrue(1+1==2, msg="判断表达式为真")
        logging.info("end run test_case_search_01")

    def test_case_search_02(self):
        logging.info("start run test_case_search_02")
        self.assertFalse(1+1==1, msg="判断表达式为假")
        logging.info("end run test_case_search_02")

    def tearDown(self):
        logging.info("...tearDown")

if __name__ == '__main__':
    unittest.main()