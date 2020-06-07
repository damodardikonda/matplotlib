import pandas as pd
from datetime import datetime,timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


#dates = [
#    datetime(2019, 5, 24),
#    datetime(2019, 5, 25),
#    datetime(2019, 5, 26),
#    datetime(2019, 5, 27),
#    datetime(2019, 5, 28),
#    datetime(2019, 5, 29),
#    datetime(2019, 5, 30)
#]


#y=[0,2,3,4,5,6,7]



data=pd.read_csv('data3.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')


#plt.plot_date(dates,y,linestyle='solid')

#plt.gcf().autofmt_xdate()#it format a dates
#date_format=mpl_dates.DateFormatter('%b,%d,%y');# it formts a date first month,day,year

plt.tight_layout();
plt.show();
