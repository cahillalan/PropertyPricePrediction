import sqlite3
import re
import csv

db = sqlite3.connect('dafthouses.db')

cursor = db.cursor()
current = cursor.execute('Select * FROM currenthouses')
currenthouses = []
for i in current:
    a = 0
    hinfo = {
                'price': '',
                'address': '',
                'bedrooms': '',
                'bathrooms': '',
                'type': '',
                'details': '',
                'views': '',
                'all_prices': '',
                'price_dates': '',
                'area': ''
            }
    for t in i:
        if a is 0:hinfo['id'] = t
        if a is 1:hinfo['price']=t
        elif a is 2: hinfo['address']=t
        elif a is 3:hinfo['bedrooms'] = t
        elif a is 4:hinfo['bathrooms'] = t
        elif a is 5:hinfo['type'] = t
        elif a is 6:hinfo['details'] = t
        elif a is 7:hinfo['views'] = t
        elif a is 8:hinfo['all_prices'] = t
        elif a is 9:hinfo['price_dates'] = t
        elif a is 10:hinfo['area'] = t

        a+=1
    currenthouses.append(hinfo)

garage = 0
conservatory = 0
underfloorheating = 0
ensuite = 0
garden = 0
land = 0
acres = 0
count = 0
hectare = 0
mylist = []
newlist = []

for i in currenthouses:
    myacre = ''
    myacre = re.search(r'([-+]?\d*\.\d+|\d+) acres', i['details'])
    if myacre:
        mylist.append(myacre.group(1))
        mylist.append(i['address'])
    else:
        myacre = re.search(r'(\d+) Acres', i['details'])
        if myacre: mylist.append(myacre.group(1))
        else:
            myacre = re.search(r'(\d+)Acres', i['details'])
            if myacre: mylist.append(myacre.group(1))
            else:
                myacre = re.search(r'(\d+)acres', i['details'])
                if myacre: mylist.append(myacre.group(1))
                else:
                    myacre = re.search(r'(\d+) acres', i['details'])
                    if myacre: mylist.append(myacre.group(1))
    if 'garage' in i['details']:
        garage +=1
    elif 'Garage' in i['details']:
        garage +=1
    if 'garden' in i['details']:
        garden += 1
    elif 'Garden' in i['details']:
        garden += 1
    if 'conservatry' in i['details']:
        conservatory += 1
    elif 'Conservatory' in i['details']:
        conservatory += 1
    if 'underfloor' in i['details']:
        underfloorheating += 1
    elif 'under-floor' in i['details']:
        underfloorheating += 1
    elif 'UnderFloor' in i['details']:
        underfloorheating += 1
    elif 'Under-Floor' in i['details']:
        underfloorheating += 1
    if 'ensuite' in i['details']:
        ensuite += 1
    elif 'en-suite' in i['details']:
        ensuite += 1
    elif 'EnSuite' in i['details']:
        ensuite += 1
    elif 'En-Suite' in i['details']:
        ensuite += 1
    if 'acres' in i['details']:
        acres += 1
    elif 'Acres' in i['details']:
        acres += 1
    if 'Hectare' in i['details']:
        hectare += 1

    #mytown = re.search(r'(\d+) Acres', i['details'])
    #if mytown: mylist.append(mytown.group(1))
    #mytown = re.search(r'(\d+)Acres', i['details'])
    #if mytown: mylist.append(mytown.group(1))
    #mytown = re.search(r'(\d+)acres', i['details'])
    #if mytown: mylist.append(mytown.group(1))
    count += 1

print('Ensuite : ', ensuite)
print('UnDerFloor : ', underfloorheating)
print('Conservatory : ', conservatory)
print('Garden : ', garden)
print('Garage : ', garage)
print('Acres : ', acres)
print('Hectare : ', hectare)
print('Total :', count)
#for i in mylist: print(i)


