import csv

with open('C:\\Users\\Cahil\\Desktop\\Database\\Dublin15HousesComplete.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    a = 0
    all_houses = []
    for i in readCSV:
        hinfo = {
            'price': '',
            'address': '',
            'bedrooms': '',
            'bathrooms': '',
            'type': '',
            'views': '',
            'area': '',
            'Garage': '',
            'Garden': '',
            'Ensuite': '',
            'LatLng': '',
            'dateofsale': ''

        }
        if i and a > 0:
            hinfo['price'] = i[0]
            hinfo['address'] = i[1]
            hinfo['bedrooms'] = i[2]
            hinfo['bathrooms'] = i[3]
            hinfo['type'] = i[4]
            hinfo['area'] = i[6]
            hinfo['Garage'] = i[7]
            hinfo['Garden'] = i[8]
            hinfo['Ensuite'] = i[9]
            hinfo['LatLng'] = i[10]
            hinfo['dateofsale'] = i[11]

            all_houses.append(hinfo)
        a += 1
        myusablehouses = []
    for house in all_houses:
        if 'Semi-Detached House' in str(house['type']):
            if house['dateofsale']:
                myusablehouses.append(house)

print(len(myusablehouses))

