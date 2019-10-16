def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a, b), c)


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))