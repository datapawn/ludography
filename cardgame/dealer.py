import game

class Table:

    def __init__(self):
        pass

    def choose_game(self, gamename):
        pass

    # starting UI
    # currently this literallu just instantiates a game.Game
    def dealer_talk(self):
        print("welcome to the Table.")
        print("here are five cards.")
        simplegame = game.Game("deal5")
        simplegame.deal()