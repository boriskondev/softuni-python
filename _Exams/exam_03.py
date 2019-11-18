start_cards = input().split(":")
new_deck = []

while True:
    command = input().split()
    if command[0] == "Ready":
        break
    elif command[0] == "Add":
        card = command[1]
        if card not in start_cards:
            print("Card not found.")
        else:
            new_deck.append(card)
    elif command[0] == "Insert":
        card = command[1]
        index = int(command[2])
        if card not in start_cards or not 0 <= index <= len(new_deck) - 1:
            print("Error!")
        else:
            new_deck.insert(index, card)
    elif command[0] == "Remove":
        card = command[1]
        if card not in new_deck:
            print("Card not found.")
        else:
            new_deck.remove(card)
    elif command[0] == "Swap":
        card_1 = command[1]
        card_2 = command[2]
        card_1_index = new_deck.index(card_1)
        card_2_index = new_deck.index(card_2)
        new_deck.remove(card_1)
        new_deck.insert(card_1_index, card_2)
        new_deck.remove(card_2)
        new_deck.insert(card_2_index, card_1)
    elif command[0] == "Shuffle":
        new_deck = list(reversed(new_deck))

print(" ".join(new_deck))