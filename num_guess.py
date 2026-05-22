# A simple number guessing game where the user tries to guess a randomly generated number between 1 and 100.

# Module
import random

# Variables
num = random.randint(1, 100)
guess = 0

# Game loop
while guess != num:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
