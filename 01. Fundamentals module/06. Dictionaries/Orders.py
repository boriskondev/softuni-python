orders = {}

while True:
    command = input().split()
    if command[0] == "buy":
        break
    else:
        product = command[0]
        price = float(command[1])
        quantity = int(command[2])
        if product not in orders:
            orders[product] = [price, quantity]
        else:
            orders[product][0] = price
            orders[product][1] += quantity

for order, info in orders.items():
    total_price = info[0] * info[1]
    print(f"{order} -> {total_price:.2f}")