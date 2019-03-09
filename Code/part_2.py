from part_1 import User
from datetime import datetime, timedelta, date
from alpha_vantage.timeseries import TimeSeries
from iexfinance.stocks import get_earnings_today, Stock

class StockPrice(User):
    def __init__(self, prices = None, time = None, company_info = None, info = None):
        '''
        object,dict, str, list, str -> None
        This mehtod initializes an object
        '''
        super().__init__(info)
        self.time = time
        self.company_info = company_info
    def get_time(self):
        '''
        object -> None
        This method takes 30 days back from a day when using
        '''
        self.time = str(datetime.now() - timedelta(days=30))[0:10]
    def get_pric(self):
        '''
        object -> None
        This method gets a json file with prices
        '''
        ts = TimeSeries(key='WYXA08Z6LYUO5HL1', retries=5)
        # Get json object with the intraday data and another with  the call's metadata
        self.price = ts.get_daily(self.info)[0]
    def get_company_info(self):
        '''
        object -> None
        This method takes list of jsons with company's earnings
        '''
        earnings = Stock(self.info)
        self.company_info = earnings.get_earnings()

class DateTaker(StockPrice):
    def __init__(self, prices = None):
        '''
        object, dict -> None
        This method initializes an object
        '''
        super().__init__(prices)
        self.needed_date = needed_date
    def starter(self):
        '''
        object -> None
        This method counts 30 days from the day when using in 'datetime.date' type
        '''
        self = StockPrice
        self.info_getter(self)
        self.get_time(self)
        self.get_pric(self)
        self.get_company_info(self)
        if self.time[5] == '0':
            self.time = self.time[:5] + self.time[6:]
        if self.time[7] == '0':
            self.time = self.time[:7] + self.time[8:]
        self.time = date(int(self.time[0:4]),int(self.time[self.time.index('-')+1:self.time.rindex('-')]),int(self.time[self.time.rindex('-')+1:]))
    def date_checker(self):
        i = 0
        for keey in self.price.keys():
            if keey[5:7][0] == 0:
                month = int(keey[5:7].replace('0',''))
            else:
                month = int(keey[5:7])
            if keey[8:][0] == 0:
                day = int(keey[8:].replace('0',''))
            else:
                day = int(keey[8:])
            year = int(keey[0:4])
            data = date(year,month,day) - timedelta(i)
            print(data)
            if data >= self.time:
                i += 1
            else:
                break



a = DateTaker
print("Welcome to demo version!")
a.starter(a)
print('Here is company earnings info: ')
print(a.company_info)
print('Here is company prices:')
print(a.price)
print('Here is 30 days in past since today day:')
print(a.time)
print('Here are days, we have to analyze: ')
a.date_checker(a)

