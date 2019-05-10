import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web


class GraphCreator():
    '''
    This is method fot creating graph of prices
    '''
    def __init__(self, name_of_company):
        '''
        obj, str -> None
        '''
        self.name_of_company = name_of_company
        self.date_getter()

    def date_getter(self):
        '''
        obj -> None
        This is method to define time frames on graph
        '''
        self.year = input('Enter a year, you want to get data from (must be positive int): ')
        self.month = input('Enter a month, you want to get data from (must be positive int):')
        self.day = input('Enter a day, you want to get data from (must be positive int):')
        try:
            self.year, self.month, self.day = int(self.year), int(self.month), int(self.day)
            self.creator()
        except:
            print('Wrong input!')
            self.date_getter()


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
        plt.show()