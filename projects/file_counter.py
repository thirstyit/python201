from pathlib import Path
from pprint import pprint


path = Path().home() / 'Desktop'
counter = dict()

for f in path.iterdir():
    counter[f.suffix] = counter.get(f.suffix, 1) + 1

pprint(counter)
