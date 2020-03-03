class Pile:

    def __init__(self):
        self.cards = []

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def add_card(self, card):
        self.cards.append(card)

    def take_top(self):
        return self.cards.pop(0)

    def add_all(self, cards):
        self.cards.extend(cards)

  
    def has_cards(self):
        return bool(self.cards)