# Simple Rock-Paper-Scissors Game

# Module
import random

# Variables
bot = random.choice(['rock', 'paper', 'scissors'])
user = input("Enter rock, paper, or scissors: ").lower()

# Game Logic
while True:
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please enter rock, paper, or scissors.")
        user = input("Enter rock, paper, or scissors: ").lower()
        continue

    print(f"Bot chose: {bot}")

    if user == bot:
        print("It's a tie!")
    elif (user == 'rock' and bot == 'scissors') or \
         (user == 'paper' and bot == 'rock') or \
         (user == 'scissors' and bot == 'paper'):
        
        print("You win!")
    else:
        print("You lose!")
    break
