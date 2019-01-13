import geopandas as gpd
import os
import numpy
import geojson
from geojson import Feature, FeatureCollection, LineString

data_pth = "D:\Работа\ВШЭ\TumenFinal"
file_name = "test.shp"
s = gpd.read_file(os.path.join(data_pth, file_name),encoding = 'utf-8')

print (type(s))

d = {}

l = []
name = []
data = []

n = len(s['geometry'])

#print (s.head())

for i in range(n):
    geom = s['geometry'][i]
    l = []
    name = []
    for j in range(n):
        if geom == s['geometry'][j]:
            #print (s['LINENAME'][j])
            l.append(s['OBJECTID'][j])
            name.append(s['LINENAME'][j])
       # else:
            #continue
    d[i] = [l,name]

spisok = []
for f in range(len(d)):
    spisok.append(d[f])
unique_numbers = []
for n in spisok:
    if n not in unique_numbers:
        unique_numbers.append(n)
#print(unique_numbers)

for r in range(len(unique_numbers)):
    f = set(unique_numbers[r][1])
    del unique_numbers[r][1]
    unique_numbers[r].append(list(f))

dic = {}

for n in range(len(unique_numbers)):
    dic[n]=unique_numbers[n]
    
print(dic)


features = []
for el in range(len(dic)):
    proper = {}
    ident = int(s.loc[s['OBJECTID'] == dic[el][0][0]]['ID'])
    geom = s.loc[s['OBJECTID'] == dic[el][0][0]]['geometry']
    for g in range(len(dic[el][1])):
        proper['route'+str(g)] = dic[el][1][g]
    proper['count'] = len(dic[el][1])
    print(proper)
    features.append(Feature(geometry = LineString(geom[ident].coords), properties = proper))

collection = FeatureCollection(features)
with open('D:/Работа/ВШЭ/TumenFinal/result.geojson', "w") as geoj:
    geoj.write('%s' % collection)