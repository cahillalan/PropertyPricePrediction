import  csv
import re
from operator import itemgetter


def import_predictions():
    with open('..\\..\\..\\Q_Learning_CSVs\\Predictions.csv') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        x=0
        my_list=[]
        for i in readCSV:
            if i and x > 0:
                my_dict = {
                    'Position':'',
                    'Area':'',
                    'Type':'',
                    'Counter':''
                }

                my_dict['Position']=i[0]
                my_dict['Area']=i[1]
                my_dict['Type']=i[2]
                my_dict['Counter']=i[3]

                my_list.append(my_dict)
            x+=1


    for j in my_list:
        j['Counter'] =j['Counter'].replace(' ','').split(',')
        count_list=[]
        for i in range(len(j['Counter'])):
            test = True
            count_dict = {}
            count_dict['value'] = re.findall(r"'(.*?)'", j['Counter'][i])

            count_dict['probability'] = re.findall(r':(\d+)', j['Counter'][i])
            if count_dict['probability']:
                count_dict['probability'] = int(count_dict['probability'][0])/2
                count_list.append(count_dict)


        j['Counter']=sorted(count_list, key=itemgetter('probability'), reverse=True)


    return my_list



