# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here

randlist.sort()

rg = len(randlist)

mainlist = []

if rg % 2 == 0:
    start = 0
    doub = 2
    while doub <= rg:
        splitbyTwo = randlist[start:doub]
        doub += 2
        start += 2
        mainlist.append(tuple(splitbyTwo))

if rg % 2 == 1:
    start = 0
    doub = 2
    while doub <= rg:
        splitbyTwo = randlist[start:doub]
        doub += 2
        start += 2
        mainlist.append(tuple(splitbyTwo))
    mainlist.append((0, randlist[-1]))


print(mainlist)