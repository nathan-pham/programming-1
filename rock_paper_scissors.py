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

    if player_choice == computer_choice:
        print(f"It's a tie! You both chose {player_choice}.")
    elif computer_choice == win_condition:
        print(f"You lose! The computer chose {computer_choice}.")
    else:
        print(f"You win! The computer chose {computer_choice}.")
        return True

    return False

def main() -> None:
    max_games = 5
    scorecard = []

    for i in range(max_games): scorecard.append(game())

    wins = scorecard.count(1)

    print(f"You won {wins} wins" if wins >= 3 else f"You lost {max_games - wins}!")

if __name__ == "__main__": 
    main()