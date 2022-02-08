# Filename:     poem_emoji.py
# Date:         2/8/2022
# Purpose:      Replace words with emojis
# Name:         Nathan Pham


from random import randint, choice


# main method
def main(filename: str) -> None:
    _filename = f"files/{filename}.txt"
    max_replacements = 5

    with open(_filename, 'r') as file:
        poem = list(file.read())

        for i in range(max_replacements):
            char_i = randint(0, len(poem))
            poem[char_i] = randemoji()

        poem = ''.join(poem)
        write(filename + "_copy", poem)
        print(poem)


# get a random emoji
def randemoji() -> str:
    return choice(list(u"🍔🔮🌟😂⚡😅🤡😔🥺👋🚀🔥🔌🐛"))


# write to a file
def write(filename=str, text=str) -> None:
    _filename = f"files/{filename}.txt"
    with open(_filename, 'w', encoding="utf8") as file:
        file.write(text)


if __name__ == "__main__":
    main(filename="i_too_poem")
