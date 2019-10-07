n = float(input())

if n == 0:
    print("zero")
elif n > 0:
    if abs(n) < 1:
        print("small positive")
    elif abs(n) > 1000000:
        print("large positive")
    else:
        print("positive")
elif n < 0:
    if abs(n) < 1:
        print("small negative")
    elif abs(n) > 1000000:
        print("large negative")
    else:
        print("negative")
