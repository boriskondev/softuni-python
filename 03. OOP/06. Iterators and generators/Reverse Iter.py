class ReverseIter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.iterable) == 0:
            raise StopIteration
        current = self.iterable[-1]
        self.iterable.pop()
        return current


reversed_list = ReverseIter([1, 2, 3, 4])

for item in reversed_list:
    print(item)
