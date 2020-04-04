from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    def add(self, card: Card):
        for current_card in self.cards:
            if current_card.name == card.name:
                raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card_name: str):
        if card_name == "":
            raise ValueError("Card cannot be an empty string!")
        for current_card in self.cards:
            if current_card.name == card_name:
                self.cards.remove(current_card)

    def find(self, name):
        for current_card in self.cards:
            if current_card.name == name:
                return current_card

    @property
    def count(self):
        return len(self.cards)
