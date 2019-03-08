import csv

data = [
    ['name', 'desc', 'cost'],
    ['apple', 'some, apple', '100'],
    ['potato', 'some, potato', '200'],
    ['onion', 'some, onion', '300'],
]

dict_data = [
    {
        'name': 'apple',
        'desc': 'some, apple',
        'cost': '100'
    }
]

with open('cvs/data.csv', 'w') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(data)


with open('csv/dict_data.csv', 'w') as file:
    write = csv.DictWriter(
        file,
        fieldnames=['name', 'desc', 'cost'],
        quoting=csv.QUOTE_NONNUMERIC
    )
    write.writeheader()
    for itm in dict_data:
        write.writerow(itm)