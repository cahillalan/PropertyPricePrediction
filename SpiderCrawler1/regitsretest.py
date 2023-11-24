import csv
import re
import string

with open('..\\PPR-2018.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    a = 0
    all_houses = []
    for i in readCSV:
        hinfo = {
            'DateOfSale': '',
            'address': '',
            'price': '',
            'VAT': ''

        }
        if i and a > 0:
            #i[1] = re.findall(r"'(.*?)'", i[1], re.DOTALL)
            hinfo['DateOfSale'] = i[0]
            hinfo['address'] = i[1]
            hinfo['price'] = i[4]
            hinfo['VAT'] = i[6]

            all_houses.append(hinfo)
        a += 1


for h in all_houses:
    h['DateOfSale']= h['DateOfSale'].split('/')
    if type(h['address']) is not type('string'):
        h['address'] = ''.join(str(h['address']))

with open('..\\PPR-2019.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    a = 0
    ninteen_houses = []
    for i in readCSV:
        hinfo = {
            'DateOfSale': '',
            'address': '',
            'price': '',
            'VAT': ''

        }
        if i and a > 0:
            # i[1] = re.findall(r"'(.*?)'", i[1], re.DOTALL)
            hinfo['DateOfSale'] = i[0]
            hinfo['address'] = i[1]
            hinfo['price'] = i[4]
            hinfo['VAT'] = i[6]

            ninteen_houses.append(hinfo)
        a += 1

for h in ninteen_houses:
    h['DateOfSale'] = h['DateOfSale'].split('/')
    if type(h['address']) is not type('string'):
        h['address'] = ''.join(str(h['address']))
eighteenhouses = []
for h in all_houses:
    eighteenhouses.append(h)
for h in ninteen_houses:
    eighteenhouses.append(h)

counter = 0
print(len(eighteenhouses))
for h in eighteenhouses:
    if 'dublin 15' in h['address'].lower():
        counter+=1
print(counter)
keys = eighteenhouses[0].keys()
with open('..\\..\\Database\\propregister.csv', 'w+') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(eighteenhouses)
