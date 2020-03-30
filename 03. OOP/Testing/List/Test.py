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


class TestsIntegerList(unittest.TestCase):
    def test_init_with_no_arguments_should_create_empty_data(self):
        data = []
        test_list = IntegerList(*data)
        actual = test_list.get_data()
        expected = []
        self.assertEqual(actual, expected)

    def test_init_with_integer_args_should_add_args_to_data(self):
        data = [1, 2, 3]
        test_list = IntegerList(*data)
        actual = test_list.get_data()
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_init_with_none_integer_args_should_not_add_elements_to_data(self):
        data = [1, 2, 3, "Pesho"]
        test_list = IntegerList(*data)
        actual = test_list.get_data()
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_get_data_method_should_return_data_attribute(self):
        data = [1, 2]
        integer_list = IntegerList(*data)
        expected = integer_list._IntegerList__data
        actual = integer_list.get_data()
        self.assertEqual(actual, expected)

    def test_add_element_function_should_add_element_and_return_the_list(self):
        data = [1, 2]
        integer_list = IntegerList(*data)
        integer_list.add(9)
        actual = integer_list.get_data()
        expected = [1, 2, 9]
        self.assertEqual(actual, expected)

    def test_add_element_when_given_string_as_a_value_should_give_value_error(self):
        data = [1, 2]
        integer_list = IntegerList(*data)

        with self.assertRaises(Exception) as context:
            integer_list.add("Test")

        self.assertTrue(context.exception)

    def test_remove_valid_index_to_remove_element_on_given_index_and_should_return_it(self):
        data = [1, 2, 3]
        integer_list = IntegerList(*data)
        expected = 2
        actual = integer_list.remove_index(1)
        self.assertEqual(actual, expected)

    def test_remove_index_when_given_index_out_of_range_should_give_IndexError(self):
        data = [1, 2, 3, 4, 5]
        integer_list = IntegerList(*data)
        with self.assertRaises(Exception) as context:
            integer_list.get(5)

        self.assertTrue(context.exception)

    def test_remove_valid_index_should_delete_element_from_data(self):
        data = [1, 2, 3, 4, 5]
        integer_list = IntegerList(*data)
        integer_list.remove_index(2)
        actual = integer_list.get_data()
        expected = [1, 2, 4, 5]
        self.assertEqual(actual, expected)

    def test_get_method_invalid_index_should_give_error(self):
        data = [1, 2, 3, 4, 5]
        integer_list = IntegerList(*data)
        with self.assertRaises(Exception) as context:
            integer_list.remove_index(10)

        self.assertTrue(context.exception)

    def test_get_method_valid_index_should_return_element(self):
        data = [1, 2, 3, 4, 5]
        integer_list = IntegerList(*data)
        actual = integer_list.get(len(data) - 1)
        expected = 5
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()