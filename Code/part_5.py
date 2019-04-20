from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OmI0YTRmNmFiYzI3NDQ5ZGY5MDRjYmE2NGYzNzZmNGZl'

company_api = intrinio_sdk.CompanyApi()

page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)