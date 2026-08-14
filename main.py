# import os
from datetime import datetime
from collections import Counter
LOG_FILE = "outputs/execution.log"

def write_log(option):
    # os.makedirs("outputs", exist_ok=True)
    with open("outputs/execution.log", "a") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{now} - {option}\n")


def menu():
    while True:
        print("\n====== CryptoLabX ======")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Attack")
        print("4. Analyze")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Encrypt - Coming Soon")
            write_log("Encrypt")

        elif choice == "2":
            print("Decrypt - Coming Soon")
            write_log("Decrypt")

        elif choice == "3":
            print("Attack - Coming Soon")
            write_log("Attack")

        elif choice == "4":
            print("Analyze - Coming Soon")
            write_log("Analyze")

        elif choice == "5":
            print("Exiting...")
            write_log("Exit")
            break

        else:
            print("Invalid Choice")


def analyze_file(filepath):
    try:
        with open(filepath, "r") as f:
            text = f.read()

        characters = len(text)
        words = len(text.split())
        lines = text.count("\n") + 1 if text else 0
        unique_characters = len(set(text))

        # Count only alphabetic letters
        letters = [ch.lower() for ch in text if ch.isalpha()]
        frequency = Counter(letters)


        print("----- File Analysis -----")
        print(f"Characters       : {characters}")
        print(f"Words            : {words}")
        print(f"Lines            : {lines}")
        print(f"Unique Characters: {unique_characters}")

        print("\nLetter Frequency:")
        for letter, count in sorted(frequency.items()):
            print(f"{letter}: {count}")

    except FileNotFoundError:
        print("File not found.")


# Example
analyze_file("datasets/sample.txt")
if __name__ == "__main__":
    menu()


