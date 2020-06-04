stack = list(map(int, input().split()))
rack_capacity = int(input())

current_capacity = rack_capacity
rack_counter = 1

while True:
    if stack:
        clothing_on_top = stack[-1]
        if clothing_on_top <= current_capacity:
            current_capacity -= clothing_on_top
            stack.pop()
        else:
            rack_counter += 1
            current_capacity = rack_capacity
            continue
    else:
        break

print(rack_counter)
