n = int(input())

special_numbers = [5, 7, 11]

for num in range(1, n+1):
    is_special = "False"
    if sum(map(int, list(str(num)))) in special_numbers:
        is_special = "True"
    print(f"{num} -> {is_special}")