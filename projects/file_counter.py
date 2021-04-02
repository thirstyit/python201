from pathlib import Path
from pprint import pprint


path = Path().home() / 'Desktop'
counter = dict()

for f in path.iterdir():
    counter[f.suffix] = counter.get(f.suffix, 1) + 1

pprint(counter)


"""
CONCEPTS

- standard library and importing code
- working with paths
- objects and methods
- iteration, for loop, list comprehensions, lists
- strings
- interacting with the file system
- enumerate
- f-strings, string formatting, string mini-language
- object attributes

"""