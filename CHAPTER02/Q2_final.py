import random


def main():
    name = "koudai"
    initial = name[0].upper()
    while True:
        random_letter = chr(random.randint(65, 90))
        print(random_letter)
        if random_letter == initial:
            print("終了します。")
            break


if __name__ == "__main__":
    main()
