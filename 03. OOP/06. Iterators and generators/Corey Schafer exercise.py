class IterableObject:
    def __init__(self, string):
        self.string = string
        self.words = self.string.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def generator_function(string):
    for word in string.split():
        yield word


my_sentence_iterator = IterableObject("This is a test")
my_sentence_generator = generator_function("This is a test")

for i in my_sentence_iterator:
    print(i)

print()

for i in my_sentence_generator:
    print(i)



