from uzwords import words
import random as rm

# GUESS THE NUMBER GAME FUNCTIONS
def guess_the_number():
    computer_choice = rm.randint(0, 100)
    attempts = 1

    while attempts <= 10:
        n = int(input("Please enter a number between 0 and 100: "))
        if n == computer_choice:
            print("Correct!")
            break
        elif n > computer_choice:
            print("Sorry, the number you entered is too high!")
        else:
            print("Sorry, the number you entered is too low!")
        attempts = attempts + 1

    if attempts == 10:
        print("You lose!")
    else:
        print("You win!")
        print(f"You guessed the number in {attempts} attempts!")

def think_the_number():
    input("Think number between 0 and 100, press enter to continue...")

    low = 0
    high = 100
    attempts = 1

    while attempts <= 10:
        computer_guess = (low + high) // 2
        print(f"Computer guess: {computer_guess}")

        sign = input("+ (high), - (low), = (guessed): ")

        if sign == "+":
            low = computer_guess + 1
        elif sign == "-":
            high = computer_guess - 1
        elif sign == "=":
            print(f"🎉 Computer guessed the number in {attempts} attempts!")
            return
        else:
            print("Wrong input!")
            continue

        attempts += 1

    print("❌ Computer didnt guess the number!")

# GUESS THE WORD GAME FUNCTIONS

def get_word():
    word = rm.choice(words)
    while ("-" in word) or ("+" in word):
        word = rm.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ""
    print(f"The length of word is {len(word)}")
    while len(word_letters) > 0:
        print(display(user_letters, word))
        if len(user_letters) > 0:
            print(f"The letters you entered were {user_letters}")

        letter = input("Enter the letter: ").upper()
        if letter in user_letters:
            print(f"You entered this letter, try another letter")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter}      was true")
        else:
            print(f"{letter} was false")
        user_letters += letter
    print(f"Congrats! {word} was guessed in {len(user_letters)} attempts!")
