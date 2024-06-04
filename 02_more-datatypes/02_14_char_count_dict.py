# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}


user_input = "hello there"

result = {}

temp_list = list(user_input)


for c in temp_list:
    if c in result:
        result[c] += 1
    else:
        result[c] = 1

print(result) 