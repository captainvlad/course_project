from iexfinance.stocks import Stock

tsla = Stock('TSLA')
# print(tsla.get_logo())
print(tsla.get_financials())
# print(tsla.get_volume())
# print(tsla.get_news())