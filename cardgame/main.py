
import dealer

def main():
    play = dealer.Table() # "starting a table" builds a dealer
    play.dealer_talk() # the dealer asks you what game you want to play, and chooses the game/deck to do so.

if __name__ == "__main__" : main()