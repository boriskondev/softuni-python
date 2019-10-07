n = int(input())

for first in range(97, 97+n):
    for second in range(97, 97+n):
        for third in range(97, 97+n):
            print(f"{chr(first)}{chr(second)}{chr(third)}")