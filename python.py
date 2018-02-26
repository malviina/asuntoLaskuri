# -*- coding: utf-8 -*-
import csv
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

kunnat = []
neliot = []
vuokrat = []
aineisto = []
yhtalot =[]
maakunnat = []


csv.register_dialect('csv', delimiter=';')

input_file = open('maakunnat.csv', 'rb')
try:
    reader = csv.reader(input_file, dialect='csv')
    for row in reader:
        yksiKunta = []
        l = 1
        n = len(row)
        while l < n:
            yksiKunta.append(row[l])
            l += 1
        kokorivi = [row[0], yksiKunta]
        maakunnat.append(kokorivi)
        
        
        
finally:
    input_file.close()


input_file2 = open('data-riisuttu.csv', 'rb')
headerline=input_file2.readline()
# Data muodossa postinro; kunta; vuokra; koko;
try:
    reader = csv.reader(input_file2, dialect='csv')
    for row in reader:

        kunta = row[1]

        if kunta in kunnat:
            i = kunnat.index(kunta)
        else:
            kunnat.append(kunta)
            i = kunnat.index(kunta)
            aineisto.append([])
        

        vuokra = float(row[2])
        koko = float(row[3])
        
        aineisto[i].append([vuokra, koko])

finally:
    input_file2.close()

# Tallennetaan kunnat, joissa riittävästi datapisteitä
isotKaupungitNimet = []
isotKaupungitAineisto = []

for kunta in kunnat:
    n = kunnat.index(kunta)
    
    if len(aineisto[n]) > 20:
        isotKaupungitNimet.append(kunta)
        isotKaupungitAineisto.append([])
        m = isotKaupungitNimet.index(kunta)
        for datapiste in aineisto[n]:
            vuokra = float(datapiste[0])
            koko = float(datapiste[1])
            isotKaupungitAineisto[m].append([vuokra, koko])

kaupunkiAineisto = []
for kaupunki in isotKaupungitNimet:
    p = isotKaupungitNimet.index(kaupunki)
    kaupunkiAineisto.append([kaupunki, isotKaupungitAineisto[p]])
# Muutetaan aineiston kunnat maakunniksi

for kunta in kunnat:
    m = kunnat.index(kunta)
    for maakunta in maakunnat:
        if kunta in maakunta[1]:
            kunnat[m] = maakunta[0]
            break;
#for rivi in maakunnat:
#    print rivi[0]

# Yhdistetään maakuntadata
uudetKunnat = []
uusiAineisto = []
testi = ""
for maakunta in kunnat:
    testi = aineisto[m]
    m = kunnat.index(maakunta)
    datapiste = aineisto[m]
    if maakunta in uudetKunnat:
        n = uudetKunnat.index(maakunta)
    else:
        uudetKunnat.append(maakunta)
        n = uudetKunnat.index(maakunta)
        uusiAineisto.append([])
    
    for datapiste in aineisto[m]:
        vuokra = float(datapiste[0])
        koko = (datapiste[1])
        

        uusiAineisto[n].append([vuokra, koko])


maakuntaAineisto = []
for kunta in uudetKunnat:
    o = uudetKunnat.index(kunta)
    maakuntaAineisto.append([kunta, uusiAineisto[o]])


# Yhdistetään kaikki lopulliseksi aineistoksi
lopullinenAineisto = []
for rivi in kaupunkiAineisto:
    lopullinenAineisto.append(rivi)

for rivi in maakuntaAineisto:
    lopullinenAineisto.append(rivi)
    
# Sovitetaan polynomifunktiot
yhtalot = []
dataAineisto = []
for row in lopullinenAineisto:
    neliot = []
    vuokrat = []
    data = row[1]
       
    for datapiste in data:
            
        vuokrat.append(datapiste[0])
        neliot.append(datapiste[1])
            
    
        X = neliot
        Y = vuokrat
    
        polynomi = np.polyfit(X, Y, 2)
        yhtalot.append([polynomi[0], polynomi[1], polynomi[2]])

for rivi in lopullinenAineisto:
    r = lopullinenAineisto.index(rivi)
    paikka = rivi[0]
    aineisto = rivi[1]
    
    data.append({"paikka": paikka, "kerroin": yhtalot[r], "data": aineisto})


tiedosto = open("data.json", "wb")
json.dump(data2, tiedosto, indent = 2)
tiedosto.close()
