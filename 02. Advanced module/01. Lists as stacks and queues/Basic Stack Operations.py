elements_to_push, elements_to_pop, to_look_for = map(int, input().split())

stack = list(map(int, input().split()))

for n in range(elements_to_pop):
    stack.pop()

if stack:
    if to_look_for in stack:
        print("True")
    else:
        print(min(stack))
else:
    print("0")