budget = float(input())
flour_price = float(input())

cozonacs = 0
eggs = 0

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4

cozonac_price = eggs_price + flour_price + milk_price

while budget >= cozonac_price:
    cozonacs += 1
    eggs += 3
    if cozonacs % 3 == 0:
        eggs_lost = cozonacs - 2
        eggs -= eggs_lost
    budget -= cozonac_price

print(f"You made {cozonacs} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")