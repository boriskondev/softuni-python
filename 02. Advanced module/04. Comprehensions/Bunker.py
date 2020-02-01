bunker = {item: {} for item in input().split(", ")}

for rows in range(int(input())):
    category, item, quantity_and_quality = input().split(" - ")
    quantity, quality = quantity_and_quality.split(";")
    quantity = int(quantity.split(":")[1])
    quality = int(quality.split(":")[1])

    if item not in bunker[category]:
        bunker[category][item] = (quantity, quality)

items_count = 0
average_quality = 0
counter = 0

for category, items in bunker.items():
    counter += 1
    for item in items:
        items_count += items[item][0]
        average_quality += items[item][1]

print(f"Count of items: {items_count}")
print(f"Average quality: {average_quality / counter:.2f}")

for category, items in bunker.items():
    print(f"{category} ->", end=" ")
    print(", ".join([item for item in items]))