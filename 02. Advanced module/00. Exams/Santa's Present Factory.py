from collections import deque

crafted = {}

magic_and_presents = {150: "Doll",
                      250: "Wooden train",
                      300: "Teddy bear",
                      400: "Bicycle",}

materials_stack = list(map(int, input().split()))
magic_values_queue = deque(map(int, input().split()))

if len(materials_stack) == len(magic_values_queue):
    traverse = len(materials_stack)

while True:
    if not materials_stack or not magic_values_queue:
        break
    material = materials_stack[-1]
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
        materials_stack.pop()
        materials_stack.append(material + magic)
        magic_values_queue.popleft()
    elif currently_crafted > 0:
        magic_values_queue.popleft()
        materials_stack[-1] += 15
    elif material == 0 and magic == 0:
        materials_stack.pop()
        magic_values_queue.popleft()
    elif material == 0:
        materials_stack.pop()
    elif magic == 0:
        magic_values_queue.popleft()

if "Doll" in crafted and "Wooden train" in crafted or "Teddy bear" in crafted and "Bicycle" in crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stack:
    print("Materials left: " + ', '.join([str(x) for x in materials_stack[::-1]]))
if magic_values_queue:
    print("magic left: " + ', '.join([str(x) for x in magic_values_queue]))

for item, quantity in sorted(crafted.items()):
    print(f"{item}: {quantity}")
