class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.end:
            raise StopIteration
        self.current = self.start
        self.start += 1
        return self.current


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)


