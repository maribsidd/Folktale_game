import random

riddles = [
    ("What has keys but cannot open locks?", "piano"),
    ("What has hands but cannot clap?", "clock"),
    ("What gets wetter the more it dries?", "towel"),
    ("What has a neck but no head?", "bottle"),
    ("What can you catch but not throw?", "cold"),
    ("What has one eye but cannot see?", "needle"),
    ("What goes up but never comes down?", "age"),
    ("What has many teeth but cannot bite?", "comb"),
]

spots = ["desk", "shelf", "drawer", "painting", "box", "carpet"]


def show_spots():
    for i in range(len(spots)):
        print(i + 1, spots[i])


def play():
    code = str(random.randint(100, 999))
    key_spot, note_spot = random.sample(spots, 2)
    moves = 8
    has_key = False
    has_note = False
    done = []

    print("\nYou are locked in a room.")
    print("Find the key and the secret code to escape.")
    print("Every search needs a riddle answer.")

    while moves > 0:
        print("\nMoves left:", moves)
        print("1. Search a spot")
        print("2. Try the door")
        print("3. Check inventory")
        print("4. Quit")
        ch = input("Choose: ").strip()

        if ch == "1":
            show_spots()
            n = input("Which spot? ").strip()
            if not n.isdigit() or int(n) < 1 or int(n) > len(spots):
                print("Invalid choice.")
                continue
            s = spots[int(n) - 1]
            if s in done:
                print("You already searched the", s)
                continue
            q, a = random.choice(riddles)
            print("Riddle:", q)
            ans = input("Answer: ").strip().lower()
            moves -= 1
            if ans != a:
                print("Wrong! The", s, "stays closed.")
                continue
            done.append(s)
            if s == key_spot:
                has_key = True
                print("You found a rusty KEY in the", s)
            elif s == note_spot:
                has_note = True
                print("You found a NOTE in the", s, "- the code is", code)
            else:
                print("Nothing useful in the", s)

        elif ch == "2":
            if not has_key:
                print("The door is locked. You need a key.")
                continue
            g = input("Enter 3 digit code: ").strip()
            moves -= 1
            if g == code:
                print("\nClick! The door opens. YOU ESCAPED!")
                return True
            print("Wrong code. The door stays shut.")

        elif ch == "3":
            print("Inventory:")
            if not has_key and not has_note:
                print("Empty")
            if has_key:
                print("- Rusty key")
            if has_note:
                print("- Note with code", code)

        elif ch == "4":
            print("You gave up.")
            return False

        else:
            print("Invalid choice.")

    print("\nOut of moves! The lights go out. YOU LOSE.")
    print("The code was", code)
    return False


def main():
    wins = 0
    games = 0
    print("=== ESCAPE ROOM ===")
    while True:
        games += 1
        if play():
            wins += 1
        print("Games:", games, "Wins:", wins)
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


main()
