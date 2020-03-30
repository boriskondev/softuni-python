import unittest


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class WorkerTests(unittest.TestCase):
    def test_1(self):
        # Cat's size is increased after eating
        catty = Cat("Snoopy")
        catty.eat()
        self.assertEqual(catty.size, 1)

    def test_2(self):
        # Cat is fed after eating
        catty = Cat("Snoopy")
        catty.eat()
        self.assertTrue(catty.fed)

    def test_3(self):
        # Cat cannot eat if already fed, raises an error
        catty = Cat("Snoopy")
        catty.eat()

        with self.assertRaises(Exception) as context:
            catty.eat()

        self.assertTrue(context.exception)

    def test_4(self):
        # Cat cannot fall asleep if not fed, raises an error
        catty = Cat("Snoopy")

        with self.assertRaises(Exception) as context:
            catty.sleep()

        self.assertTrue(context.exception)

    def test_5(self):
        # Cat is not sleepy after sleeping
        catty = Cat("Snoopy")
        catty.eat()
        catty.sleep()
        self.assertFalse(catty.sleepy)


if __name__ == '__main__':
    unittest.main()