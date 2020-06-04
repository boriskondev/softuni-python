word = input()

result = "".join(list(map(lambda char: char * 2, word)))

print(result)