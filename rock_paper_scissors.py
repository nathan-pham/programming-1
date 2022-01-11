from random import choice
from typing import List

def prompt(message: str, enforce: List[str] = []) -> str:
    answer = input(message)
    return answer if answer in enforce else prompt(message, enforce)

def game() -> bool:
    options = ["rock", "paper", "scissors"]

    computer_choice = choice(options)
    player_choice = prompt(f"\nEnter your choice ({', '.join(options)}): ", options)

    win_condition = list(reversed(options))[(options.index(player_choice) + 1) % len(options)]

    print(f"\nYou chose {player_choice} and the computer chose {computer_choice}.")

    return [
        player_choice == computer_choice, # tie         (index: 0)
        computer_choice == win_condition, # you lose    (index: 1)
        True                              # you win     (index: 2)
    ].index(True)

def main() -> None:
    max_games = 5
    scorecard = []

    for i in range(max_games): 
        result = game()
        scorecard.append(result)

        print(["A tie!", "You've lost!", "You win!"][result])
        print(f"You've won {scorecard.count(2)} out of {i + 1} games.")
        print(f"The computer has won {scorecard.count(1)} out of {i + 1} games.")

    wins = scorecard.count(1)

    print(f"You won {wins} wins" if wins >= 3 else f"You lost {max_games - wins}!")

if __name__ == "__main__": 
    main()