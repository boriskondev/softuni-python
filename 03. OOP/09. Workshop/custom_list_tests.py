import unittest
from .custom_list import CustomList


class CustomListTests(unittest.TestCase):
    def setUp(self):
        self.test_list = CustomList()

    def test_1(self):
        data = 2
        self.test_list.append(data)
        expected = [2]
        self.assertEqual(self.test_list.sequence, expected)


if __name__ == '__main__':
    unittest.main()
