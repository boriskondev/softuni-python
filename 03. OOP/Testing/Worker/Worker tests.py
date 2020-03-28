import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')


class WorkerTests(unittest.TestCase):
    def test_if_worker_initializes_with_correct_attributes(self):
        name = "Test User"
        salary = 1000
        energy = 10
        test_worker = Worker(name, salary, energy)
        self.assertEqual(test_worker.name, name)
        self.assertEqual(test_worker.salary, salary)
        self.assertEqual(test_worker.energy, energy)
        self.assertEqual(test_worker.money, 0)

    def test_if_worker_energy_increments_after_rest_method_is_called(self):
        name = "Test User"
        salary = 1000
        energy = 10
        test_worker = Worker(name, salary, energy)
        test_worker.rest()
        self.assertEqual(test_worker.energy, energy + 1)

    def test_if_error_rises_when_worker_tries_to_work_with_zero_or_negative_energy(self):
        name = "Test User"
        salary = 1000
        energy = 0
        test_worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            test_worker.work()

        self.assertIsNotNone(context.exception)

        energy = - 10
        test_worker = Worker(name, salary, energy)

        with self.assertRaises(Exception) as context:
            test_worker.work()

        self.assertIsNotNone(context.exception)

    def test_if_worker_money_increase_with_salary_when_work_method_called(self):
        name = "Test User"
        salary = 1000
        energy = 10
        test_worker = Worker(name, salary, energy)
        test_worker.work()
        self.assertEqual(test_worker.money, test_worker.salary)

    def test_if_worker_energy_decreases_after_work_method_is_called(self):
        name = "Test User"
        salary = 1000
        energy = 10
        test_worker = Worker(name, salary, energy)
        test_worker.work()
        self.assertEqual(test_worker.energy, energy - 1)

    def test_if_get_info_method_returns_proper_values(self):
        name = "Test User"
        salary = 1000
        energy = 10
        test_worker = Worker(name, salary, energy)
        actual = test_worker.get_info()
        expected = f"{name} has saved 0 money."
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
