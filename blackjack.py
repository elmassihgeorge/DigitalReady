import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def to_string(self):
        if (self.value == 13):
            return "King of " + self.suit
        elif (self.value == 12):
            return "Queen of " + self.suit
        elif (self.value == 11):
            return "Jack of " + self.suit
        elif (self.value == 1):
            return "Ace of " + self.suit
        else:
            return str(self.value) + " of " + self.suit

def make_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    deck = []
    for suit in suits:
        for value in range(1, 13):
            deck.append(Card(suit, value))
    random.shuffle(deck)
    return deck
    
def biggest_number(list):
    biggest_so_far = 0
    for num in list:
        if (num > biggest_so_far):
            biggest_so_far = num
    return biggest_so_far

def blackjack(players):
    num_players = int(players)
    if num_players < 1:
        print("ERROR: Invalid Number of Players")
        return
    player_scores = [0] * num_players
    deck = make_deck()
    play_again = True
    
    while play_again:
        #Loop for entire game
        for player in range(num_players):
            print("Player " + str(player + 1) + "'s turn")
            sum = 0
            current_card = deck.pop()
            sum = sum + current_card.value
            print("Current Card: " + current_card.to_string())
            while True:
                print("Current Sum: " + str(sum))
                choice = input("Would you like to take another card? Y / N or Q to quit ... ")
                if choice == "Q":
                    return
                if choice == "Y":
                    next_card = deck.pop()
                    sum = sum + next_card.value
                    print("Current Card: " + next_card.to_string())
                    if (sum > 21):
                        print("You went over 21! You lose.")
                        break
                elif choice == "N":
                    print("Player " + str(player + 1) + "'s score: " + str(sum))
                    player_scores[player] = sum
                    break
                else:
                    print("Invalid input")
                current_card = next_card
        winner = player_scores.index(biggest_number(player_scores))   
        print("Player " + str(winner + 1) + " wins with a score of " + str(biggest_number(player_scores)))
        play = input("Would you like to play again? Y or N ...")
        if play == "N":
            return
