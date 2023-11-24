import DataImporter
import pandas as pd
from pathlib import Path
import random
import csv

def split_data(houses,htype,areas):
    lenght = len(houses)
    twenty = []
    eighty = lenght*.8
    # pop twenty percent into a new file
    while lenght > eighty:
        twenty.append(houses.pop(random.randint(0, lenght-1)))
        lenght -= 1

    print(len(houses))
    print(len(twenty))
    #save to a new file
    keys = twenty[0].keys()
    with open('..\\..\\Q_Learning_CSVs\\'+str(areas)+str(htype)+'Twenty.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(twenty)

    return houses

def create_segment(htype):
    housesegment = {}
    housesegment['positions']={}
    # create a total segment of bedrooms bathrooms and area inside of the Location
    # It is already a specific type
    for i in range(1, 11):
        for x in range(1, 11):
            for y in range(1,11):
                ###################################################################
                pos = 'bd' + str(i) + 'br' + str(x) + 'area' + str(y)
                housesegment['positions'][pos] = {}
                housesegment['positions'][pos]['houses'] = []
                housesegment['positions'][pos]['bedrooms'] = i
                housesegment['positions'][pos]['bathrooms'] = x
                housesegment['positions'][pos]['area'] = y
    housesegment['type'] = htype

    return housesegment

def segment_thedata(all_houses,htype,area):
    housesegment = create_segment(htype)
    for i in range(1,11):
        for x in range(1,11):
            for y in range(1,11):
                ###################################################################
                pos = 'bd'+str(i)+'br'+str(x)+'area'+str(y)
                for house in all_houses:
                    if int(house['bedrooms']) == i:
                        if int(house['bathrooms']) ==x:
                            if int(house['label'])==y:
                                housesegment['positions'][pos]['houses'].append(house['price'])
                                housesegment['positions'][pos]['area'] = area
                                housesegment['positions'][pos]['type']=htype
                                # aassign correct data for future use and append relevant properties

    count = 0
    for i in range(1, 11):
        for x in range(1, 11):
            for y in range(1, 11):
                ###################################################################
                pos = 'bd' + str(i) + 'br' + str(x) + 'area' + str(y)
                if len(housesegment['positions'][pos]['houses']) < 1:
                    del(housesegment['positions'][pos])
                    # over 20,000 combos
                    # deletes any without instances.
                    # could be a vast amount

    return housesegment

def import_then_segment():
    type_list1 = ['Terraced_House', 'Apartment_For_Sale', 'Bungalow'
                                                          'Duplex', 'End_of_T', 'House_For_Sale', 'New_Dwelling',
                  'Second-Hand',
                  'Site', 'Terraced'  'Townhouse', 'Detatched_House', 'Semi-Detached']
    type_list2 = [ 'Semi-Detached']
    all_segments =[]

    for t in type_list1:
        my_file = Path('..\\..\\Database\\CorkCity' + str(t) + 'Complete.csv')
        if my_file.is_file():
            houses = DataImporter.import_Cork(t)
            houses = split_data(houses, t,'CorkCity')
            all_segments.append(segment_thedata(houses, t, 'CorkCity'))

    for t in type_list1:
        my_file = Path('..\\..\\Database\\Dublin15' + str(t) + 'Complete.csv')
        if my_file.is_file():
            houses = DataImporter.import_Dublin(t)
            houses = split_data(houses,t,'Dublin15')
            all_segments.append(segment_thedata(houses, t,'Dublin15'))

    return all_segments

#dublin_houses = DataImporter.splitHouses(dublin_houses)
