import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2019, 1, 1)
a = dt.datetime.today()
end = dt.datetime(a.year, a.month, a.day)


df = web.DataReader('AAPL', 'yahoo', start, end)

df['High'].plot()
df['Low'].plot()
plt.show()