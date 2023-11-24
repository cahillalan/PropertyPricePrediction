import csv

with open('..\\..\\Database\\Dublin15HousesComplete.csv') as csv_file:
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
            'area': '',
            'Garage': '',
            'Garden': '',
            'Ensuite': '',
            'LatLng': '',
            'DateOfSale': '',
            'SalePrice': ''

        }
        if i and a > 0:
            hinfo['price'] = i[0]
            hinfo['address'] = i[1]
            hinfo['bedrooms'] = i[2]
            hinfo['bathrooms'] = i[3]
            hinfo['type'] = i[4]
            hinfo['area'] = i[5]
            hinfo['Garage'] = i[6]
            hinfo['Garden'] = i[7]
            hinfo['Ensuite'] = i[8]
            hinfo['LatLng'] = i[9]
            hinfo['DateOfSale'] = i[10]
            hinfo['SalePrice'] = i[11]

            all_houses.append(hinfo)
        a += 1


