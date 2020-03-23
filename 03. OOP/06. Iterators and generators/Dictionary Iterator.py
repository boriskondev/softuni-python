class DictionaryIter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.dictionary_keys = list(self.dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dictionary_keys):
            raise StopIteration
        current_key = self.dictionary_keys[self.index]
        current_value = self.dictionary[current_key]
        self.index += 1
        return current_key, current_value


result = DictionaryIter({1: "1", 2: "2"})
for x in result:
    print(x)

