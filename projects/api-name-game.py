# import requests

# min_len = 6
# max_len = 6
# URL = f"https://uzby.com/api.php?min={min_len}&max={max_len}"

# response = requests.get(URL)
# print(response.text)

import requests


name_length = 0
while not (name_length >= 2 and name_length <= 40):
    original_name = input("Enter your name: ")
    name_length = len(original_name)

URL = f"https://uzby.com/api.php?min={name_length}&max={name_length}"

try:
    response = requests.get(URL)
    name = response.text
    print(f"Welcome to the dungeon! In this world, you won't be {original_name}.")
    print(f"Instead, you'll be know as {name.upper()}.")
except requests.exceptions.ConnectionError as e:
    print("You gotta be online to get your name!")