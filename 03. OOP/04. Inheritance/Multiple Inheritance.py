class Person:
    @staticmethod
    def sleep():
        return "sleeping..."


class Employee:
    @staticmethod
    def get_fired():
        return "fired..."


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return "teaching..."


teacher = Teacher()
print(teacher.sleep())
print(teacher.get_fired())
print(teacher.teach())