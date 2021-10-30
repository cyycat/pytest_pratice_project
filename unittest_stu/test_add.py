import unittest
import logging
logging.basicConfig(level=logging.INFO)

class Add(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info("setUpClass--------")

    @classmethod
    def tearDownClass(cls):
        logging.info("--------tearDownClass")

    def test_case_add_01(self):
        logging.info("start run test_case_add_01")
        self.assertIn("test", "testing", msg="判断包含")
        logging.info("end run test_case_add_01")

    def test_case_add_02(self):
        logging.info("start run test_case_add_02")
        self.assertEqual(1, 1, msg="判断相等")
        logging.info("end run test_case_add_02")

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            # self.assertEqual(i % 2, 0)
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


if __name__ == '__main__':
    unittest.main()