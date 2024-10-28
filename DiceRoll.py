import random

def roll_dice():
    roll = random.randint(1, 6)
    return roll

def start_game():
    probability = 1 / 6
    print(f"The probability of getting a 6 on the first roll is {probability:.2f}")

    roll = roll_dice()
    print(f"You rolled a {roll}")

    if roll == 6:
        print("The game can be started!")
    else:
        print("Roll again. Best of luck!")

start_game()
