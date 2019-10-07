items_and_prices = input().split("|")
budget = int(input())

items_bought = []

for item_and_price in items_and_prices:
    item, price = item_and_price.split("->")
    price = float(price)
    if budget >= price:
        if item == "Clothes" and price <= 50.00 \
                or item == "Shoes" and price <= 35.00 \
                or item == "Accessories" and price <= 20.50:
            budget -= price
            items_bought.append(price * 1.4)


[print(f"{num:.2f}", end=" ") for num in items_bought]
print()
print(f"Profit: {(sum(items_bought) - sum(items_bought) / 1.4):.2f}")
if sum(items_bought) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")