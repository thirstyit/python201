# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path

desktop = Path("/Users/macintosh/Desktop/")
csv_output_path = Path("/Users/macintosh/Projects/python-201/03_file-input-output/")

png = 0
jpg = 0
xlsx = 0

for file in desktop.glob('*'):
    if file.suffix == '.png':
        png+=1
    if file.suffix == '.jpg':
        jpg+=1
    if file.suffix == '.xlsx':
        xlsx+=1

output = str(png) + ", " + str(jpg) + ", " + str(xlsx)

with open(csv_output_path.joinpath("file_count.csv"), "w") as csv_file:
    csv_file.write(output)
    csv_file.write('\n')

          
