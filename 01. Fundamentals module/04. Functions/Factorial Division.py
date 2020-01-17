def factorial(n):
    for i in range(n, 1, -1):
        n = n * (i - 1)
    return n


x = int(input())
y = int(input())

result = factorial(x) / factorial(y)

print(f"{result:.2f}")