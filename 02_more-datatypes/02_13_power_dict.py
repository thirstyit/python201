# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}


dict_ = {}

key_ = 1

while key_ <= 10:
    value = key_ * key_
    dict_[key_] = value
    key_+=1

print(dict_)