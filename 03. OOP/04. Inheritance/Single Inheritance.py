class Animal:
    @ staticmethod
    def eat():
        return "eating..."


class Dog(Animal):
    @ staticmethod
    def bark():
        return "barking..."


doggo = Dog()
print(doggo.bark())
print(doggo.eat())