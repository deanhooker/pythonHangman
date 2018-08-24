# Python Hangman

# Welcome user
name = input("What is your name? ")

print("Hello", name + ".", "Let's play hangman!")

# Start Game

# set game variables
word = "anaconda"

turns = 8

guesses = ''

# game loop

while turns > 0:

    print("")

    for letter in word:

        if letter in guesses:

            print(letter, end=" ")

        else:

            print("_", end=" ")

            turns - 1

    print("\n")

    guess = input("guess a letter: ")

    guesses += guess