import csv

def import_Dublin(htype):
    with open('..\\..\\..\\Q_Learning_CSVs\\Dublin15'+str(htype)+'Tewnty.csv') as csv_file:
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
                'SalePrice': '',
                'label' : ''

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
                hinfo['label'] = i[12]

                all_houses.append(hinfo)
            a += 1
    new_houses=[]


    for house in all_houses:
        if house['label']:
            new_houses.append(house)

    new_houses=add_pos(new_houses)
    return new_houses



def add_pos(houses):

    for i in range(1,11):
        for x in range(1,11):
            for y in range(1,11):
                for house in houses:
                    if int(house['bedrooms']) == i:
                        if int(house['bathrooms']) == x:
                            if int(house['label']) == y:
                                house['pos']= 'bd' + str(i) + 'br' + str(x) + 'area' + str(y)

    return houses