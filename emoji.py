# Filename:     emoji.py
# Date:         1/12/2022
# Purpose:      Use unicode to print emojis
# Name:         Nathan Pham

def print_emojis() -> None:
    emojis = ["\U0001F600", "\U0001F601", "\U0001F605", "\U0001F606",
              "\U0001F609", "\U0001F60A", "\U0001F60B", "\U0001F60E", "\U0001F60F"]

    for emoji in emojis:
        print(emoji)


if __name__ == "__main__":
    print_emojis()
