def multiplication_sign(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "zero"
    elif a < 0 and b < 0:
        if c < 0:
            return "negative"
        else:
            return "positive"
    elif a < 0 and c < 0:
        if b < 0:
            return "negative"
        else:
            return "positive"
    elif b < 0 and c < 0:
        if a < 0:
            return "negative"
    elif a > 0 and b > 0:
        if c > 0:
            return "positive"
        else:
            return "negative"
    elif a > 0 and c > 0:
        if b > 0:
            return "positive"
        else:
            return "negative"
    elif b > 0 and c > 0:
        if a > 0:
            return "positive"
        else:
            return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(multiplication_sign(num1, num2, num3))