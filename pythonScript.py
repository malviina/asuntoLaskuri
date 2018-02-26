import csv
import pandas as pd
import json

kunnat = []
neliot = []
vuokrat = []
aineisto = []
yhtalot =[]

csv.register_dialect('csv', delimiter=';')

input_file = open('data-riisuttu.csv', 'rb')

headerline=input_file.readline()
# Data muodossa postinro; kunta; vuokra; koko;

try:
    reader = csv.reader(input_file, dialect='csv')
    for row in reader:

        kunta = row[1]

        if kunta in kunnat:
            i = kunnat.index(kunta)
        else:
            kunnat.append(kunta)
            i = kunnat.index(kunta)
            neliot.append([])
            vuokrat.append([])
            aineisto.append([])
        

        vuokra = float(row[2])
        koko = float(row[3])
        
        aineisto[i].append([vuokra, koko])


finally:
    input_file.close()

input_file2 = open('yhtalot.csv', 'rb')
try:
    reader = csv.reader(input_file2, dialect='csv')
    for row in reader:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
        yhtalot.append([a, b, c])
finally:
    input_file2.close()
    
data = []


for j in kunnat:
    k = kunnat.index(j)
    
    data.append({"paikka": j, "kerroin": yhtalot[k], "data": aineisto[k]})


tiedosto = open("data.json", "wb")
json.dump(data, tiedosto, indent = 2)
tiedosto.close()
