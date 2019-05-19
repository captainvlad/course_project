import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web


class GraphCreator():
    '''
    This is method fot creating graph of prices
    '''
    def __init__(self, name_of_company, year, month, day):
        '''
        obj, str -> None
        This method initializes an object
        '''
        self.year = year
        self.month = month
        self.day = day
        self.name_of_company = name_of_company
        self.creator()


    def creator(self):
        '''
        obj -> None
        This is method to create a graph
        '''
        style.use('ggplot')

        start = dt.datetime(self.year, self.month, self.day)
        a = dt.datetime.today()
        end = dt.datetime(a.year, a.month, a.day)
        df = web.DataReader(self.name_of_company, 'yahoo', start, end)

        df['High'].plot()
        df['Low'].plot()
        plt.savefig('chart.jpg')