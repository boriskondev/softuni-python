from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    additional_consumption = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + self.additional_consumption):
            self.fuel_quantity -= distance * (self.fuel_consumption + self.additional_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    additional_consumption = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + self.additional_consumption):
            self.fuel_quantity -= distance * (self.fuel_consumption + self.additional_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
