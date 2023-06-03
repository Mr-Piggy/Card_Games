import base
class War:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = base.Deck()
        self.p1 = base.Player(name1)
        self.p2 = base.Player(name2)
    def wins(self, winner):
        w = "{} wins this battle!".format(winner)
        print(w)
    def draw(self, p1n, p2n):
        self.p1c = self.deck.draw_card()
        self.p2c = self.deck.draw_card()
        d = "{} drew {}  {} drew {}".format(p1n,self.p1c,p2n,self.p2c)
        print(d)
    def play(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any key to play: "
            response = input(m)
            if response == 'q':
                break
            self.draw(self.p1.name, self.p2.name)
            if self.p1c > self.p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins.".format(win))
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p2.wins > p1.wins:
            return p2.name
        return "nobody"
if __name__ == "__main__":
    game = War()
    game.play()