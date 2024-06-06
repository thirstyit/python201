# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.
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

with open(csv_output_path.joinpath("file_count.csv"), "a") as csv_file:
    csv_file.write(output)
    csv_file.write('\n')

          
