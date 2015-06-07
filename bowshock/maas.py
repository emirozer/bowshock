# http://marsweather.ingenology.com/#get_started

# Below description taken from https://github.com/ingenology/mars_weather_api
# The {MAAS} API is an open source REST API built to help make it easier and more efficient to build interactive applications that want to utilize the wealth of weather data being transmitted by the Curiosity Rover on Mars. Our API is built upon the REMS (Rover Environmental Monitoring Station) data provided by the Centro de Astrobiologia (CSIC-INTA).
# This API is built on Django and Django REST Framework.
# Our implementation of the API is available at marsweather.ingenology.com.
import decimal

from bowshock.helpers import nasa_api_key, bowshock_logger, vali_date, validate_float, dispatch_http_get

logger = bowshock_logger()


def maas_latest():
    '''
    will return a JSON object for the latest report:

{
    "report": {
        "terrestrial_date": "2013-05-01", 
        "sol": 261, 
        "ls": 310.5, 
        "min_temp": -69.75, 
        "min_temp_fahrenheit": -93.55, 
        "max_temp": -4.48, 
        "max_temp_fahrenheit": 23.94, 
        "pressure": 868.05, 
        "pressure_string": "Higher", 
        "abs_humidity": null, 
        "wind_speed": null, 
        "wind_direction": "--", 
        "atmo_opacity": "Sunny", 
        "season": "Month 11", 
        "sunrise": "2013-05-01T11:00:00Z", 
        "sunset": "2013-05-01T22:00:00Z"
    }
}

    '''
    base_url = 'http://marsweather.ingenology.com/v1/latest/'

    return dispatch_http_get(base_url)


def maas_archive(begin, end):
    '''
    This returns a collection of JSON objects for every weather report available for October 2012:

{
    "count": 29, 
    "next": "http://marsweather.ingenology.com/v1/archive/?terrestrial_date_end=2012-10-31&terrestrial_date_start=2012-10-01&page=2", 
    "previous": null, 
    "results": [
        ...
    ]
}
    '''

    base_url = 'http://marsweather.ingenology.com/v1/archive/?'
    try:
        vali_date(begin)
        vali_date(end)
        base_url += 'terrestrial_date_start=' + begin + "&" + 'terrestrial_date_end=' + end
    except:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    return dispatch_http_get(base_url)
