# Filename:     ghetto_encryption.py
# Date:         2/8/2022
# Purpose:      Ceasar Cipher
# Name:         Nathan Pham


def main(phrase: str, shift: int) -> None:
    encrypted = encrypt(phrase, shift)

    print_format("original", phrase)
    print_format("encrypted", encrypted)
    print_format("decrypted", decrypt(encrypted, shift))


def print_format(method, phrase) -> None:
    print("%-10s %s" % (method, phrase))


def encrypt(phrase: str, shift: int) -> str:
    return ''.join([chr(ord(character) + shift) for character in phrase])


def decrypt(phrase: str, shift: int) -> str:
    try:
        return ''.join([chr(ord(character) - shift) for character in phrase])
    except ValueError:
        return "invalid shift value"

if __name__ == "__main__":
    main(phrase="Hello World!", shift=3)
