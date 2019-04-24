'''

API Information available at https://railwayapi.com/api/

get API key from api_key.py file

Connect this to front end

Need to add funtions for Fare


getTrains() api return format: https://railwayapi.com/api/#train-between-stations
getStation() api return format: https://railwayapi.com/api/#station-autocomplete-suggest

'''


import requests
import json
from . import api_key as APIKEY

def getStation(query):
    api_return = None
    # try block for if the request times out
    try:

        # recieves JSON Query
        api_return = requests.get(
            f'https://api.railwayapi.com/v2/suggest-station/name/{query}/apikey/{APIKEY.APIKey()}/', timeout=30)

        # turns query to pytohn dict
        api_return_pure = api_return.json()

        # if the request doesn't time out
        if api_return != 'request timeout':

            # 200 response code for success
            if api_return_pure['response_code'] == 200:

                return api_return_pure['stations']

            else:
                return 'response code error'

        # if the request does timeout
        else:
            return api_return

    # if request times out except runs
    except:
        api_return = 'request timeout'
        return api_return


def getTrains(source, destination, date):
    api_return = None
    try:
        api_return = requests.get(
            f'https://api.railwayapi.com/v2/between/source/{source}/dest/{destination}/date/{date}/apikey/{APIKEY.APIKey()}/', timeout=30)
        api_return_pure = api_return.json()

        # if the request doesn't time out
        if api_return != 'request timeout':

            # 200 response code for success
            if api_return_pure['response_code'] == 200:

                return api_return_pure['trains']

            else:
                return 'response code error'

        # if the request does timeout
        else:
            return api_return

    except:
        api_return = 'request timeout'
