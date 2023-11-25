import make_predictions
import math
import csv

allHouses = make_predictions.predict_values()

figure_list = []
for h in allHouses:
    print(h)
    for house in allHouses[str(h)]:
        mydict={}
        mydict['price'] = float(house['price'])/10000
        mydict['prediction' ]=house['prediction']
        if mydict['prediction']:
            figure_list.append(mydict)
sigmax = 0
sigmay = 0
sigmaxy=0
sigmax2=0
sigmay2=0
keys = figure_list[0].keys()
print(keys)
with open('..\\..\\..\\Q_Learning_CSVs\\testinPredictions.csv', 'w+') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(figure_list)

for fig in figure_list:

    fig['prediction'] = float(fig['prediction'][0])/10000
    print(fig)
    fig['pricesq']= float(fig['price']) * float(fig['price'])
    fig['predictsq']=float(fig['prediction']) * float(fig['prediction'])
    fig['xy']=float(fig['price']) * float(fig['prediction'])
    sigmax += float(fig['price'])
    sigmay += float(fig['prediction'])
    sigmaxy += float(fig['xy'])
    sigmax2 += float(fig['pricesq'])
    sigmay2 += float(fig['predictsq'])

print(sigmax)
print(sigmay)
print(sigmaxy)
print(sigmax2)
print(sigmay2)




n = len(figure_list)

print(n)

topl = sigmaxy * n
topr = sigmax * sigmay
top = topl - topr
bottomleftl = n * sigmax2
bottomleftr = sigmax * sigmax
bottomleft = bottomleftl - bottomleftr
bottomrightl = n * sigmay2
bottomrightr = sigmay * sigmay
bottomright = bottomrightl - bottomrightr
bottomcentre = bottomleft * bottomright

bottom = math.sqrt(bottomcentre)

total = top/bottomcentre

print('Accuracy is')
print(total)
