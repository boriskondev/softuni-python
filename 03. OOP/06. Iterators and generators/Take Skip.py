class TakeSkip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.result = self.start
        self.count -= 1
        self.start += self.step
        return self.result


numbers = TakeSkip(2, 6)
for number in numbers:
    print(number)
