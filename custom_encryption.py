# Filename:     custom_encryption.py
# Date:         2/9/2022
# Purpose:      custom encryption stuff (RSA)
# Name:         Nathan Pham


"""
source: https://en.wikipedia.org/wiki/RSA_(cryptosystem)

It is difficult to factor the product of two large prime numbers (basically a one-way function because it so hard); this is why it is slow but also why it is so secure if a large enough key is used.

Even when knowing e, n, and m, it is difficult to find d. 
"""


from typing import Union, Tuple, List
from math import lcm
import random


def is_prime(num: int) -> bool:
    """
    determine if a number is prime
    """

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_coprime(a: int, b: int) -> int:
    """
    euclid's algorithm to verify if two numbers are coprime
    """
    return a if b == 0 else is_coprime(b, a % b)


def generate_prime(max: int = 100) -> int:
    """
    generate a prime number
    """
    
    while True:
        num = random.randint(1, max)
        if is_prime(num):
            return num

def find_coprime(num: int) -> Union[int, None]:
    """
    find a number that is coprime with the totient and > 1
    """

    for i in range(2, num):
        if is_coprime(i, num) == 1:
            return i


def generate_keypair() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    generate a public and private key pair
    """

    p = generate_prime(1000)
    q = generate_prime(1000)
    n = p * q

    # compute totient
    phi = lcm(p - 1, q - 1)

    # find a coprime
    e = find_coprime(phi)
    if e is None: return generate_keypair()

    # the modular multiplicative inverse of e (mod λ(n))
    d = 1
    while (d * e) % phi != 1:
        d += 1

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def encrypt(message: str, public_key: Tuple[int, int]) -> str:
    """
    encrypt a message using a public key
    """

    e, n = public_key
    return [(ord(c) ** e) % n for c in message]


def decrypt(encrypted: List[int], private_key: Tuple[int, int]) -> str:
    """
    decrypt a message using a private key
    """

    d, n = private_key
    return "".join([chr((c ** d) % n) for c in encrypted])


def main() -> None:
    public_key, private_key = generate_keypair()
    message = input("enter a message > ")
    encrypted = encrypt(message, public_key)
    decrypted = decrypt(encrypted, private_key)

    print("%-10s: %s" % ("message", message))
    print("%-10s: %s" % ("encrypted", encrypted))
    print("%-10s: %s" % ("decrypted", decrypted))


if __name__ == "__main__":
    main()