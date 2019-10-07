companions = int(input())
party_days = int(input())

days = 0
coins = 0

while days != party_days:
    days = days + 1
    if days % 10 == 0:
        companions = companions - 2
    if days % 15 == 0:
        companions = companions + 5
    coins = coins + 50
    coins = coins - (2 * companions)
    if days % 3 == 0:
        coins = coins - (3 * companions)
    if days % 5 == 0:
        coins = coins + (20 * companions)
        if days % 3 == 0:
            coins = coins - (2 * companions)


final_coins = int(coins / companions)

print(f"{companions} companions received {final_coins} coins each.")