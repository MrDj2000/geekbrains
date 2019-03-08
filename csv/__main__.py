import csv



with open('csv/dict_data.csv', 'w') as file:
    write = csv.DictWriter(
        file,
        fieldnames=['name','desc','cost'],
        quoting=csv.quote_nonnumeric
    )
    write.writeheader()
    for itm in dict_data:
        write.writerow(itm)