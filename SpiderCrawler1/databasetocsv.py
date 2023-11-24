import csv
import sqlite3

db = sqlite3.connect('dafthouses.db')

cursor = db.cursor()
current = cursor.execute('Select * FROM viablehousestable')
currenthouses = []
for i in current:
    a = 0
    hinfo = {
        'price': '',
        'address': '',
        'bedrooms': '',
        'bathrooms': '',
        'type': '',
        'views': '',
        'area': ''
    }
    for t in i:
        if a is 0: hinfo['id'] = t
        if a is 1:
            hinfo['price'] = t
        elif a is 2:
            hinfo['address'] = t.encode("utf-8")
        elif a is 3:
            hinfo['bedrooms'] = t
        elif a is 4:
            hinfo['bathrooms'] = t
        elif a is 5:
            hinfo['type'] = t.encode("utf-8")
        elif a is 7:
            hinfo['area'] = t

        a += 1
    currenthouses.append(hinfo)

keys = currenthouses[0].keys()
with open('viablecsv.csv', 'w+') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(currenthouses)