from datetime import datetime
from iexfinance.stocks import get_historical_intraday


date = datetime(2018, 11, 27)

print(get_historical_intraday("AAPL", date)[0]) # [0] означає перша хвилина від початку торгів певного дня.