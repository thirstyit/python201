# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

test_string = "This is a really really long string"

split_list = test_string.split(' ')

result = max(set(split_list), key=split_list.count)

print(result)

