# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

import random
from pathlib import Path
import requests


image_url = "http://shibe.online/api/shibes"
quote_url = "http://quotes.stormconsultancy.co.uk/random.json"

image_link = requests.get(image_url).json()[0]
quote = requests.get(quote_url).json()
# breakpoint()  # Inspect the structure of what you get back

q = quote["quote"]
ql = q.split()
random.shuffle(ql)
shibed = ["WOW" if len(w) < 5 else w for w in ql]
shquote = " ".join(shibed)

f = Path().cwd().joinpath("sites", "shibe5.html")

f.write_text(
    f"""<h1>{shquote}</h1>
<img src={image_link} width=800>"""
)



"""
CONCEPTS
========

- external libraries, `pip`, virtual environments
- web interactions, interfacing with APIs
- reading documentation
- GET requests
- JSON
- `breakpoint()` debugging
- dictionaries, lists
- advanced list comprehensions
- string methods
- the `random` module
- simple HTML
- writing to files, `pathlib` revisited
- running a server with python `http.server` on localhost

"""