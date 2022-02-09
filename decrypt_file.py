# Filename:     decrypt_file.py
# Date:         2/9/2022
# Purpose:      Brute force a Ceasar Cipher
# Name:         Nathan Pham


from ghetto_encryption import decrypt, encrypt
from nltk.corpus import stopwords


def main() -> None:
    filtered_words = [word for word in stopwords.words("english") if len(word) >= 3]
    with open("files/encrypted_file.txt", "r", encoding="utf8") as file:
        encrypted = file.read().strip()

        for i in range(256):
            potential_decrypted = decrypt(encrypted, i).lower()

            for word in filtered_words:
                if word in potential_decrypted.split(' '):
                    print(potential_decrypted)
                    print(f"key = {i}")
                    return 

        print("no match oof")


if __name__ == "__main__":
    main()