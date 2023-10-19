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

climb_ladder(5, 2)
climb_ladder(2, 5)
