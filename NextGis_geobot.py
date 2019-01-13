#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import xlwt
import datetime
rb = xlrd.open_workbook('D:/NextGIS/request.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)
val = sheet.row_values(0)
#print(val)
vals = [sheet.row_values(rownum) for rownum in range(1,sheet.nrows)]
#print(vals)
l = sheet.row_values(0)
#print(l)
dic1 = {0:0}
dic2 = {0:0}
d1 = 'vid'
a = []
b = []
c = []
e = []
z = []
vidy = []
zones = []
for i in range(len(l)):
    if d1 in l[i]:
        a.append(i)
        g = l[i].replace('vid','')
        w = g.replace('_','')
        b.append(w)
        dic1[i] = int(w)
d0 = 'data'
for i in range(len(l)):
    if d0 in l[i]:
        d01 = i
d2 = 'number_zone'
for i in range(len(l)):
    if d2 in l[i]:
        d3 = i
d4 = 'lake'
for i in range(len(l)):
    if d4 in l[i]:
        d5 = i
d6 = 'Lat'
for i in range(len(l)):
    if d6 in l[i]:
        d7 = i
d8 = 'long'
for i in range(len(l)):
    if d8 in l[i]:
        d9 = i
d10 = 'soobshestvo'
for i in range(len(l)):
    if d10 in l[i]:
        d11 = i
d12 = 'dlina_zone'
for i in range(len(l)):
    if d12 in l[i]:
        d13 = i
d14 = 'OPP'
for i in range(len(l)):
    if d14 in l[i]:
        d15 = i
d16 = 'vetosh'
for i in range(len(l)):
    if d16 in l[i]:
        d17 = i
d18 = 'zelen'
for i in range(len(l)):
    if d18 in l[i]:
        d19 = i
d20 = 'visota'
for i in range(len(l)):
    if d20 in l[i]:
        d21 = i
for i in range(len(l)):
    for j in b:
        
        try:
            s = 'PP' + j
            if s == l[i]:
                dic2[int(j)] = i
                
        except:
            s = 'PP_' + j
            if s == l[i]:
                dic2[int(j)] = i
        #p = 'PP'+ w
        #b.append(p)
        #if p in l[i]:
           # pp = sheet.row_values(rownum)[i]
           # b.append(i)
            #print(pp)
            #dic[value] = [rownum, pp]
del dic1[0]
del dic2[0]
#print(a)
#print(b)
#print(dic1)
#print(dic2)

for i in a:
    for rownum in range(1,sheet.nrows):
        value = sheet.row_values(rownum)[i]
        value_zone = sheet.row_values(rownum)[d3]
        zones.append(int(value_zone))
        vidy.append(value)
        h = dic1[i]
        valuepp = sheet.row_values(rownum)[dic2[h]]
        if value != '':
            e.append([int(value_zone), value, float(valuepp)])

v = [i for i in vidy if i != '']
#print(v)
v = list(set(v))
v.sort()
zones = list(set(zones))
print('zones = ', zones)
print(zones)
#print(v)
#print(vidy)
#a = [print(i) for i in range(len(l)) if d in l[i]]
dic1 == dic2

wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet1')
ws.write(0,0,'Дата заполнения электронной таблицы')
ws.write(1,0,'Дата')
ws.write(2,0,'Местонахождение')
ws.write(3,0,'№ пояса')
ws.write(4,0,'N')
ws.write(5,0,'E')
ws.write(6,0,'Сообщество')
ws.write(7,0,'Примечание')
ws.write(8,0,'Протяженность пояса, м')
ws.write(9,0,'ОПП, %')
ws.write(10,0,'Ветошь, %')
ws.write(11,0,'Зелень, %')
ws.write(12,0,'Высота яруса, м')
ws.write(13,0,'Виды')

numzon = []
date = {0:0}
loc = {0:0}
lat = {0:0}
long = {0:0}
soob = {0:0}
length = {0:0}
opp = {0:0}
vetosh = {0:0}
zelen = {0:0}
height = {0:0}
for rownum in range(1,sheet.nrows):
    value_zone = sheet.row_values(rownum)[d3]
    numzon.append([rownum, int(value_zone)])
    date[value_zone] = sheet.row_values(rownum)[d01]
    loc[value_zone] = sheet.row_values(rownum)[d5]
    #loc.append([value_zone, value_loc])
    lat[value_zone] = sheet.row_values(rownum)[d7]
    #lat.append([value_zone, value_lat])
    long[value_zone] = sheet.row_values(rownum)[d9]
    #long.append([value_zone, value_long])
    soob[value_zone] = sheet.row_values(rownum)[d11]
    #soob.append([value_zone, value_soob])
    length[value_zone] = sheet.row_values(rownum)[d13]
    #length.append([value_zone, value_length])
    opp[value_zone] = sheet.row_values(rownum)[d15]
    #opp.append([value_zone, value_opp])
    vetosh[value_zone] = sheet.row_values(rownum)[d17]
    #vetosh.append([value_zone, value_vetosh])
    zelen[value_zone] = sheet.row_values(rownum)[d19]
    #zelen.append([value_zone, value_zelen])
    height[value_zone] = sheet.row_values(rownum)[d21]
    #height.append([value_zone, value_height])


#d = datetime.datetime.strptime('2011-06-09', '%Y-%m-%d') 
#d.strftime('%d-%m-%Y')
k = 14
for i in v:
    ws.write(k, 0, i)
    z.append([k, i])
    k += 1


#print(numzon)
#print(numzon[0][1])

#print(z)
for j in range(len(e)):
    for i in range(len(z)):
        if e[j][1] == z[i][1]:
            #print(e[j][1])
            ws.write(z[i][0], e[j][0], e[j][2])
zones.sort()
m = 1
for zonnum in range(len(zones)):
    ws.write(0, m, datetime.datetime.now().strftime('%d-%m-%Y'))
    #ws.write(1, m, date[zones[zonnum]])
    ws.write(2, m, loc[zones[zonnum]])
    ws.write(3, m, zones[zonnum])
    ws.write(4, m, lat[zones[zonnum]])
    ws.write(5, m, long[zones[zonnum]])
    ws.write(6, m, soob[zones[zonnum]])
    ws.write(8, m, length[zones[zonnum]])
    ws.write(9, m, opp[zones[zonnum]])
    ws.write(10, m, vetosh[zones[zonnum]])
    ws.write(11, m, zelen[zones[zonnum]])
    ws.write(12, m, height[zones[zonnum]])
    m += 1

for i in range(len(zones)+1):
    if i == 0:
        ws.col(i).width = 10000
    else:
        ws.col(i).width = 5000

wb.save('D:/NextGIS/table.xls')
