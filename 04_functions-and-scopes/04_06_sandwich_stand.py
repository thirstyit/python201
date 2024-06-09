# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.


def make_sandwich(bread, *args):
    print(bread)
    for t in args:
        print(t)
        
    print(bread)


make_sandwich("Wholemeal", "Ham", "Cheese", "Sauce")