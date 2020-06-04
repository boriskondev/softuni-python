daily_allowance = int(input())
days_left = int(input())

items_per_day = daily_allowance

days_counter = 0
cost = 0
spirit = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        items_per_day += 2
    if day % 10 == 0:
        cost += 23
        spirit -= 20
    if day % 2 == 0:
        cost += 2 * items_per_day
        spirit += 5
    if day % 3 == 0:
        cost += 8 * items_per_day
        spirit += 13
    if day % 5 == 0:
        cost += 15 * items_per_day
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    days_counter += 1

if days_counter % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")