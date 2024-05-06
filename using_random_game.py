import random
import sys

choices = ["rock", "paper", "scissors"]

user_input = input("Please type rock, paper, or scissors\n")
comp_choice = random.choice(choices)

if user_input not in choices:
    print("Type only rock, paper, or scissors. Try again.")
    sys.exit()

if comp_choice == user_input:
    print('TIE')
elif user_input == "rock" and comp_choice == "scissors":
    print("You WIN!")
elif user_input == "paper" and comp_choice == "rock":
    print("You WIN!")
elif user_input == "scissors" and comp_choice == "paper":
    print("You WIN!")
else:
    print("Computer wins")

print("You selected:", user_input, "\nComputer selected:", comp_choice)
sys.exit()
