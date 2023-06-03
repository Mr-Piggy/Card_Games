import base
class BlackJack:
    def __init__(self):
        name = input("What is your name ")
        self.player = base.Player(name)
        self.dealer = base.Player("AI")
        self.deck = base.Deck()
        self.playerstick = False
        self.dealerstick = False
    def add_card(self, player):
        player.card.append(self.deck.draw_card())
    def decide_AI(self):
        pass
    def play(self):
        self.player.card = []
        self.dealer.card = []
        for x in range(2):
            self.add_card(self.player)
            self.add_card(self.dealer)
        while not(self.player.points >= 21 or self.dealer.points >= 21):
            self.player.points = 0
            self.dealer.points = 0
            for card in self.player.card:
                self.player.points += card.value
            for card in self.dealer.card:
                self.dealer.points += card.value
            m = "You have {} points. Do you stick or twist? s/t".format(self.player.points)
            response = input(m).lower()
            if response == 't':
                self.add_card(self.player)
            else:
                self.playerstick = True
            self.decide_AI()
            if self.playerstick == True and self.dealerstick == True:
                break
        print("Someone won.")
if __name__ == "__main__":
    game = BlackJack()
    game.play()