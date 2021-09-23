import backtrader
import datetime
from strategies import TestStrategy

a = backtrader.Cerebro()

a.broker.set_cash(20000)

data = backtrader.feeds.YahooFinanceCSVData(dataname='RELIANCE.NS.csv',fromdate=datetime.datetime(2020,11,1),todate=datetime.datetime(2020,11,13),reverse=False)

a.adddata(data)

a.addstrategy(TestStrategy)

a.addsizer(backtrader.sizers.FixedSize,stake=10)

print('Starting Portfolio Value : %.2f' % a.broker.getvalue())

a.run()

print('Final Portfolio Value : %.2f' % a.broker.getvalue())
