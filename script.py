import random as rm
from functions import guess_the_number, think_the_number, play

# GUESS THE NUMBER GAME
while True:
    print("Welcome to Guess the number game!")
    play_again = "y"

    guess_the_number()
    think_the_number()

    print("Do you want to play again? (y/n)")
    play_again = input("Yes - y, No - n: ")

    if play_again == "n":
        break

# GUESS THE WORD GAME
play()