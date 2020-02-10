from collections import deque

traverse = 0
materials_to_add = 0
crafted = {}

magic_and_presents = {150: "Doll",
                      250: "Wooden train",
                      300: "Teddy bear",
                      400: "Bicycle",}

materials_stack = list(map(int, input().split()))
magic_values_queue = deque(map(int, input().split()))

if len(materials_stack) == len(magic_values_queue):
    traverse = len(materials_stack)

for case in range(traverse):
    material = materials_stack[-1] + materials_to_add
    magic = magic_values_queue[0]
    currently_crafted = material * magic
    if currently_crafted in magic_and_presents:
        materials_stack.pop()
        magic_values_queue.popleft()
        if magic_and_presents[currently_crafted] in crafted:
            crafted[magic_and_presents[currently_crafted]] += 1
        else:
            crafted[magic_and_presents[currently_crafted]] = 1
    elif currently_crafted < 0:
        materials_to_add = material + magic
        materials_stack.pop()
        magic_values_queue.popleft()
    elif currently_crafted > 0:
        magic_values_queue.popleft()
        materials_to_add = 15
    elif material == 0 and magic == 0:
        materials_stack.pop()
        magic_values_queue.popleft()
    elif material == 0:
        materials_stack.pop()
    elif magic == 0:
        magic_values_queue.popleft()

print(crafted)