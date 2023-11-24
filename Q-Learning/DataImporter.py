import csv



def splitHouses(all_houses):
    DetHouse = []
    SemDetHouse = []
    TerrHouse = []
    AppSale = []
    Bungalow = []
    DuplexSale = []
    EndTHouse = []
    NewDHA = []
    SHDHA = []
    SiteSale = []
    Townhouse = []
    HouseSale = []
    OtherType = []
    for house in all_houses:

        if 'Detatched House' in house['type']:
            DetHouse.append(house)
        elif 'Semi-detatched House' in house['type']:
            SemDetHouse.append(house)
        elif 'Terraced House' in house['type']:
            TerrHouse.append(house)
        elif 'Apartment For Sale' in house['type']:
            AppSale.append(house)
        elif 'Bungalow' in house['type']:
            Bungalow.append(house)
        elif 'Semi-Detached' in house['type']:
            SemDetHouse.append(house)
        elif 'Detached' in house['type']:
            DetHouse.append(house)
        elif 'Duplex' in house['type']:
            DuplexSale.append(house)
        elif 'End of' in house['type']:
            EndTHouse.append(house)
        elif 'House For Sale' in house['type']:
            HouseSale.append(house)
        elif 'New Dwelling' in house['type']:
            NewDHA.append(house)
        elif 'Second-Hand' in house['type']:
            SHDHA.append(house)
        elif 'Site' in house['type']:
            SiteSale.append(house)
        elif 'Terraced' in house['type']:
            TerrHouse.append(house)
        elif 'Townhouse' in house['type']:
            Townhouse.append(house)
        else:
            OtherType.append(house)
    Houses = {}
    Houses['DetHouse'] = []
    Houses['DetHouse'].append(DetHouse)
    Houses['DetHouse'].append('DetachedHouse')
    Houses['SemDetHouse']= []
    Houses['SemDetHouse'].append(SemDetHouse)
    Houses['SemDetHouse'].append('SemiDetachedHouse')
    Houses['TerrHouse']=[]
    Houses['TerrHouse'].append(TerrHouse)
    Houses['TerrHouse'].append('TerracedHouse')
    Houses['AppSale'] = []
    Houses['AppSale'].append(AppSale)
    Houses['AppSale'].append('Apartment')
    Houses['Bungalow'] = []
    Houses['Bungalow'].append(Bungalow)
    Houses['Bungalow'].append('Bungalow')
    Houses['Duplex'] = []
    Houses['Duplex'].append(DuplexSale)
    Houses['Duplex'].append('Duplex')
    Houses['EndTHouse'] = []
    Houses['EndTHouse'].append(EndTHouse)
    Houses['EndTHouse'].append('EndOfTerraceHouse')
    Houses['NewDHA'] = []
    Houses['NewDHA'].append(NewDHA)
    Houses['NewDHA'].append('NewDHA')
    Houses['SHDHA'] = []
    Houses['SHDHA'].append(SHDHA)
    Houses['SHDHA'].append('SHDHA')
    Houses['Site'] = []
    Houses['Site'].append(SiteSale)
    Houses['Site'].append('Site')
    Houses['TownHouse'] = []
    Houses['TownHouse'].append(Townhouse)
    Houses['TownHouse'].append('TownHouse')
    Houses['House'] = []
    Houses['House'].append(HouseSale)
    Houses['House'].append('House')
    return Houses


def import_Dublin(htype):
    with open('..\\..\\Database\\Dublin15'+str(htype)+'Complete.csv') as csv_file:
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
    return new_houses


def import_Cork(htype):
    with open('..\\..\\Database\\CorkCity' + str(htype) + 'Complete.csv') as csv_file:
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
                'label': ''

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
    new_houses = []

    for house in all_houses:
        if house['label']:
            new_houses.append(house)
    return new_houses