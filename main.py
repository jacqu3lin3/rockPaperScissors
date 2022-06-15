
import random

options = ["R", "P", "S"]
user_choice = False


while user_choice == False:
    user_choice = input("Enter a choice (R, P, S): ")
    computer_choice = random.choice(options)
    print(f"\nPlayer ({user_choice}): Computer ({computer_choice})\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie! Play again!")
        user_choice = False
    elif user_choice == "R":
        if computer_choice == "scissors":
            print("Player won!")
        else:
            print("Computer won!")
    elif user_choice == "P":
        if computer_choice == "rock":
            print("Player won!")
        else:
            print("Computer won!")
    elif user_choice == "S":
        if computer_choice == "paper":
            print("Player won!")
        else:
            print("Computer won!")
    else:
        print("Error! Please choose a valid option!")
        user_choice = False
