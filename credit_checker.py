# Filename:     credit_checker.py
# Date:         1/18/2022
# Purpose:      Simple algorithm to validate a credit card number
# Name:         Nathan Pham


from typing import List


def digit_sum(number: str) -> List[int]:
    return sum([int(i) for i in list(str(number))])


def validate(number: str) -> int:
    number = ''.join(number.split(' '))
    return digit_sum(''.join(str(digit_sum(number[i]) * 2) if i % 2 == 0 else number[i] for i in range(len(number)))) % 10 == 0

if __name__ == "__main__":
    valid = validate("3141 4352 7221 1006")
    print("Valid credit card" if valid else "Invalid credit card")