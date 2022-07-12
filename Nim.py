import random

def nim():
    score = 10
    # Loop that runs the game until someone wins
    while(score > 0):
        print("Current Score: " + str(score))

        #Asking for user input
        user_choice = int(input("Would you like to remove 1, 2, or 3 points"))
        if (user_choice == 1) or (user_choice == 2) or (user_choice == 3):
            score = score - user_choice
            if (score <= 0):
                print("You set the score to 0! You lose!")
                break
            print("Current Score: " + str(score))
        else:
            print("Error: Must be 1, 2 or 3")

        # Process the AI's turn
        if (score == 6):
            ai_choice = 1
        elif (score == 7):
            ai_choice = 2
        elif (score == 8):
            ai_choice = 3
        elif (score == 3):
            ai_choice = 2
        elif (score == 2):
            ai_choice = 1
        else:
            ai_choice = random.choice([1, 2, 3])
        print("The AI chose: " + str(ai_choice))
        score = score - ai_choice
        if (score <= 0):
            print("The AI set the score to 0, you win!")
            break
