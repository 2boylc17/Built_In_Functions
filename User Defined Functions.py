def listen():
    print("What sound did you hear? ")
    sound = input("")
    print(f"That was a loud {sound}!")


def identify():
    print("What do you see? ")
    obj = input("")
    if obj == "boulder":
        print("Time to run!")
    else:
        print("We will be fine")


def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    if plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    if plan == "cross bridge ahead":
        print("That might just work! Let's go!")


def cross_bridge(steps):
    for x in range(steps):
        print("Crossed step")
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")


def climb_ladder(remaining, crossed):
    if remaining >= crossed:
        print("Still some way to go!")
    else:
        print("Almost there!")


def display_ladder(steps):
    for count in range(steps):
        print("|   |")
        print("|---|")
    print("|   |")


def create_ladder():
    many = int(input("How long is the ladder? "))
    return many


def sum_weights(char, inv):
    total = char + inv
    print(f"The sum of weights is {total}")


def avg_weights(char, inv):
    total = (char + inv) / 2
    print(f"The average of weights is {total}")


def run():
    x = int(input("What is the character's weight? "))
    y = int(input("What is the inventory's weight? "))
    z = input("sum or average? ")
    if z == 'sum':
        sum_weights(x, y)
    else:
        avg_weights(x, y)


run()
