# Filename:     while_loop.py
# Date:         1/7/2022
# Purpose:      Demonstrate while loop
# Name:         Nathan Pham

# main method
def main(max_guesses: int, secret: str) -> bool:
    guess_count = 0

    # loop until max guesses reached
    while guess_count < max_guesses:
        
        # prompt for a guess
        guess = input("\nEnter a password > ")

        # if guess is correct, return True 
        if guess == secret:
            print("Access granted!")
            return True
        
        # otherwise, increment guess count
        else: print(f"Access denied! You have {max_guesses - (guess_count + 1)} guesses left.")

        guess_count += 1

    print("I guess you couldn't crack the code! Better luck next time!")
    return False

main(3, "secret")