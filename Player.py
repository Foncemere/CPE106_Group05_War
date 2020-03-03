class Player:

    def __init__(self, name, hand):
        self.name, self.hand = name, hand

    def drop_card(self, collection):
        if self.hand.has_cards:
            collection.add_card(self.hand.take_top(), self)

    def drop_bonus(self, collection, count):
        collection.add_bonus(self.hand.cards[:count])
        self.hand.cards = self.hand.cards[count:]

    def give_cards(self, cards):
        self.hand.add_all(cards)

    def show_hand(self):
        print(self.name, 'has', self.hand)
