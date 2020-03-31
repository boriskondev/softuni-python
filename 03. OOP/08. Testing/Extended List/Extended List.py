import unittest


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class TestsIntegerList(unittest.TestCase):
    def test_out_or_range_index_throws_index_error(self):
        data = [1, 2, 3]
        test_list = IntegerList(*data)

        with self.assertRaises(Exception) as context:
            test_list.insert(3, 4)

        self.assertTrue(context.exception)

    def test_not_integer_element_throws_value_error(self):
        data = [1, 2, 3]
        test_list = IntegerList(*data)

        with self.assertRaises(Exception) as context:
            test_list.insert(0, "Pesho")

        self.assertTrue(context.exception)

    def test_add_value_with_correct_index_and_element(self):
        data = [1, 2, 3]
        test_list = IntegerList(*data)
        test_list.insert(0, 0)
        actual = test_list.get_data()
        expected = [0, 1, 2, 3]
        self.assertEqual(actual, expected)

    def test_get_biggest_returns_biggest_value(self):
        data = [1, 2, 3]
        test_list = IntegerList(*data)
        actual = test_list.get_biggest()
        expected = 3
        self.assertEqual(actual, expected)

    def test_get_index_of_valid_element_in_list(self):
        data = [1, 2, 3]
        test_list = IntegerList(*data)
        actual = test_list.get_index(2)
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()