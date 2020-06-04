input_string = list(input())

stack = []

for i in range(len(input_string)):
    stack.append(input_string.pop())

print("".join(stack))