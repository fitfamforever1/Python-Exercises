# Hangman Game

# Module
import random

# Variables
words = ("candy", "chocolate", "milk", "cake", "cookie", "cupcake")
word = random.choice(words)

guesses = ""
turns = 10

length = len(word)

# Game loop
while turns > 0:
    input_letter = input("Guess a letter: ")
    guesses += input_letter
    for i in range(length):
        if word[i] in guesses:
            print(word[i], end=" ")
        else:
            print("_", end=" ")
    print()
    if input_letter not in word:
        turns -= 1
        print(f"Wrong! You have {turns} turns left.")
        if turns == 0:
            print(f"You lose! The word was '{word}'.")
    else:
        if all(letter in guesses for letter in word):
            print(f"Congratulations! You guessed the word '{word}'!")
            break
