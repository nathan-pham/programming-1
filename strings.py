def prompt(message: str) -> str:
    return input(message)

def main() -> None:
    while True:
        name = prompt("Enter a name > ").lower()
        frequency = {}

        if name == "quit":
            break

        for char in name:
            frequency[char] = frequency.get(char, 0) + 1

        for char, n in frequency.items():
            print(f"The name {name} contains {n} {char}'s.")

if __name__ == "__main__":
    main()