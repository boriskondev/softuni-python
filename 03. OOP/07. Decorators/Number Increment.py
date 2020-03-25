def number_increment(numbers):
    def increase():
        value = list([x + 1 for x in numbers])
        return value
    return increase()


print(number_increment([1, 2, 3]))