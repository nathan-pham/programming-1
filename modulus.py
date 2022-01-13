# Filename:     modulus.py
# Date:         1/7/2022
# Purpose:      Use modulus to find prime numbers
# Name:         Nathan Pham

# prompt for an integer
def prompt(message: str) -> int:
    try: return int(input(message))
    except ValueError: return prompt(message)

# determine if a number is prime
def is_prime(n: int) -> bool:

    # if n is less than or equal to 1 then it cannot be prime
    if n <= 1:
        return False

    # divide n by all numbers leading to it; if it divides evenly it cannot be prime
    for i in range(2, n):
        if n % i == 0:
            return False

    # must be prime
    return True

while True:
    n = prompt("Enter a number > ")
    print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")