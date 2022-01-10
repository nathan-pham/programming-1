import random

def prompt(message: str) -> int:
    try: return int(input(message))
    except ValueError: return prompt(message)

def guessing_game() -> None:
    
    min_number = 1
    max_number = 100
    max_guesses = 3

    number = random.randint(min_number, max_number)
    guess = 0

    print(f"I'm thinking of a number between {min_number} and {max_number}.")

    for guess in range(max_guesses):
        print(f"You have {max_guesses - guess} guesses.")
        guess = prompt("What is your guess? ")

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You got it!")
            break

    if guess != number: print(f"Sorry, the number was {number}.")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y": guessing_game()
    else: print("\nThanks for playing!")

guessing_game()