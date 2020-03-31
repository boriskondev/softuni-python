import unittest


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


class TestsCar(unittest.TestCase):
    def setUp(self):
        self.test_car = Car("Mazda", "Mazda6", 1, 10)

    def test_init_initializes_properly(self):
        self.assertEqual(self.test_car.make, "Mazda")
        self.assertEqual(self.test_car.model, "Mazda6")
        self.assertEqual(self.test_car.fuel_consumption, 1)
        self.assertEqual(self.test_car.fuel_capacity, 10)
        self.assertEqual(self.test_car.fuel_amount, 0)

    def test_make_property_returns_make(self):
        expected = "Mazda"
        self.assertEqual(self.test_car.make, expected)

    def test_make_setter_returns_exception_when_no_value(self):
        with self.assertRaises(Exception) as context:
            self.test_car.make = ""

        # Right way
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")
        # Alternative (my assumption), but not sure how correct it is
        # self.assertTrue(context.exception)

    def test_model_property_returns_model(self):
        expected = "Mazda6"
        self.assertEqual(self.test_car.model, expected)

    def test_model_setter_returns_exception_when_no_value(self):
        with self.assertRaises(Exception) as context:
            self.test_car.model = ""

        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_property_returns_fuel_consumption(self):
        expected = 1
        self.assertEqual(self.test_car.fuel_consumption, expected)

    def test_fuel_consumption_setter_returns_exception_when_value_is_zero(self):
        with self.assertRaises(Exception) as context:
            self.test_car.fuel_consumption = 0

        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_setter_returns_exception_when_value_is_below_zero(self):
        with self.assertRaises(Exception) as context:
            self.test_car.fuel_consumption = -10

        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_property_returns_fuel_capacity(self):
        expected = 10
        self.assertEqual(self.test_car.fuel_capacity, expected)

    def test_fuel_capacity_setter_returns_exception_when_value_is_zero(self):
        with self.assertRaises(Exception) as context:
            self.test_car.fuel_capacity = 0

        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_setter_returns_exception_when_value_is_below_zero(self):
        with self.assertRaises(Exception) as context:
            self.test_car.fuel_capacity = -10

        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_property_returns_fuel_amount(self):
        expected = 0
        self.assertEqual(self.test_car.fuel_amount, expected)

    def test_fuel_amount_setter_returns_exception_when_value_is_below_zero(self):
        with self.assertRaises(Exception) as context:
            self.test_car.fuel_amount = -10

        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_method_raises_exception_when_fuel_argument_is_zero(self):
        with self.assertRaises(Exception) as context:
            self.test_car.refuel(0)

        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_method_raises_exception_when_fuel_argument_is_below_zero(self):
        with self.assertRaises(Exception) as context:
            self.test_car.refuel(-10)

        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_method_amount_increases_with_given_fuel(self):
        expected = 2
        self.test_car.refuel(2)
        self.assertEqual(self.test_car.fuel_amount, expected)

    def test_refuel_method_fuel_amount_equals_capacity_when_amount_is_bigger_than_capacity(self):
        expected = 10
        self.test_car.refuel(12)
        self.assertEqual(self.test_car.fuel_amount, expected)

    def test_drive_method_raises_exception_when_needed_fuel_is_bigger_than_fuel_amount(self):
        self.test_car.fuel_amount = 4
        with self.assertRaises(Exception) as context:
            self.test_car.drive(500)

        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")

    def test_drive_method_fuel_amount_decreases_with_needed_fuel_amount(self):
        self.test_car.fuel_amount = 4
        self.test_car.drive(100)
        expected = 3
        self.assertEqual(self.test_car.fuel_amount, expected)


if __name__ == '__main__':
    unittest.main()