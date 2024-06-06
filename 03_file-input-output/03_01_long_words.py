# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

wp = Path("/Users/macintosh/Projects/python-201/03_file-input-output/")

with open(wp.joinpath("words.txt"), "r") as word_file:
    words = word_file.read()
    word_list = words.split('\n')
    [print(w) for w in word_list if len(w) > 20]
