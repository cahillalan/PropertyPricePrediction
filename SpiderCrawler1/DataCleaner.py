import sqlite3
import re
import csv

def create_csvs() :
    db = sqlite3.connect('dafthouses.db')
    #import database and transfer it to a dictionary
    cursor = db.cursor()
    current = cursor.execute('Select * FROM mainhousestable')
    myhouses = []
    for i in current:

        a = 0
        hinfo = {
                    'price': '',
                    'address': '',
                    'bedrooms': '',
                    'bathrooms': '',
                    'type': '',
                    'details': '',
                    'area': ''
                }
        for t in i:

            if a is 1:hinfo['price']=t
            elif a is 2: hinfo['address']=t.encode("utf-8")

            elif a is 3:hinfo['bedrooms'] = t
            elif a is 4:hinfo['bathrooms'] = t
            elif a is 5:hinfo['type'] = t.encode("utf-8")
            elif a is 6:hinfo['details'] = t
            #elif a is 7:hinfo['views'] = t
            elif a is 10:hinfo['area'] = t

            a+=1
        myhouses.append(hinfo)

    #call the cleaning functions and reinitise myhouses to the return value
    print('Starting Cleaning')
    myhouses = additional_columns(myhouses)
    myhouses = currency_and_strings(myhouses)
    print('Currency')
    myhouses = removenovalues(myhouses)
    print('nullvals')
    myhouses = change_to_int(myhouses)
    print('Changed Strings to Int')
    myhouses = remove_duplicates(myhouses)
    print('Duplicates')
    for i in myhouses:
        del i['details']
    #remove details as not needed anymore
    #write to file
    keys = myhouses[0].keys()
    with open('..\\..\\Database\\allviablehousescsv.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(myhouses)

def currency_and_strings(houses):


    for t in houses:
        #set the price to the digits returned by the regular expression.
        t['price'] = re.findall('\d+', t['price'])
        if t['bedrooms']:
            #  set bedrooms to the digits returned by the re.
            t['bedrooms'] = re.findall('\d+', str(t['bedrooms']))
        if t['bathrooms']:
            #ste bathrooms to the digits returned by the re.
            t['bathrooms'] = re.findall('\d+', str(t['bathrooms']))
            #change them back to strings for future ease
        if t['price']:
            t['price'] = ''.join(t['price'])
        else:
            t['price'] = ''
        if t['bedrooms']:
            t['bedrooms'] = ''.join(t['bedrooms'])
        else:
            t['bedrooms'] = ''
        if t['bathrooms']:
            t['bathrooms'] = ''.join(t['bathrooms'])
        else:
            t['bathrooms'] = ''

    return houses


def removenovalues(houses):
    nothouse = []
    #if the value is null then append the full house to the new list
    for house in houses:
        if not house['price']:
            nothouse.append(house)
        elif not house['bedrooms']:
            nothouse.append(house)
        elif not house['bathrooms']:
            nothouse.append(house)
        elif house['area'] is 0:
            nothouse.append(house)
        elif not house['area']:
            nothouse.append(house)

    b = 0
    # loop the list and remove the corrosponding value from the other list
    for house in nothouse:
        b+=1
        houses.remove(house)

    return houses


def change_to_int(houses):
    for house in houses:
        house['price'] = float(house['price'])
        house['bathrooms'] = int(house['bathrooms'])
        house['bedrooms'] = int(house['bedrooms'])
        house['area'] = int(house['area'])
    #change all to int
    return houses


def remove_duplicates(houses):

    dup = False
    newhouses = []
    for house in houses:
        #loop the houses list
        for i in newhouses:
            #loop the new houses list
            if house == i:
                #if the house is already in the newhouses list set dup to True
                dup = True

        if dup is False:
            #if dup is false then there is no existing duplicate so,
            # append the house to the newhouses
            newhouses.append(house)
        dup = False

    return newhouses

def additional_columns(houses):
    for i in houses:
        # check the details for the specified substring
        #if the substring exists
        #set the key to true
        #otherwise set it as false
        if 'garage' in i['details']:
            i['Garage'] = 'Yes'
        elif 'Garage' in i['details']:
            i['Garage'] = 'Yes'
        else: i['Garage'] = 'No'

        if 'garden' in i['details']:
            i['Garden'] = 'Yes'
        elif 'Garden' in i['details']:
            i['Garden'] = 'Yes'
        else: i['Garden'] = 'No'

        if 'ensuite' in i['details']:
            i['Ensuite'] = 'Yes'
        elif 'en-suite' in i['details']:
            i['Ensuite'] = 'Yes'
        elif 'EnSuite' in i['details']:
            i['Ensuite'] = 'Yes'
        elif 'En-Suite' in i['details']:
            i['Ensuite'] = 'Yes'
        else: i['Ensuite'] = 'No'

    return houses


