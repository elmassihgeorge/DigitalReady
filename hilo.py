import random

class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_string(self):
        if (self.value >= 2) and (self.value <= 10):
            return (str(self.value)) + " of " + self.suit
        if (self.value == 1):
            return "Ace of " + self.suit
        if (self.value == 11):
            return "Jack of " + self.suit
        if (self.value == 12):
            return "Queen of " + self.suit
        if (self.value == 13):
            return "King of " + self.suit
        

def make_deck():
    deck = []
    for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
        for value in range(1, 13):
            deck.append(Card(value, suit))
    random.shuffle(deck)
    return deck

    
# hilo(): plays a game of hilo
def hilo():

    # Data Declarations
    points = 100
    deck = make_deck()
    current_card = deck.pop()

    # Game Loops
    while points > 0:

        # Input / Output
        print("Current points: " + str(points))
        print("Current card: " + current_card.to_string())
        guess = input("Do you think the next card is H or L? Or type Q to quit.")
        if (guess == "Q"):
            break
        elif (guess != "H") and (guess != "L"):
            print("Invalid Guess, must be H, L, or Q")
        else:
            bet = int(input("How many points would you like to bet?"))
            if (bet < 0) or (bet > points):
                print("Invalid Bet")
            else:
                next_card = deck.pop()
                print("Next Card: " + next_card.to_string())
                if (current_card.value > next_card.value):
                    if (guess == "H"):
                        print("You guessed wrong!")
                        points = points - bet
                    if (guess == "L"):
                        print("You guessed right!")
                        points = points + bet
                if (current_card.value < next_card.value):
                    if (guess == "L"):
                        print("You guessed wrong!")
                        points = points - bet
                    if (guess == "H"):
                        print("You guessed right!")
                        points = points + bet
                if (current_card.value == next_card.value):
                    print("Cards have same value")
                current_card = next_card
    
    if (points > 0):
        print("You quit with " + str(points) + " remaining")
    else:
        print("You ran out of points! You lose!")