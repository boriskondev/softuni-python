expression = input()

opening = []
closing = []

indices_list = []

for i in range(len(expression)):
    if expression[i] == "(":
        opening.append(i)
    elif expression[i] == ")":
        closing.append(i)
        if opening and closing:
            indices = [opening.pop(), closing.pop()]
            indices_list.append(indices)

for idx in indices_list:
    print(expression[idx[0]:idx[1]+1])


