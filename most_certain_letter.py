# Filename:     most_certain_letter.py
# Date:         2/8/2022
# Purpose:      get the most of a certain letter in a list
# Name:         Nathan Pham


def count_letters(word: str, letter: str) -> int:
    """
    count the number of times a letter appears in a word
    """
    
    count = 0

    for char in word:
        if char == letter:
            count += 1

    return count


def main() -> None:
    """
    main method
    """

    letter = input("enter a character > ")
    array = ['baboon', 'stargaard', 'maddog', 'frenchfry', 'tote', 'unbrella',
             'nigeria', 'racecar', 'mommy', 'elephant', 'hippo', 'sillyputty', 'nitros oxide']

    counted_array = [count_letters(word, letter) for word in array]
    most_occurences = array[counted_array.index(max(counted_array))]

    print(f"the most occurences of {letter} is in {most_occurences}")


if __name__ == "__main__":
    main()
