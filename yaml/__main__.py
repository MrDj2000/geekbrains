import yaml

with open('yaml/conf.yml','w') as file:
    yaml.dump(data, file, sort_keys=True, indent=2)
