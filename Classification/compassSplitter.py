
def splitter(property_list,point) :
    north =[]
    south =[]
    east = []
    west = []
    neast = []
    nwest = []
    swest = []
    seast = []
    thecentre = []
    for prop in property_list:
        prop['Compass'] = ''



    for p in property_list:
        try:

            if p['LatLng'][0] > point[0] and p['LatLng'][1] == point[1]:
                p['Compass'] = 'North'
                north.append(p)
                #print(len(north))
            elif p['LatLng'][0] < point[0] and p['LatLng'][1] == point[1]:
                p['Compass'] = 'South'
                south.append(p)
            elif p['LatLng'][0] == point[0] and p['LatLng'][1] > point[1]:
                p['Compass'] = 'East'
                east.append(p)
            elif p['LatLng'][0] == point[0] and p['LatLng'][1] < point[1]:
                p['Compass'] = 'West'
                west.append(p)
            elif p['LatLng'][0] > point[0] and p['LatLng'][1] > point[1]:

                p['Compass'] = 'NorthEast'
                neast.append(p)
            elif p['LatLng'][0] < point[0] and p['LatLng'][1] > point[1]:
                p['Compass'] = 'SouthEast'
                seast.append(p)
            elif p['LatLng'][0] > point[0] and p['LatLng'][1] < point[1]:
                p['Compass'] = 'NorthWest'
                nwest.append(p)
            elif p['LatLng'][0] < point[0] and p['LatLng'][1] < point[1]:
                p['Compass'] = 'SouthWest'
                swest.append(p)
            else:
                p['Compass'] ='Unknown'
                thecentre.append(p)
        except:
            print(property_list)



    return neast,nwest,seast,swest,north,south,east,west,thecentre



