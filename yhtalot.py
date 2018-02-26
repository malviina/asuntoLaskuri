# -*- coding: UTF-8 -*-

import csv
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt



kunnat = []
neliot = []
vuokrat = []
yhtalot = []

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
        

        vuokra = float(row[2])
        koko = float(row[3])
               
        if vuokra < 5000 and koko < 250:
            vuokrat[i].append(vuokra)
            neliot[i].append(koko)


finally:
    input_file.close()
#print kunnat


for kunta in kunnat:
    k = kunnat.index(kunta)
    
    X = neliot[k]
    Y = vuokrat[k]
    
    polynomi = np.polyfit(X, Y, 2)
    yhtalot.append([polynomi[0], polynomi[1], polynomi[2]])


output_file = open('yhtalot.csv', 'wb')
writer = csv.writer(output_file, dialect="csv")
writer.writerows(yhtalot)
output_file.close()


#tiedosto = open("tiedosto.json", "wb")
#json.dump(kunnat, tiedosto, indent = 4)
#tiedosto.close()

#c = kunnat.index("Vantaa")
#X = neliot[c]
#Y = vuokrat[c]

#kertoimet = np.polyfit(X, Y, 2)
#print kertoimet
#plt.plot(X, Y, 'o', label='raakadata')

#polynomi = np.poly1d(kertoimet)
#pol_X = np.linspace(0, 700, 20)
#pol_Y = polynomi(pol_X)

#plt.plot(pol_X, pol_Y, color='red', label='sovitus 1. aste')

#plt.show()