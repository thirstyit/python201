# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!


input_dict = {"item1": 5, "item2": 6, "item3": 1}

result_list = []

#for idx, key in enumerate(input_dict):


#result_list.append()

first = 0

for i in input_dict.items():
    if first == 0:
        result_list.append(i)
        first += 1
    else:
        for r in result_list:
            if input_dict[i[0]] < r[1]:
                result_list.insert(result_list.index(r), i)
                break
            elif input_dict[i[0]] >= r[1]:
                result_list.insert(result_list.index(r)+1, i)
                break
            


print(result_list)

