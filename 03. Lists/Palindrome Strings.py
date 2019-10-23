words = input().split()
palindrome = input()

palindromes = [word for word in words if word == word[::-1]]

found = palindromes.count(palindrome)

print(palindromes)
print(f"Found palindrome {found} times")