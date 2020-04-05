import unittest
from project.factory.paint_factory import PaintFactory


class TestsPaintFactory(unittest.TestCase):
    def test_init_sets_the_correct_attributes(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        self.assertEqual(test_paint_factory.__class__.__name__, "PaintFactory")

    def test_ingredients_attribute_initializes_properly_as_empty_dictionary(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        self.assertEqual(test_paint_factory.ingredients, {})

    def test_add_ingredient_raises_exception_when_wrong_ingredient_type_given(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        with self.assertRaises(TypeError) as context:
            test_paint_factory.add_ingredient("banana", 2)
        self.assertEqual(str(context.exception), "Ingredient of type banana not allowed in PaintFactory")

    def test_add_ingredient_raises_error_when_capacity_is_less_than_quantity(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        with self.assertRaises(ValueError) as context:
            test_paint_factory.add_ingredient("white", 20)
        self.assertEqual(str(context.exception), "Not enough space in factory")

    def test_add_ingredient_sets_new_ingredient_type_quantity_to_given_quantity(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        test_paint_factory.add_ingredient("white", 2)
        self.assertEqual(test_paint_factory.ingredients["white"], 2)

    def test_add_ingredients_sets_new_ingredients_types_quantities_to_given_quantities(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        test_paint_factory.add_ingredient("white", 2)
        test_paint_factory.add_ingredient("blue", 3)
        self.assertEqual(test_paint_factory.ingredients["white"], 2)
        self.assertEqual(test_paint_factory.ingredients["blue"], 3)

    def test_add_ingredient_raises_ingredient_type_quantity_with_given_quantity(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        test_paint_factory.add_ingredient("white", 2)
        test_paint_factory.add_ingredient("white", 4)
        self.assertEqual(test_paint_factory.ingredients["white"], 6)

    def test_remove_ingredient_raises_error_when_no_such_product_to_be_removed(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        test_paint_factory.add_ingredient("white", 5)
        with self.assertRaises(KeyError) as context:
            test_paint_factory.remove_ingredient("black", 7)
        self.assertEqual(str(context.exception), "'No such ingredient in the factory'")

    def test_remove_ingredient_raises_error_when_not_enough_quantity_of_remaining_product_to_be_removed(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        test_paint_factory.add_ingredient("white", 5)
        with self.assertRaises(ValueError) as context:
            test_paint_factory.remove_ingredient("white", 7)
        self.assertEqual(str(context.exception), "Ingredient quantity cannot be less than zero")

    def test_remove_ingredient_quantity_with_given_quantity(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        test_paint_factory.add_ingredient("white", 5)
        test_paint_factory.remove_ingredient("white", 3)
        self.assertEqual(test_paint_factory.ingredients["white"], 2)

    def test_products_property_returns_ingredients(self):
        test_paint_factory = PaintFactory("Charley's", 10)
        self.assertEqual(test_paint_factory.products, test_paint_factory.ingredients)


if __name__ == "__main__":
    unittest.main()