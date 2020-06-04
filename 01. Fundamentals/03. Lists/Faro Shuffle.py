deck = input().split(" ")
shuffles_limit = int(input())

shuffles = 0

new_deck = []

while shuffles < shuffles_limit:
    half = int(len(deck) / 2)
    first_half = deck[:half]
    second_half = deck[half:]
    for first, second in zip(first_half, second_half):
        new_deck.append(first)
        new_deck.append(second)
    deck = new_deck[:]
    new_deck.clear()
    shuffles += 1

print(deck)