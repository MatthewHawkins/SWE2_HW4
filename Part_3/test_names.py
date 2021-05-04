import generate_name as names
import unittest

class test_names(unittest.TestCase):
    def test_name_1(self):
        self.assertEqual(names.create_name("Matthew", "Hawkins"), "Matthew Hawkins")
    def test_name_2(self):
        self.assertEqual(names.create_name("123", "456"), "ERROR")
    def test_name_3(self):
        self.assertEqual(names.create_name("", ""), "ERROR")


if __name__ == "__main__":
    unittest.main()