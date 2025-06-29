#5 way rock, paper, scissors, lizard and spock from the Big Bang Theory


#importing the random module
import random



#The only answers that the user can give
valid_cases = ["rock", "paper", "scissors", "spock", "lizard"]

#Word association, that would cause the user to lose, if user picks rock and the computer picks paper then the user loses etc...
losing_cases = {
     "rock": ["paper", "spock"],
     "paper": ["scissors", "lizard"],
     "scissors": ["rock", "spock"],
     "spock": ["lizard", "paper"],
     "lizard": ["scissors", "rock"]     
}


#Loop to repeat the game
while True:
    #Question for the user
    user_choice = input("Please insert your choice here: \n").lower()

    #Handle cases where the users write something that aren't part of the options
    if user_choice not in valid_cases:
        print("Please only write: rock, paper scissors, spock or lizard... Thanks")
        continue

    #Computer makes a choice with the random module
    computer_choice = random.choice(["rock", "paper", "scissors", "spock", "lizard"])



    #draw functionality
    if user_choice == computer_choice:
        print(f"You chose {user_choice} and Sheldon chose {computer_choice} so its a draw!!")

    #Win & lose functionality
    elif computer_choice in losing_cases[user_choice]:
        print(f"You chose {user_choice} and Sheldon chose {computer_choice} so you win!!")
    else:
        print(f"You chose {user_choice} and Sheldon chose {computer_choice} so you lose!!")


    #Loop to play again
    while True:

        play_again = input("Would you like to play again? \n Type YES to continue:").lower()

        if play_again == "yes":
            break

        elif play_again == "no":
            print("Thanks for playing!")
            exit()
        #If the user writes something that is not yes or no!
        else:
            print("Please only type yes or no!!")









