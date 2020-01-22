parentheses = input()

not_valid = False

stack = []

pairs = {"{": "}",
         "[": "]",
         "(": ")"
         }

for el in range(len(parentheses)):
    if parentheses[el] in "{[(":
        stack.append(parentheses[el])
    elif parentheses[el] in ")]}":
        if stack:
            last = stack[-1]
            if parentheses[el] == pairs[last]:
                stack.pop()
            else:
                not_valid = True
                break
        else:
            not_valid = True
            break

    else:
        not_valid = True
        break

if not_valid:
    print("NO")
else:
    print("YES")
