import unittest

from avg import get_avg

class EmptyList(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can take an empty list
        """
        result = get_avg([])
        self.assertEqual(result, 0)

class TestZeroDiv(unittest.TestCase):
    @unittest.expectedFailure
    def test_list_int(self):
        """
        Test that it can error if invalid input is entered
        """

        result = get_avg([0,0,0,0])
        self.assertEqual(result, ZeroDivisionError)

class TestStrings(unittest.TestCase):
    @unittest.expectedFailure
    def test_list_int(self):
        """
        Test that it can handle strings instead of numbers
        """
        result = get_avg(["Hello", "World"])
        self.assertEqual(result, TypeError)


if __name__ == '__main__':
    unittest.main()
