#Project 2: Rock Paper Scissors Game 
import random
#  A list containing the valid options
options = ["rock", "paper", "scissors"]

print("-------Welcome to Rock, Paper, Scissors!--------")
user_choice = input("Enter rock, paper, or scissors: ").lower()

# The computer randomly picks an item from our options list
computer_choice = random.choice(options)

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Add the Game Decision Logic Below:
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins! Better luck next time.")