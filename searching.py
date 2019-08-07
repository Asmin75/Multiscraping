import json
import re
with open("items.json") as f:
    data = json.load(f)
    search = str(input("Enter word to find reference link:"))
    for item in data:
        v = list(item.values())
        for i in range(len(v)):
            for j in range(len(v[i])):
                match = re.search(search, v[i][j]) or re.search(search, v[i][j])
                if match:
                    print("word matched: %s ==> url: %s" % (v[i][j], item['url']))

