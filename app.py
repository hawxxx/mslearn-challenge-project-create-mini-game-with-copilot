# Import necessary modules
# Let's create rock, paper, scissors minigame computer vs player
# We need random module
import random
# Define score variables
player_score = 0
computer_score = 0
# Define list of possible choices
choices = ["rock", "paper", "scissors"]
# Let's create a game loop
while True:
    # Let's get user input
    player_input = input("Rock, Paper or Scissors? ").lower()
    # Let's get computer input
    computer_input = random.choice(choices)
    # Let's check if user input is valid
    if player_input in choices:
        # Let's check if user and computer inputs are the same
        if player_input == computer_input:
            print(f"Computer chose {computer_input}. It's a draw!")
        # Let's check if user wins
        elif player_input == "rock" and computer_input == "scissors":
            print(f"Computer chose {computer_input}. You win!")
            player_score += 1
        elif player_input == "paper" and computer_input == "rock":
            print(f"Computer chose {computer_input}. You win!")
            player_score += 1
        elif player_input == "scissors" and computer_input == "paper":
            print(f"Computer chose {computer_input}. You win!")
            player_score += 1
        # Let's check if computer wins
        elif player_input == "rock" and computer_input == "paper":
            print(f"Computer chose {computer_input}. You lose!")
            computer_score += 1
        elif player_input == "paper" and computer_input == "scissors":
            print(f"Computer chose {computer_input}. You lose!")
            computer_score += 1
        elif player_input == "scissors" and computer_input == "rock":
            print(f"Computer chose {computer_input}. You lose!")
            computer_score += 1
        # Let's ask user if he wants to play again
        play_again = input("Play again? (y/n) ").lower()
        if play_again == "n":
            print(f"Player score: {player_score}")
            print(f"Computer score: {computer_score}")
            break
    else:
        print("Invalid input. Please enter rock, paper or scissors.")