class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Person):
    pass


nemo = Child("Cops", 22)
print(nemo)