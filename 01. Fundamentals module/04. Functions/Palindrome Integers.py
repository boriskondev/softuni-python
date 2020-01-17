def is_palindrome(num):
    if num == num[::-1]:
        return True
    return False


inp = input().split(", ")

for num in inp:
    print(is_palindrome(num))