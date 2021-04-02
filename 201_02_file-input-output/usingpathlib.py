# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file

from pathlib import Path


data_path = Path("/Users/martin/Documents/codingnomads/course-dev/python/labs/python-201/02_201/file-i-o/")

with open(data_path.joinpath("filecounts.csv"), "r") as fin:
    print(fin.read())
