# Python Hangman

# Welcome user
name = input("What is your name? ")

print("Hello", name + ".", "Let's play hangman!")

# Start Game

# set game variables
word = "anaconda"

turns = 4

guesses = ''

# game loop

while turns > 0:

    # print underscores & correct letters
    print("")   # visual spacing in game

    for letter in word:

        if letter in guesses:

            print(letter, end=" ")

        else:

            print("_", end=" ")

    print("\n") # visual spacing in game

    guess = input("guess a letter: ")

    guesses += guess

    if guess not in word:

        turns -= 1

        print("Nope...")

        print("You have", turns, "guesses left.")

        if turns == 0:

            print("You lost :(")