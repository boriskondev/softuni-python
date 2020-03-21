class SentenceIterator:
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


def sentence_generator(string):
    for word in string.split():
        yield word


my_sentence_iterator = SentenceIterator("This is a test")
my_sentence_generator = sentence_generator("This is a test")

for i in my_sentence_iterator:
    print(i)

print()

for i in my_sentence_generator:
    print(i)



