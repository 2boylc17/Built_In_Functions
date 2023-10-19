import random


def number_guess():
    value = random.randint(1, 100)
    correct = False
    while not correct:
        guess = int(input("Make a guess between 1 & 100: "))
        if guess == value:
            print("That's correct!")
            correct = True
        elif guess < value:
            print("Higher")
        else:
            print("Lower")
