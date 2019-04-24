import requests
import json
from . import api_key


def getStation(query):
    api_return = None
    # try block for if the request times out
    try:

        # recieves JSON Query
        api_return = requests.get(
            f'https://api.railwayapi.com/v2/suggest-station/name/{query}/apikey/{APIKey}/', timeout=30)

        # turns query to pytohn dict
        api_return_pure = api_return.json()

    # if request times out except runs
    except:
        api_return = 'request timeout'

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


def getTrains():
    pass
