# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

pointslost = 0
pointswon = 0 
set_ = set()
while pointslost > -5 and pointswon < 10:
    val = input("Enter New Integer Value: ")
    if val in set_:
        pointslost -= 1
    else:
        set_.add(val)
        pointswon +=1

if pointswon == 10:
    print(set_)
    print("You win!")

if pointslost == -5:
    print(set_)
    print("You lost!")

