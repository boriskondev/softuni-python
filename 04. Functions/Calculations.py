def calculate(operation, x, y):
    if operation == "multiply":
        return x * y
    elif operation == "divide":
        return int(x / y)
    elif operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y


operation = input()
x = int(input())
y = int(input())

print(calculate(operation, x, y))