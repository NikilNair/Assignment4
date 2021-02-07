import unittest

from cube import get_volume

class TestNegative(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can cube a negative number
        """
        result = get_volume(-3)
        self.assertEqual(result, -27)

class TestErr(unittest.TestCase):
    @unittest.expectedFailure
    def test_list_int(self):
        """
        Test that it can error if invalid input is entered
        """

        result = get_volume("apple")
        self.assertEqual(result, TypeError)

class Testdecimal(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can cube a decimal number
        """
        result = get_volume(2.5)
        self.assertEqual(result, 15.625)






if __name__ == '__main__':
    unittest.main()
