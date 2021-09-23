import talib
import yfinance as yf
import pandas as pd


ind_ticker = pd.read_csv('NSE Ticker.csv')


print(ind_ticker)

#----------- For One Stock -------------
#data = yf.download("TCS.NS",start="2020-11-01",end="2020-11-28")
#num = talib.CDLMORNINGSTAR(data['Open'],data['High'],data['Low'],data['Close'])
#aapl_historical = aapl.history(start="2020-06-02", end="2020-06-07", interval="1m")
#num = talib.CDLENGULFING(data['Open'],data['High'],data['Low'],data['Close'])
#print(num[num==100])

result = {}
j = 0

#------------ For All NSE Stocks ---------------
for i in ind_ticker['TICKERS']:
    if j == 20:
        break
    print(i)
    try:
        data = yf.download(i, start="2020-10-01", end="2020-11-28")
        num = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
        #num2 = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

        if len(num[num == 100]) != 0:
            dates = []
            data = num[num == 100]
            for x in data.index:
                dates.append(x.strftime('%d-%m-%Y'))
                #print(x.strftime('%d-%m-%Y'))
            result[i] = dates
        #print(num2[num2!=0])
    except:
        print()
    j += 1


print(result)