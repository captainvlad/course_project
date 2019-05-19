from iexfinance.stocks import Stock
from datetime import datetime, timedelta
from alpha_vantage.timeseries import TimeSeries
from arrays import Array


class StockADT:
    '''
    This is class for needed ADT
    '''
    def __init__(self, name):
        '''
        obj, str -> None
        This method initializes an object
        '''
        self.array = Array(5)
        self.nname = name
        self.name = Stock(name)
        self.logo_giver(), self.news_giver(), self.get_fin(), self.highest_lowest_definer()

    def logo_giver(self):
        '''
        obj -> None
        This method puts link on image in array
        '''
        self.array.__setitem__(1,self.name.get_logo()['url'])

    def news_giver(self):
        '''
        obj -> None
        This method puts news on image in array
        '''
        self.array.__setitem__(2, self.name.get_news()[0])

    def get_fin(self):
        '''
        obj -> None
        This method calculates and puts koefficients in array
        '''
        list_of_koefs = []
        result = self.name.get_financials()[0]
        for item in ['totalLiabilities','currentDebt', 'currentAssets','totalAssets', 'operatingIncome', 'netIncome']:
            if result[item] == None:
                result[item] = 1
        list_of_koefs.append(round(result['totalLiabilities']/result['totalAssets'],2)) # коефіцієнт заборгованості
        list_of_koefs.append(round(result['currentAssets'] / result['currentDebt'],2)) # коефіцієнт покриття
        list_of_koefs.append(round(result['operatingIncome'] / result['currentAssets'],2)) # оборотність власного капіталу
        list_of_koefs.append(round(result['netIncome'] / result['currentAssets'],2)) # рентабельнітсь власного капіталу
        list_of_koefs.append(result['netIncome'])
        self.array.__setitem__(3, (list_of_koefs))

    def time_definer(self):
        '''
        obj -> None
        This method defines nearest 20 days in past
        '''
        historical_period = []
        i = 1
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
        price = ts.get_daily(self.nname)[0]
        result = {}

        for i in price:
            if i in self.history:
                result[i] = price[i]

        self.history = result

    def highest_lowest_definer(self):
        '''
        obj -> None
        This method defines highest and lowest prices for the 20-days period
        '''

        self.get_daily_price()
        lowest = []
        highest = []
        for item in self.history:
            lowest.append(float(self.history[item]['3. low']))
            highest.append(float(self.history[item]['2. high']))

        self.array.__setitem__(4, [min(lowest), max(highest)])

    def __str__(self):
        '''
        obj -> str
        Printing method
        '''
        message = ''

        for i in range(1,5):
            message += str(self.array.__getitem__(i))
            message += '\n'
        return message

