input_string = input().split()

output = []

for word in input_string:
    code = [x for x in word if x.isnumeric()]
    first_char = chr(int("".join(code)))
    if len(code) + 1 == len(word):
        fixed_word = first_char + word[-1]
    else:
        second_char = word[len(code)]
        fixed_word = first_char + word[-1] + word[len(code)+1:-1] + second_char
    output.append(fixed_word)

print(" ".join(output))