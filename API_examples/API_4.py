from iexfinance.stocks import get_earnings_today, Stock


appl = Stock("AAPL")


print(appl.get_earnings())
