import json

with open('json/data.json','w') as file:
    json.dump(data, file, sort_keys=True, indent=2)

with open('json/data.json') as file:
    