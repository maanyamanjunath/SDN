import unittest
from add import add_numbers

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numbers(5, 6), 11)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
