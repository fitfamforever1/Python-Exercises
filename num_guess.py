# A simple number guessing game where the user tries to guess a randomly generated number between 1 and 100.

# Module
import random

# Variables
num = random.randint(1, 100)
guess = 0

# Game loop
while guess != num:
    guess = input("Guess a number between 1 and 100: ")

    if guess.isdigit():
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            guess = input("Guess a number between 1 and 100: ")
            
        elif guess < num:
            print("Too low! Try again.")
        elif guess > num:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")

    else:
        print("Please enter a valid number.")
        continue
