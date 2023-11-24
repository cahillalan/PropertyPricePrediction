import sqlite3
import re
import csv

def manipulatedata():
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


    myhouses = currency_and_nulls(currenthouses)
    myhouses = currency_and_nulls(myhouses)
    myhouses = currency_and_nulls(myhouses)
    myhouses = removenoprice(myhouses)
    myhouses = removenoprice(myhouses)
    myhouses = removenoprice(myhouses)
    myhouses = removenoprice(myhouses)
    myhouses = change_to_int(myhouses)


    cursor.execute('DELETE FROM viablehousestable')
    for house in myhouses:
        cursor.execute('''INSERT INTO viablehousestable(price,address,bedrooms,bathrooms,type,details,views,allprices,pricedates,area)
                              VALUES(?,?,?,?,?,?,?,?,?,?)''', (house['price'], house['address'], house['bedrooms'],
                                                               house['bathrooms'], house['type'],
                                                               house['details'], house['views'],
                                                               house['all_prices'], house['price_dates'],
                                                               house['area']))
        print('house entered')

    db.commit()

    for house in myhouses:
        if not house['price']:
            print(house['address'])


def currency_and_nulls(houses):
    b = 0
    for t in houses:
        houses[b]['price'] = re.findall('\d+', t['price'])
        if houses[b]['bedrooms']:
            houses[b]['bedrooms'] = re.findall('\d+', str(t['bedrooms']))
        if houses[b]['bathrooms']:
            houses[b]['bathrooms'] = re.findall('\d+', str(t['bathrooms']))

        if houses[b]['price']:
            houses[b]['price'] = ''.join(houses[b]['price'])
        else:
            houses[b]['price'] = ''
        if houses[b]['bedrooms']:
            houses[b]['bedrooms'] = ''.join(houses[b]['bedrooms'])
        else:
            houses[b]['bedrooms'] = ''
        if houses[b]['bathrooms']:
            houses[b]['bathrooms'] = ''.join(houses[b]['bathrooms'])
        else:
            houses[b]['bathrooms'] = ''
        b += 1

    viable = houses
    for house in houses:
        if not house['price']:
            viable.remove(house)
    for house in houses:
        if not house['bedrooms']:
            viable.remove(house)
    for house in houses:
        if not house['bathrooms']:
            viable.remove(house)

    for house in houses:
        if house['price'] is '0' or house['bedrooms'] is '0' or house['bathrooms'] is '0' or house['area'] is 0:
            viable.remove(house)


    return viable


def removenoprice(houses):
    viable = houses
    for house in houses:
        if not house['price']:
            viable.remove(house)
    for house in houses:
        if len(house['price']) < 5:
            viable.remove(house)
    for house in houses:
        if len(house['price']) > 8:
            viable.remove(house)

    return viable


def change_to_int(houses):
    for house in houses:
        house['price'] = float(house['price'])
        house['bathrooms'] = int(house['bathrooms'])
        house['bedrooms'] = int(house['bedrooms'])
        house['area'] = int(house['area'])

    return houses


manipulatedata()