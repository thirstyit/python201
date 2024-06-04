# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]


input = "hello world"

words = input.split(' ')

result_list = []

for x in words:
    tup = tuple(list(x))
    result_list.append(tup)


print(result_list)