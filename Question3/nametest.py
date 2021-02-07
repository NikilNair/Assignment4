import unittest

from name import full_name

class EmptyList(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can take numbers
        """
        result = full_name(1, 2)
        self.assertEqual(result, "12")

class EmptyString(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can take empty strings
        """

        result = full_name("", "")
        self.assertEqual(result, "")

class TestBools(unittest.TestCase):
    #@unittest.expectedFailure
    def test_list_int(self):
        """
        Test that it can handle booleans
        """
        result = full_name(True, False)
        self.assertEqual(result, "TrueFalse")


if __name__ == '__main__':
    unittest.main()
