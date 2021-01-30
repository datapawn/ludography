import random
import deck

class Game:
    # build a Game by telling it the Name of the Game
    def __init__(self, game):
        self.gamename = game

    # deal is just a test game
    def deal(self):
        #instantiate a deck
        cards = deck.Deck()
        # print the first 5 cards from that deck
        print(cards.deck[0:4])
        # shuffle those cards
        random.shuffle(cards.deck)
        # print the first five shuffled cards
        print(cards.deck[0:4])