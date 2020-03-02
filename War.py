class War:

    def __init__(self, players):
        self.players = [Player(name, Pile()) for name in players]
        self.deck = Deck()

    def dealer(self):
        self.deck.shuffle()
        self.deck.setup_pile(self.players)
        for i in self.players:
            i.show_pile()

    def play(self, istied=None):
        i = Game()
        for player in (self.players if istied is None else istied):
            player.drop_card(i)
            if istied:
                player.drop_bonus(i, 3)
        winner = i.winner
        if winner is not None:
            i.win(winner)
        else:
            winner = self.play(i.istied)
            i.win(winner)
        return winner

    def playf(self):
        while not self.finished:
            self.play()
        self.show_winner()

    def show_winner(self):
        for x in self.players:
            if x.pile.has_cards:
                print("\n Winner = ", x.name)
                break

    def finished(self):
        return sum(bool(player.pile.cards) for player in self.players) == 1