a = int(input())
is_prime = ""

if a < 1:
    is_prime = "False"
else:
    for n in range(2, a):
        if a % n == 0:
            is_prime = "False"
            break
        is_prime = "True"

print(is_prime)

