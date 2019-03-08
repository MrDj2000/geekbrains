import yaml

data = {
    'entrypoint': 'main.py',
    'host': 'loaclhost',
    'port': 8000
}

with open('yaml/conf.yml', 'w') as file:
    yaml.dump(data, file)

with open('yaml/conf.yml') as file:
    print(
        type(
            yaml.load(file)
        )
    )

 #   yaml.dump(data, file, sort_keys=True, indent=2)
