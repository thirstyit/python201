# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

tup = tuple(string)

lis = list(tup)

lis[0] = 'k'

tup2 = tuple(lis)

print(tup2)