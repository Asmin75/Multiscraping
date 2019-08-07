import json
import re
with open("items.json") as f:
    data = json.load(f)
    search = str(input("Enter word to find reference link:"))
    for item in data:
        match = re.findall(search, str(item['h2'] or item['h3']))
        if match:
            print("word matched: %s ==> url: %s" % (search, item['url']))

