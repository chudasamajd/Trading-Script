import yfinance as yf
import datetime
import pandas as pd
import requests
import io
from nsepy import get_history

def index():

    url50 = 'https://archives.nseindia.com/content/indices/ind_nifty50list.csv'
    url100 = 'https://archives.nseindia.com/content/indices/ind_nifty100list.csv'
    url200 = 'https://archives.nseindia.com/content/indices/ind_nifty200list.csv'

    sfifty = requests.get(url50).content
    shundred = requests.get(url100).content
    stwohundred = requests.get(url200).content

    nifty50 = pd.read_csv(io.StringIO(sfifty.decode('utf-8')))
    nifty100 = pd.read_csv(io.StringIO(shundred.decode('utf-8')))
    nifty200 = pd.read_csv(io.StringIO(stwohundred.decode('utf-8')))

    nifty50 = nifty50['Symbol']
    nifty100 = nifty100['Symbol']
    nifty200 = nifty200['Symbol']

    return nifty50,nifty100,nifty200


to_dt = datetime.datetime.now().date()
from_dt = to_dt - datetime.timedelta(weeks=52)

nifty50,_,_ = index()
for i in nifty50:
    print(i)
    try:
        #data = yf.download(i + ".NS", start=from_dt, end=to_dt)
        data = get_history(symbol=i, start=from_dt, end=to_dt)
        data.to_csv('Data/'+i+'.csv')
    except:
        pass
#data = yf.download('.NS',start=from_dt,end=to_dt)
#data.to_csv('Data/TCS.csv')