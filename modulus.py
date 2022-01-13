# Filename:     modulus.py
# Date:         1/7/2022
# Purpose:      Use modulus to find prime numbers
# Name:         Nathan Pham

from typing import List

# prompt for an integer
def prompt(message: str) -> int:
    try: return int(input(message))
    except ValueError: return prompt(message)

# determine if a number is prime
def is_prime(n: int) -> List[int]:

    factors = []

    # if n is less than or equal to 1 then it cannot be prime
    if n <= 1:
        factors.append(1)

    # divide n by all numbers leading to it; if it divides evenly it cannot be prime
    for i in range(2, n):
        if n % i == 0 and n != i:
            factors.append(i)

    # must be prime
    return factors

# condense an array of ints into a str
def condense(arr: List[int]) -> str:
    return ", ".join([ str(i) for i in arr ])    

if __name__ == "__main__":
    while True:
        n = prompt("Enter a number > ")
        factors = is_prime(n)

        print(f"{n} is prime" if len(factors) == 0 else f"{n} is not prime and is divisible by {condense(factors)}.")