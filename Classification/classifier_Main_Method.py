import csv
import compassSplitter
import sectionStepper
import section_splitting_runprogram
import re
import point_setter
from datetime import datetime
import coverageCompleter
from pathlib import Path

def open_CorkCity():

#opens cork city and converts to a dictionary
    with open('..\\..\\Database\\CorkCityHousesComplete.csv') as csv_file:
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
                'Garage' : '',
                'Garden' : '',
                'Ensuite': '',
                'LatLng' : '',
                'DateOfSale':'',
                'SalePrice' :''

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
    return all_houses

def open_Dublin15():


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
                'Garage' : '',
                'Garden' : '',
                'Ensuite': '',
                'LatLng' : '',
                'DateOfSale':'',
                'SalePrice' :''

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
    return all_houses

def split_houseType(all_houses,htype):
    myusablehouses = []
    # if the house type matches the passed htype it is appended
    for house in all_houses:
        if str(htype) in str(house['type']):
            myusablehouses.append(house)
    return myusablehouses

def split_Type_detached(all_houses,htype1,htype2):
    myusablehouses = []
    # splits detached as there are two spellings of detached/detatched
    # if either is in the address they are appended
    for house in all_houses:
        if str(htype1) in str(house['type']) or str(htype2) in str(house['type']):
            myusablehouses.append(house)
    return myusablehouses

def dublin_outliers(newhouses):
    cleanhouses = []
    for house in newhouses:
    # make sure the data is in dublin 15 by removing points outside a general area
    # not very specific as borders can be inconsistent
    # a property with dublin 15 in the address but a lat lng in dub4 for eg will cause major issues
    # a property directly next to dub 15 will cause no issues
        if house['LatLng'][0] < 53.45 and house['LatLng'][0] > 53.35:
            if house['LatLng'][1] > -6.5 and house['LatLng'][1] < -6.3:
                if float(house['price']) < float(5000000) and float(house['price']) > float(90000):
                    cleanhouses.append(house)
    return cleanhouses

def cork_outliers(newhouses):
    # same with cork addresses
    cleanhouses = []
    for house in newhouses:
        if house['LatLng'][0] < 52 and house['LatLng'][0] > 51.7:
            if house['LatLng'][1] > -8.6 and house['LatLng'][1] < -8.4:
                if float(house['price']) < float(5000000) and float(house['price']) > float(90000):
                    cleanhouses.append(house)
    return cleanhouses


def run_classifier(myusablehouses,htype,mainArea):
    price = 100000
    newhouses = []
    for i in myusablehouses:
        i['label'] = ''
        if i['LatLng']:
            # this converts the string of latlng to a list of latlng
            i['LatLng'] = str(i['LatLng']).split(",")
            i['LatLng'][0] = float(i['LatLng'][0].strip("["))
            i['LatLng'][1] = float(i['LatLng'][1].strip("]"))
            newhouses.append(i)
    if 'Dublin'in mainArea:
        cleanhouses = dublin_outliers(newhouses)
    else:
        cleanhouses= cork_outliers(newhouses)
    #removes outliers
    length = len(cleanhouses)
    #sets the length for future use
    mydict = {}
    if length > 9:
    # if length is less than 10 the algorithm will not be able to classiffy the houses so it is rejected
    # point setter is called and variable initialised to the return values
        borders , mynewhouses, gate,area,points = point_setter.number_of_areas(cleanhouses,price,length)
    # if the algorithm was able to classify the houses then borders will not be 0
        if len(borders) > 0:
            counts = {}
            labels = ['1','2','3','4','5','6','7']
            for l in labels:
                counts[l] = 0
            for house in mynewhouses:
                # adds lat and long full values for graphing
                house['Lattitude'] = house['LatLng'][0]
                house['Longitude'] = house['LatLng'][1]
                for l in labels:
                    if house['label'] ==l:
                        counts[l] +=1
                # count the lables for future use

            # set type and area for future use
            # write to the files
            mydict['type'] = htype
            mydict['area'] = area
            keys = myusablehouses[0].keys()
            with open('..\\..\\Database\\'+str(mainArea)+str(htype)+'Complete.csv', 'w+') as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(myusablehouses)
            keys = borders[0].keys()
            with open('..\\..\\Database\\'+str(mainArea)+str(htype)+'BorderPoints.csv', 'w+') as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(borders)
            print(points)
            keys = points[0].keys()
            with open('..\\..\\Database\\'+str(mainArea) + str(htype) + 'CentrePoints.csv', 'w+') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(points)

    return mydict



st = datetime.now()
#################################
#RUN OFF EACH HOUSE TYPE HERE
type_list =[ 'Terraced House', 'Apartment For Sale','Bungalow' 
             'Duplex' , 'End of T' , 'House For Sale' ,'New Dwelling' , 'Second-Hand'  ,
            'Site' , 'Terraced'  'Townhouse' ]

# for cork run through the type list and segregate each house type and attempt to classify the houses within
# semi-detached and detached are run seperatley to other due to spelling duplicates
area_list=[]
all_houses = open_CorkCity()
for t in type_list:
    myusablehouses = split_houseType(all_houses,t)
    if len(myusablehouses) > 10:
        print(t)
        area_list.append(run_classifier(myusablehouses,t.replace(' ','_'),'CorkCity'))

myusablehouses = split_Type_detached(all_houses,'Semi-detatched House','Semi-Detached')
if len(myusablehouses) > 10:
    area_list.append(run_classifier(myusablehouses,'Semi-Detached','CorkCity'))

myusablehouses = split_Type_detached(all_houses,'Detached','Detatched House')
if len(myusablehouses) > 10:
    area_list.append(run_classifier(myusablehouses,'Detatched_House','CorkCity'))

keys = area_list[0].keys()
with open('..\\..\\Q_Learning_CSVs\\CorkCityAreaNumbers.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(area_list)


type_list2 =[ 'Terraced_House', 'Apartment_For_Sale','Bungalow' 
             'Duplex' , 'End_of_T' , 'House_For_Sale' ,'New_Dwelling' , 'Second-Hand'  ,
            'Site' , 'Terraced'  'Townhouse','Semi-Detached' ,'Detatched_House']

# finish the coverage of any file that exists
for t in type_list2:
    my_file = Path('..\\..\\Database\\CorkCity'+str(t)+'Complete.csv')
    if my_file.is_file():
        coverageCompleter.finish_coverage(t, 'CorkCity')


# REPEAT FOR DUBLIN
##################################################
area_list=[]
all_houses = open_Dublin15()
for t in type_list:
    myusablehouses = split_houseType(all_houses,t)
    if len(myusablehouses) > 10:
        area_list.append(run_classifier(myusablehouses,t.replace(' ','_'),'Dublin15'))

myusablehouses = split_Type_detached(all_houses,'Semi-detatched House','Semi-Detached')
if len(myusablehouses) > 10:
    area_list.append(run_classifier(myusablehouses,'Semi-Detached','Dublin15'))

myusablehouses = split_Type_detached(all_houses,'Detached','Detatched House')
if len(myusablehouses) > 10:
    area_list.append(run_classifier(myusablehouses,'Detatched_House','Dublin15'))

keys = area_list[0].keys()
with open('..\\..\\Q_Learning_CSVs\\Dublin15AreaNumbers.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(area_list)


type_list2 =[ 'Terraced_House', 'Apartment_For_Sale','Bungalow' 
             'Duplex' , 'End_of_T' , 'House_For_Sale' ,'New_Dwelling' , 'Second-Hand'  ,
            'Site' , 'Terraced'  'Townhouse','Semi-Detached' ,'Detatched_House']

for t in type_list2:
    my_file = Path('..\\..\\Database\\Dublin15'+str(t)+'Complete.csv')
    if my_file.is_file():
        coverageCompleter.finish_coverage(t,'Dublin15')

print(datetime.now() - st)