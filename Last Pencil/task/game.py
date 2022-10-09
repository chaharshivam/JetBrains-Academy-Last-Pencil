names = ["John", "Jack"]


def main():
    print("How many pencils would you like to use:")
    pencils = get_pencils()
    print("Who will be the first (John, Jack):")
    name = get_first_player()

    print("|" * pencils)

    turn = names.index(name)
    while pencils > 0:
        print(f"{names[turn % 2]}'s turn:")
        if names[turn % 2] == "Jack":
            n = take_pencils_bot(pencils)
        else :
            n = take_pencils(pencils)
        pencils -= n
        if pencils == 0:
            print(f"{names[(turn + 1) % 2]} won!")
            break

        print("|" * pencils)
        turn += 1


def take_pencils(max_count):
    while True:
        number = input()

        if not number.isnumeric():
            print("Possible values: '1', '2', '3'")
            continue

        number = int(number)

        if number not in (1, 2, 3):
            print("Possible values: '1', '2', '3'")
            continue

        if number > max_count:
            print("Too many pencils were taken")
            continue

        return number


def get_first_player():
    while True:
        name = input()
        if name not in names:
            print("Choose between 'John' and 'Jack':")
            continue

        return name


def get_pencils():
    while True:
        number = input()

        if not number.isnumeric():
            print("The number of pencils should be numeric")
            continue

        number = int(number)

        if number <= 0:
            print("The number of pencils should be positive")
            continue

        return number

def take_pencils_bot(max_count):
    if max_count % 4 == 1:
        print(1)
        return 1
    elif max_count % 4 == 0 and max_count >= 4:
        print(3)
        return 3
    else:
        print(max_count % 4 -1)
        return max_count % 4 - 1

if __name__ == "__main__":
    main()