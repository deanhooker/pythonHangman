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

    # create var to track underscores left
    blanksLeft = 0

    # print underscores & correct letters
    print("")   # visual spacing in game

    for letter in word:

        if letter in guesses:

            print(letter, end=" ")

        else:

            print("_", end=" ")

            blanksLeft += 1

    print("\n")  # visual spacing in game
    
    # handle win
    if blanksLeft == 0:

        print("You won!!!")

        break

    # grab user input and add into guesses var
    guess = input("guess a letter: ")

    guesses += guess

    # handle incorrect guesses
    if guess not in word:

        turns -= 1

        print("Nope...")

        print("You have", turns, "guesses left.")

        # end game
        if turns == 0:

            print("\nYou lost :(")