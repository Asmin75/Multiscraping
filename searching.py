import json
import re
with open("items.json") as f:
    data = json.load(f)
    search = str(input("Enter word to find reference link:"))
    for item in data:
        value = list(item.values())
        for i in range(len(v)):
            for j in range(len(value[i])):
                match = re.search(search, value[i][j]) or re.search(search, value[i][j])
                if match:
                    print("word matched: %s ==> url: %s" % (value[i][j], item['url']))

