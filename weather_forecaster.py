"""
Developer: Rob Marchetti
Description: A simple  example of making a call to the governments weather api
to get the weather forecast for my location. Not the most eloquent but it works
"""
import requests
from pprint import pprint
from time import gmtime, strftime




def get_forecast(location):
    """Gets the weather forecast based on location using a lat/lon."""

    url = f'https://api.weather.gov/points/{location}'
    res = requests.get(url)

    # Json data
    data = res.json()

    # Get the City - will print out later
    city = data['properties']['relativeLocation']['properties']['city']
    # Get the State
    state = data['properties']['relativeLocation']['properties']['state']

    # get the forecast url from the returned data
    forecast_url = data['properties']['forecast']

    # request forecast data from url
    res = requests.get(forecast_url)
    # Now we have the forecast data
    forecast_data = res.json()

    # Now we need to format and print out the forecast data
    fdata = forecast_data['properties']['periods'][1]
    # Use the following keys from weather_list to get the values of what we want from the forecast data
    weather_list = ['temperature', 'windSpeed', 'windDirection', 'shortForecast', 'detailedForecast']


    print(f'\nGetting forecast for: {city}, {state}\n')
    print(strftime("Date: %m-%d-%Y\nTime:%H:%M:%S\n", gmtime()))

    n = {k: fdata[k] for k in fdata.keys() & set(weather_list)}
    for k, v in n.items():
        pprint(f'{k.capitalize()}: {v}')


# Gets the forecast for Barrington RI using lat lon.
# Note: decimals can only be 4 places or it will error
loc = '41.7280,-71.3948'
get_forecast(loc)
