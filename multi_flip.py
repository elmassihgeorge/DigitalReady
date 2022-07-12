import random

def coinflip():
    return random.choice(["Heads", "Tails"])

# multi_flip(num) -> Flips a coin num times and returns the results
def multi_flip(num):

    # Data Declaration
    heads = 0
    tails = 0

    # While loops -> condition
    # For loops -> exact # of loops
    for x in range(num):
        flip = coinflip()
        if (flip == "Heads"):
            heads = heads + 1
        else:
            tails = tails + 1
    
    print("You flipped " + str(heads) + " heads and " + str(tails) + " tails.")
    print("Percentage of Heads: " + str(100 * heads / num) + "%")
    print("Percentage of Tails: " + str(100 * tails / num) + "%")

    if (heads == tails):
        print("You flipped the same number of heads and tails")
    elif (heads > tails):
        print("You flipped more heads than tails")
    elif (heads < tails):
        print("You flipped more tails than heads")
