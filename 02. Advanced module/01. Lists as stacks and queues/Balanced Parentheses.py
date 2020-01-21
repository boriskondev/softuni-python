parentheses = input()

not_found = False

stack = []

pairs = {"{": "}",
         "[": "]",
         "(": ")"
         }

for el in range(len(parentheses)):
    if parentheses[el] in "{[(":
        stack.append(parentheses[el])
    elif parentheses[el] in ")]}":
        last = stack[-1]
        if parentheses[el] == pairs[last]:
            stack.pop()
        else:
            not_found = True
            break
    else:
        not_found = True
        break

if not_found:
    print("NO")
else:
    print("YES")
