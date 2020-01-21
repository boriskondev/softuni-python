from collections import deque

not_enough = False
orders_counter = 0
biggest_order = 0

food_quantity = int(input())

queue = deque(map(int, input().split()))

while True:
    if food_quantity >= queue[-1]:
        food = queue.popleft()
        food_quantity -= food
        if food > biggest_order:
            biggest_order = food
    else:
        not_enough = True
        break
    if not queue:
        break

print(biggest_order)

if not_enough:
    print(f"Orders left:", end=" ")
    [print(food, end=" ") for food in queue]

else:
    print("Orders complete")