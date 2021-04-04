# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path


data_path = Path.cwd().joinpath("201_02_file-input-output/file-counter")

with open(data_path.joinpath("filecounts.csv"), "r") as fin:
    print(fin.read())
