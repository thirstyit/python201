# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input hasn't been added and deduce a point.
# If the user gets loses 5 points, quite the program.
# They wil if they manage to create a set that has more than 10 items.

test_set = set()
points = 5
while True:
    if points < 1:
        print("Improve your memory!")
        break
    if len(test_set) > 10:
        print("You win! Nice brain!")
        break
    num = int(input("Enter a number you haven't entered before: "))
    if num not in test_set:
        test_set.add(num)
    else:
        points -= 1
        print(f"You're repeating yourself... Points left: {points}")
