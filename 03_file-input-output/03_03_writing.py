# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

from pathlib import Path

wp = Path("/Users/macintosh/Projects/python-201/03_file-input-output/")


with open(wp.joinpath("words.txt"), "r") as word_file:
    words = word_file.read()
    word_list = words.split()

    reverse_words = []

    for w in word_list:
        reverse_words.insert(0, w)


with open(wp.joinpath("words_reverse.txt"), "w") as reverse_file:
    for w in reverse_words:
        reverse_file.write(w)
        reverse_file.write('\n')
    

