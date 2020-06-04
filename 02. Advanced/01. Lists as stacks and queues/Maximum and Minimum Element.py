number_of_queries = int(input())

queries_counter = 0

stack = []

while number_of_queries > queries_counter:
    token = input().split()
    if token[0] == "1":
        stack.append(int(token[1]))
    if stack:
        if token[0] == "2":
            stack.pop()
        elif token[0] == "3":
            print(max(stack))
        elif token[0] == "4":
            print(min(stack))

    queries_counter += 1

print(", ".join(list(map(str, reversed(stack)))))