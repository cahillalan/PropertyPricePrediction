import DataSegmentation
import actor
from datetime import datetime
import collections
import csv


start = datetime.now()
x = 0
all_segments = DataSegmentation.import_then_segment()
env_list =[]
# create segments and append to a full environment list
# save extra params for future testing
for s in all_segments:
    for p in s['positions']:
        exit_points = []
        my_dict ={}

        for price in s['positions'][p]['houses']:
            exit_points.append(float(price))

        print('before')
        my_dict['pos'] = p
        my_dict['area'] = s['positions'][p]['area']
        my_dict['type'] = s['positions'][p]['type']
        # enter the environment for each env
        my_dict['env'] = actor.enter_environment(exit_points)
        env_list.append(my_dict)
        x+=1
mycounter = []

print('Predicting')
for e in env_list:
    print(1)
    my_dict={}
    counter ={}
    predictions =[]
    position = 100000
    position2 = 195000
    for lp in range(99):
    # Make predictios and add the necessary values to a list opf dicts
    # for writing to a file.
        predictions.append(actor.get_predictions(e['env'], position))
        predictions.append(actor.get_predictions(e['env'], position2))
        position += 100000
        position2 += 100000
    my_dict['pos'] = e['pos']
    my_dict['area'] = e['area']
    my_dict['type'] = e['type']
    for p in predictions:
        counter[str(p)]=0
    counter[str(0)]=0
    for p in predictions:
        counter[str(p)]+=1
    del counter[str(0)]
    my_dict['counter'] = str(counter)
    mycounter.append(my_dict)

keys = mycounter[0].keys()
with open('..\\..\\Q_Learning_CSVs\\Predictions.csv', 'w+') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(mycounter)
print(mycounter)
end = datetime.now()-start
print(end)