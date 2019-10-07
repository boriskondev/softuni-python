divisor = int(input())
bound = int(input())

number = bound

for n in range(number, 0, -1):
    if n % divisor == 0 and 0 < n <= bound:
        break
    n -= 1

print(n)