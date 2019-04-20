from part_1 import User
from datetime import datetime, timedelta, date
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

class StockPrice:
    def __init__(self, name):
        self.name = name

    def time_definer(self):
        historical_period = []
        i = 0
        while len(historical_period) != 21:

            date_to_add = datetime.now() - timedelta(i)
            if date_to_add.weekday() != 5 and date_to_add.weekday() != 6:
                historical_period.append(str(date_to_add.date()))

            i += 1

        self.history = historical_period

    def get_daily_price(self):
        '''
        object -> None
        This method gets a json file with prices
        '''
        self.time_definer()

        ts = TimeSeries(key='WYXA08Z6LYUO5HL1', retries=2)
        # Get json object with the intraday data and another with  the call's metadata
        price = ts.get_daily(self.name)[0]
        result = {}

        for i in price:
            if i in self.history:
                result[i] = price[i]


        self.history = result

    def get_weekly_price(self):
        '''
        object -> None
        This method gets a json file with prices
        '''
        ts = TimeSeries(key='WYXA08Z6LYUO5HL1', retries=2)
        # Get json object with the intraday data and another with  the call's metadata
        price = ts.get_weekly(self.name)[0]

        self.history = {}
        for i in price:

            if len(self.history) < 25:
                self.history[i] = price[i]

            else:
                break

    def get_monthly_price(self):
        '''
        object -> None
        This method gets a json file with prices
        '''
        ts = TimeSeries(key='WYXA08Z6LYUO5HL1', retries=2)
        # Get json object with the intraday data and another with  the call's metadata
        price = ts.get_monthly(self.name)[0]

        self.history = {}
        for i in price:

            if len(self.history) < 25:
                self.history[i] = price[i]

            else:
                break

    def converter(self):
        for item in range(len(self.highest)):
            self.highest[item] = float(self.highest[item])

        for item in range(len(self.lowest)):
            self.lowest[item] = float(self.lowest[item])

        for item in range(len(self.volume)):
            self.volume[item] = int(self.volume[item])

    def highest_lowest_definer(self):

        self.days = []
        lowest = []
        highest = []
        volume = []
        for item in self.history:
            self.days.append(item)
            lowest.append(self.history[item]['3. low'])
            highest.append(self.history[item]['2. high'])
            volume.append(self.history[item]['5. volume'])


        self.days = sorted(self.days)
        self.lowest = list(reversed(lowest))
        self.highest = list(reversed(highest))
        self.volume = list(reversed(volume))
        self.converter()


    def paint(self):
        plt.plot(self.days, self.highest)
        plt.ylabel('some numbers')
        plt.show()



name = User()
company_1 = StockPrice(name.info)
company_1.get_weekly_price()
# elif name.typ == 'daily':
#     company_1.get_daily_price()
# else:
#     company_1.get_monthly_price()
company_1.highest_lowest_definer()
company_1.paint()
# print(company_1.highest)
# print(company_1.lowest)
# print(company_1.volume)
# print(company_1.days)




