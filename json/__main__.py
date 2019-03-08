import json

data = [
    {
        'name': 'apple',
        'desc': 'some apple',
        'cost': 235
    },
    {
        'name': 'apple',
        'desc': 'some apple',
        'cost': 236
    },
    {
        'name': 'apple',
        'desc': 'some apple',
        'cost': 237
    }
]

with open('json/data.json', 'w') as file:
    json.dump(data, file, sort_keys=True, indent=2)

with open('json/data.json') as file:
    print(
        type(
            json.load(file)
        )
    )