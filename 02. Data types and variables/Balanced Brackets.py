lines = int(input())

brackets = []

for line in range(1, lines + 1):
    char = input()
    if char == "(" or char == ")":
        brackets.append(char)

if brackets[0] == "(" and brackets[1] == ")":
    print("BALANCED")
else:
    print("UNBALANCED")
