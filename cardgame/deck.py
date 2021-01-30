class Deck:

    # override constructor has "Hoyle" as default deck
    # changing the deck name sets instance values for decksuits and deckvalues
    def __init__(self, deckname = "Hoyle"):
        self.deckname = deckname
        self.decksuits = {"Spades":1, "Clubs":2, "Diamonds":3, "Hearts":4}
        self.deckvalues = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":1}
        self.deck = ["S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "SX", "SJ", "SQ", "SK", "SA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "CX", "CJ", "CQ", "CK", "CA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "DX", "DJ", "DQ", "DK", "DA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "HX", "HJ", "HQ", "HK", "HA",]
        self.deckbuild = [self.decksuits, self.deckvalues, self.deck]

    # deckname sets the suits and values
    # new decks with different suits and values can be added in elif statements
    # decksuits lists the suit name and value
    # deckvalues lists the card face and value
    # deck is a List of all suit and value combos as 2 char strings - 10 == X
    def deck_builder(self, deckname):
        if deckname == "Hoyle" or "Standard":
            self.deckname = "Standard"
            self.decksuits = {"Spades":1, "Clubs":2, "Diamonds":3, "Hearts":4}
            self.deckvalues = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":1}
            self.deck = ["S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "SX", "SJ", "SQ", "SK", "SA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "CX", "CJ", "CQ", "CK", "CA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "DX", "DJ", "DQ", "DK", "DA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "HX", "HJ", "HQ", "HK", "HA",]
            deckbuild = [decksuits, deckvalues, deck]
            return deckbuild
        elif deckname == "Zaithen":
            self.deckname = "Zaithen"
            self.decksuits = {"Circle":1, "X":2, "Triangle":3, "Square":4}
            self.deckvalues = list(range(1,11))
            self.deck = None
            deckbuild = [decksuits, deckvalues, deck]
            return deckbuild

    # returns a shuffled deck
    def shuffle_deck(self):
        shuffled_deck = random.shuffle(self.deckbuild[2])
        return shuffled_deck

    # getter returns deckname
    def get_deck(self):
        return self.deckname

    # setter sets deck name and (in theory) calls the deck_picker method?
    def set_deck(self, deckname):
        self.deckname = deckname
        deck_picker(deckname)
