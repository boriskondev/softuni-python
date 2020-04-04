class CustomList:
    def __init__(self, *args):
        self.sequence = [arg for arg in args]

    def __repr__(self):
        return f"{self.sequence}"

    def append(self, value):
        self.sequence += [value]
        return self.sequence

    def remove(self, index):
        if index >= len(self.sequence):
            raise IndexError("This index does not exist!")
        return self.sequence.pop(index)

    def get(self, index):
        if index >= len(self.sequence):
            raise IndexError("This index does not exist!")
        return self.sequence[index]

    def extend(self, iterable):
        iterable_data = [x for x in iterable]
        self.sequence += iterable_data
        return self.sequence

    def insert(self, index, value):
        if index >= len(self.sequence):
            raise IndexError("This index does not exist!")
        return self.sequence[:index] + [value] + self.sequence[index+1:]

    def pop(self):
        result = self.sequence[-1]
        self.sequence = self.sequence[:-1]
        return result

    def clear(self):
        self.sequence = []
        return self.sequence

    def index(self, value):
        if value not in self.sequence:
            raise ValueError("This value does not exist!")
        result = [x for x in range(len(self.sequence)) if self.sequence[x] == value]
        if len(result) == 1:
            return result[0]
        return result

    def count(self, value):
        if value not in self.sequence:
            raise ValueError("This value does not exist!")
        result = len([x for x in range(len(self.sequence)) if self.sequence[x] == value])
        return result

    def reverse(self):
        return self.sequence[::-1]

    def copy(self):
        return self.sequence[:]

    def size(self):
        return len(self.sequence)

    def add_first(self, value):
        self.sequence = [value] + self.sequence

    def dictionize(self):
        evens = []
        odds = []
        for index in range(len(self.sequence)):
            if index % 2 == 0:
                evens.append(self.sequence[index])
                if index == len(self.sequence) - 1:
                    odds.append(" ")
            else:
                odds.append(self.sequence[index])
        return dict(zip(evens, odds))

    def move(self, amount):
        if amount > len(self.sequence):
            raise IndexError("Not enough elements in list!")
        self.sequence = self.sequence[amount:] + self.sequence[:amount]
        return self.sequence

    def sum(self):
        result = 0
        for element in self.sequence:
            if isinstance(element, int):
                result += element
            else:
                result += len(element)
        return result

    def overbound(self):
        pass
        # TODO: Returns the index of the biggest value. If the value is not a number, check it’s length.

    def underbound(self):
        pass
        # TODO: Returns the index of the smallest value. If the value is not a number, check it’s length.


# test_list = CustomList(1, 2, "Pesho")
# test_list.append(10)
# test_list.append("Mihal")
# print(test_list.remove(4))
# print(test_list.get(2))
# print(test_list.extend([1, 2, 3]))
# print(test_list.extend([1, 1, 1]))
# print(test_list.insert(3, "new value"))
# print(test_list.pop())
# print(test_list)
# #test_list.clear()
# #print(test_list.sequence)
# print(test_list.index(1))
# print(test_list.count(1))
# print(test_list.sequence)
# print(test_list.reverse())
# print(test_list.copy())
# print(test_list.size())
# test_list.add_first("Add1")
# test_list.add_first("Add2")
# print(test_list.dictionize())
# print(test_list.size())
# print(test_list)
# print(test_list.move(5))
# print(test_list.sum())