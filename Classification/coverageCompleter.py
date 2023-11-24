import csv
import section_splitting_runprogram
import math
from pathlib import Path


def import_points(htype,area):
    with open('..\\..\\Database\\'+str(area) + str(htype) + 'CentrePoints.csv') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        ## import points using the htype as a reference
        a = 0
        all_points = []
        for i in readCSV:
            hinfo = {
                'point': '',
                'label': ''
            }
            if i and a > 0:

                hinfo['point'] = i[0]
                hinfo['label'] = i[1]

                all_points.append(hinfo)
            a += 1
    return all_points

def import_houses(htype,area):
    with open('..\\..\\Database\\'+str(area)+str(htype)+'Complete.csv') as csv_file:
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
                'label':'',
                'Latitude':'',
                'Longitude':''

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
                hinfo['Latitude'] = i[13]
                hinfo['Longitude'] = i[14]

                all_houses.append(hinfo)
            a += 1
    return all_houses

def distance_calculator(centre,point):

    centre['point'] = str(centre['point']).split(",")
    centre['point'][0] = float(centre['point'][0].strip("["))
    centre['point'][1] = float(centre['point'][1].strip("]"))
    # set the centre points lat and long

    x = float(centre['point'][0])
    y = float(centre['point'][1])

    print(point)
    point['LatLng'] = str(point['LatLng']).split(",")
    point['LatLng'][0] = float(point['LatLng'][0].strip("["))
    point['LatLng'][1] = float(point['LatLng'][1].strip("]"))
    # set the points lat and long
    x2 = float(point['LatLng'][0])
    y2 = float(point['LatLng'][1])
    # use the formula srt((x1-x2)^2+(y1-y2)^2) to calculate the distance between the points
    mx = ((x2) - (x))
    my = ((y2) - (y))
    add = ((mx) + (my))
    sq = ((add) * (add))
    distance = math.sqrt(sq)

    return distance



def finish_coverage(htype,area):

    points = import_points(htype,area)
    houses = import_houses(htype,area)

    distance_dict={}
    # import the relevant data


    for house in houses:
        for p in points:
            distance_dict[str(p['label'])] = 100
            # assign the distance as 100 as a default
        if house['label'] == '':
            for p in points:
                # calculate the distance of the point from the centre
                distance_dict[str(p['label'])]=distance_calculator(p,house)
        lowest = distance_dict['1']
        newlabel = '1'

        for p in points:
            new = distance_dict[str(p['label'])]
            #iterate the list and if a distance is lower than the assigned it becomes the new lowest.
            # set the new label
            if new < lowest:
                lowest = new
                newlabel = str(p['label'])
        #whatever the lowest is should be the newlabel
        house['label'] = newlabel


