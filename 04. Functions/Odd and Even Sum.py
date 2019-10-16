def odd_even_sum(number):
    odd = sum([int(n) for n in number if int(n) % 2 != 0])
    even = sum([int(n) for n in number if int(n) % 2 == 0])
    return f"Odd sum = {odd}, Even sum = {even}"


n = input()

print(odd_even_sum(n))