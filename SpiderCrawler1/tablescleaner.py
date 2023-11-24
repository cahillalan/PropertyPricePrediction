import sqlite3
import re

def addtofulltables():
    print('started')
    db = sqlite3.connect('dafthouses.db')
    cursor = db.cursor()
    current = cursor.execute('Select * FROM currenthouses')
    print('b')
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


    viablehouses = []
    allviable = cursor.execute('Select * FROM mainhousestable')
    print('c')
    for i in allviable:
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
            if a is 1:hinfo['price'] = t
            elif a is 2:hinfo['address'] = t
            elif a is 3:hinfo['bedrooms'] = t
            elif a is 4:hinfo['bathrooms'] = t
            elif a is 5:hinfo['type'] = t
            elif a is 6:hinfo['details'] = t
            elif a is 7:hinfo['views'] = t
            elif a is 8:hinfo['all_prices'] = t
            elif a is 9:hinfo['price_dates'] = t
            elif a is 10:hinfo['area'] = t
            a += 1

        viablehouses.append(hinfo)

    print('d')
    current = currenthouses
    for i in currenthouses:
        # loop through the list and any values that are already in the viable list will not be added again
        for viable in viablehouses:
            if i['address'] == viable['address'] and i['price'] == viable['price']:
                current.remove(i)
                break
    for house in current:
        viablehouses.append(house)

    cursor.execute('DELETE FROM mainhousestable')
    for house in viablehouses:
        cursor.execute('''INSERT INTO mainhousestable(price,address,bedrooms,bathrooms,type,details,views,allprices,pricedates,area)
                              VALUES(?,?,?,?,?,?,?,?,?,?)''', (house['price'], house['address'], house['bedrooms'],
                                                               house['bathrooms'], house['type'],
                                                               house['details'], house['views'],
                                                               house['all_prices'], house['price_dates'],
                                                               house['area']))
        print('house entered')

    db.commit()



