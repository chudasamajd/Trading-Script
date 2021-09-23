from EMA_Crossing_Check import final_dates
import pandas as pd
import numpy as np

date1,_ = final_dates()

data = pd.read_csv('Data/TCS.csv')


#---------------- Day when 5 Day EMA Cross 13 Day EMA -------------
record13 = []
for x in date1:
    for i in data.index:
        if data['Date'][i] == x:
            record13.append([data['Date'][i+1],data['Open'][i+1],data['High'][i+1],data['Close'][i+1],data['Low'][i+1]])


#--------------- Buy on High of Day when 5 Day EMA Cross 13 Day EMA -------------
buyonhigh = []
rate = float(input('Enter Profit Rate :'))
rate = rate*0.01
for i in record13:
    buyonhigh.append([i[0],np.round(i[2], decimals=2),np.round((i[2]*rate)+i[2],decimals=2)])

for i in data.index:
    for j in buyonhigh:
        if data['Date'][i] == j[0]:
            print(j[0],"---",j[1],"---",j[2])
            for count in range(1,5):
                print(data['High'][i+count])
                if j[2] < data['High'][i+count]:
                    print("...Profit Booked...")