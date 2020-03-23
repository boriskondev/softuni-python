class CountdownIterator:
    def __init__(self, count):
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == -1:
            raise StopIteration
        self.current = self.count
        self.count -= 1
        return self.current


iterator = CountdownIterator(10)
for item in iterator:
    print(item, end=" ")
