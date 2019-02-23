from iexfinance.stocks import Stock

tsla = Stock('TSLA')
print(tsla.get_price())