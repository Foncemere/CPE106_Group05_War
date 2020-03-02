class Game:

    def __init__(self):
        self.cards = []
        self.players = []
        self.bonus = []

    def addC(self, card, player):
        self.cards.append(card)
        self.players.append(player)

    def addB(self, cards):
        self.bonus.extend(cards)

    def winner(self):
        self.show()
        val = [i.value for i in self.cards]
        self.best = max(val)
        if val.count(self.best) == 1:
            return self.players[val.index(self.best)]

    def show(self):
        for player, card in zip(self.players, self.cards):
            print('{} : {} '.format(player.name, card))

    def win(self, player):
        player.give_cards(self.cards)
        player.give_cards(self.bonus)

    def istied(self):
        for card, player in zip(self.cards, self.players):
            if card.value == self.best:
                yield player
