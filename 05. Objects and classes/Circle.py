class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def calculate_circumference(self):
        return 2 * self.__pi * self.radius

    def calculate_area(self):
        return self.__pi * self.radius ** 2

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * self.__pi * self.radius ** 2