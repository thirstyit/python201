# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {}

for key1 in dict_1.keys():
    for key2 in dict_2.keys():
        if key1 in dict_2.keys():
            if key1 == key2:
                val = dict_1[key1] + dict_2[key2]
                result[key1] = val
        else:
            result[key1] = dict_1[key1]


for key2 in dict_2.keys():
    if key2 not in dict_1.keys():
        result[key2] = dict_2[key2]


print(result)

