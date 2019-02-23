import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OmI0YTRmNmFiYzI3NDQ5ZGY5MDRjYmE2NGYzNzZmNGZl'

historical_data_api = intrinio_sdk.HistoricalDataApi()

identifier = 'AAPL' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
tag = 'marketcap' # str | An Intrinio data tag ID or code-name
type = '' # str | Filter by type, when applicable (optional)
start_date = '2015-01-01' # date | Get historical data on or after this date (optional)
end_date = '2019-01-01' # date | Get historical date on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = historical_data_api.get_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoricalDataApi->get_historical_data: %s\n" % e)