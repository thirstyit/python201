# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

from pathlib import Path

wp = Path("/Users/macintosh/Projects/python-201/03_file-input-output/")

with open(wp.joinpath("words.txt"), "r") as word_file:
    words = word_file.read()
    word_list = words.split('\n')

   
    total_words = 0

    min_word_length = len(word_list[0])
    max_word_length = len(word_list[0])

    for w in word_list:
        word_length = len(w.strip())
        if word_length < min_word_length and word_length != 0:
            min_word_length = word_length
        if word_length > max_word_length:
            max_word_length = word_length
        
        total_words+=1

    short_words = set()
    long_words = set()

    for w in word_list:
        word_length = len(w)
        if word_length == min_word_length:
            short_words.add(w)
        if word_length == max_word_length:
            long_words.add(w)

print(str(total_words) + "\n")
print(short_words)
print(long_words)
        
