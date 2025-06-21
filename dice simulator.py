import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print(" Dice Simulator")
    while True:
        input("Press Enter to roll the die...")
        result = roll_dice()
        print(f"You rolled: {result}")

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("NOOOO!")
            break

if __name__ == "__main__":
    main()
