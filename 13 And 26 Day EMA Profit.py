from EMA_Crossing_Check import final_dates
import pandas as pd
import numpy as np
import datetime
from dateutil import parser

date1,date2 = final_dates()

data = pd.read_csv('Data/TCS.csv')


#---------------- Day when 5 Day EMA Cross 13 Day EMA -------------
record13 = []
for x in date1:
    for i in data.index:
        if data['Date'][i] == x:
            record13.append([data['Date'][i+1],data['Open'][i+1],data['High'][i+1],data['Close'][i+1],data['Low'][i+1]])

print('Last Date When 5 Day Crossing 13 Day EMA --',x)

#---------------- Day when 5 Day EMA Cross 26 Day EMA -------------
record26 = []
for x in date2:
    for i in data.index:
        if data['Date'][i] == x:
            record26.append([data['Date'][i+1],data['Open'][i+1],data['High'][i+1],data['Close'][i+1],data['Low'][i+1]])

print('Last Date When 5 Day Crossing 26 Day EMA --',x)

day13_26 = []
for i in date1:
    for j in date2:
        if i < j:
            if not j in day13_26:
                day13_26.append(j)


for i in day13_26:
    for j in data.index:
        if i == data['Date'][j]:
            print("----",data['High'][j],"----")
            for count in range(1,30):
                try:
                    if parser.parse(data['Date'][j+count]) < datetime.datetime.now():
                        print(count,"->",data['Date'][j+count],'----',data['Low'][j+count])
                except:
                    pass


