import Import_twenties
import Import_predictions
from pathlib import Path
import csv

def import_andrun():

    type_list1 = ['Terraced_House', 'Apartment_For_Sale', 'Bungalow'
                                                          'Duplex', 'End_of_T', 'House_For_Sale', 'New_Dwelling',
                  'Second-Hand',
                  'Site', 'Terraced'  'Townhouse', 'Detatched_House', 'Semi-Detached']
    type_list2 = ['Semi-Detached']

    all_Houses = {}
    for t in type_list1:
        my_file = Path('..\\..\\..\\Q_Learning_CSVs\\Dublin15'+str(t)+'Tewnty.csv')
        if my_file.is_file():
            all_Houses[str(t)]=Import_twenties.import_Dublin(t)




    return all_Houses



def predict_values():

    allHouses = import_andrun()
    predictions = Import_predictions.import_predictions()

    for h in allHouses:
        for house in allHouses[str(h)]:
            house['prediction']= ''
            for p in predictions:
                if str(p['Type'][0:2]) == str(house['type'][0:2]):

                    if str(p['Position'])== str(house['pos']):
                        if p['Counter']:
                            house['prediction'] = p['Counter'][0]['value']

    newhouses = []
    for h in allHouses:
        print(h)
        for house in allHouses[str(h)]:
            print(house['price'])
            print(house['prediction'])
            newhouses.append(house)
    
        
        
    return allHouses

