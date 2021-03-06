from iexfinance.stocks import Stock
from datetime import datetime, timedelta
from alpha_vantage.timeseries import TimeSeries
from arrays import Array


class StockADT:
    def __init__(self, name):
        self.array = Array(5)
        self.nname = name
        self.name = Stock(name)
        self.logo_giver(), self.news_giver(), self.get_fin(), self.highest_lowest_definer()

    def logo_giver(self):
        self.array.__setitem__(1,self.name.get_logo()['url'])

    def news_giver(self):
        self.array.__setitem__(2, self.name.get_news()[0])

    def get_fin(self):
        list_of_koefs = []
        result = self.name.get_financials()[0]
        list_of_koefs.append(round(result['totalAssets']/result['totalLiabilities'],2)) # коефіцієнт боргового навантаження
        list_of_koefs.append(round(result['currentAssets'] / result['currentDebt'],2)) # коефіцієнт маневреності капіталу
        list_of_koefs.append(round(result['operatingIncome'] / result['currentAssets'],2)) # оборотність власного капіталу
        list_of_koefs.append(round(result['netIncome'] / result['currentAssets'],2)) # рентабельнітсь власного капіталу
        self.array.__setitem__(3, (round((sum(list_of_koefs) / 4), 2)))

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
        price = ts.get_daily(self.nname)[0]
        result = {}

        for i in price:
            if i in self.history:
                result[i] = price[i]

        self.history = result

    def highest_lowest_definer(self):

        self.get_daily_price()
        lowest = []
        highest = []
        for item in self.history:
            lowest.append(self.history[item]['3. low'])
            highest.append(self.history[item]['2. high'])

        self.array.__setitem__(4, [max(lowest), min(highest)])

