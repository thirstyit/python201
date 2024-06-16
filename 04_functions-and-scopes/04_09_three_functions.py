# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def sams_func():
    return 5

def sams_big_func():
    temp = sams_func() + 7
    return temp


def printer():
    print(sams_big_func())


printer()