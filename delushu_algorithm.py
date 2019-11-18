import random

tryouts = int(input("How many tryouts? "))

NAT_TOM_PRICE = 6.00
POR_SPI_PRICE = 6.50
AVERAGE_PRICE = (NAT_TOM_PRICE + POR_SPI_PRICE) / 2

differences = []

for tryout in range(1, tryouts + 1):
    natural = random.randint(0, 100)
    tomatoes = random.randint(0, 100)
    porcini = random.randint(0, 100)
    spicy = random.randint(0, 100)
    total_purchases = natural + tomatoes + porcini + spicy
    total_turnover = NAT_TOM_PRICE * (natural + tomatoes) + POR_SPI_PRICE * (porcini + spicy)
    print(f"Purchases: {total_purchases} |", end=" ")
    print(f"Turnover: {total_turnover:.2f} |", end=" ")
    fee_purchases = total_purchases * 0.30
    print(f"Fee (purchases): {fee_purchases:.2f} |", end=" ")
    fee_turnover = total_turnover / AVERAGE_PRICE * 0.30
    print(f"Fee (turnover): {fee_turnover:.2f} |", end=" ")
    difference = fee_purchases - fee_turnover
    print(f"Difference: {difference:.2f}")
    differences.append(f"{difference:.2f}")

print()
[print(x) for x in sorted(differences)]
print()

print(f"Out of {tryouts} tryouts:")
print(f"Min difference: {min(differences)}")
print(f"Max difference: {max(differences)}")