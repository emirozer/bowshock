# There is no doubt that, on average, the earth is warming. However, the warming is spatially heterogenous. 
# How much warmer (or cooler) is your hometown? This endpoint reports local temperature anomalies from the 
# Goddard Institute for Space Studies Surface Temperature Analysis via the New Scientist web application to explore global temperature anomalies. 
# This endpoint restructures the query and response to correspond to other APIs on api.nasa.gov. The developer supplies a location and date range, and the returned object is a list of dictionaries that is ready for visualization in the d3 framework.
import decimal

from bowshock.helpers import nasa_api_key, bowshock_logger, validate_year, validate_float, dispatch_http_get

logger = bowshock_logger()


def adress(adress=None, begin=None, end=None):
    '''
    HTTP REQUEST

    GET https://api.data.gov/nasa/planetary/earth/temperature/address

    QUERY PARAMETERS

    Parameter	Type	Default	Description
    text	string	n/a	Address string
    begin	int	1880	beginning year for date range, inclusive
    end	int	2014	end year for date range, inclusive
    api_key	string	DEMO_KEY	api.data.gov key for expanded usage
    EXAMPLE QUERY

    https://api.data.gov/nasa/planetary/earth/temperature/address?text=1800 F Street, NW, Washington DC&begin=1990
    '''
    base_url = "http://api.data.gov/nasa/planetary/earth/temperature/adress?"

    if not adress:
        raise ValueError(
            "adress is missing, which is mandatory. example : 1800 F Street, NW, Washington DC")
    elif not isinstance(adress, str):
        try:
            adress = str(adress)
        except:
            raise ValueError("adress has to be type of string")
    else:
        base_url += "adress=" + adress + "&"

    if not begin:
        raise ValueError(
            "Begin year is missing, which is mandatory. Format : YYYY")
    else:
        try:
            validate_year(begin)
            base_url += "begin=" + begin + "&"
        except:
            raise ValueError("Incorrect begin year format, should be YYYY")

    if end:
        try:
            validate_year(end)
            base_url += "end=" + end + "&"
        except:
            raise ValueError("Incorrect end year format, should be YYYY")

    req_url = base_url + "api_key=" + nasa_api_key()

    return dispatch_http_get(req_url)


def coordinate(lon=None, lat=None, begin=None, end=None):
    '''
    HTTP REQUEST

    GET https://api.data.gov/planetary/earth/temperature/coords

    QUERY PARAMETERS

    Parameter	Type	Default	Description
    lat	float	n/a	Latitude
    lon	float	n/a	Longitude
    begin	int	1880	beginning year for date range, inclusive
    end	int	2014	end year for date range, inclusive
    api_key	string	DEMO_KEY	api.data.gov key for expanded usage
    EXAMPLE QUERY

    https://api.data.gov/nasa/planetary/earth/temperature/coords?lon=100.3&lat=1.6&begin=1990&end=2005&api_key=DEMO_KEY


    '''
    base_url = "http://api.data.gov/nasa/planetary/earth/temperature/coords?"

    if not lon or not lat:
        raise ValueError(
            "temp/coordinate endpoint expects lat and lon, type has to be float. Call the method with keyword args. Ex : lon=100.75, lat=1.5")
    else:
        try:
            validate_float(lon, lat)
            # Floats are entered/displayed as decimal numbers, but your computer 
            # (in fact, your standard C library) stores them as binary. 
            # You get some side effects from this transition:
            # >>> print len(repr(0.1))
            # 19
            # >>> print repr(0.1)
            # 0.10000000000000001
            # Thus using decimal to str transition is more reliant
            lon = decimal.Decimal(lon)
            lat = decimal.Decimal(lat)
            base_url += "lon=" + str(lon) + "&" + "lat=" + str(lat) + "&"
        except:
            raise ValueError(
                "temp/coordinate endpoint expects lat and lon, type has to be float. Call the method with keyword args. Ex : lon=100.75, lat=1.5")

    if not begin:
        raise ValueError(
            "Begin year is missing, which is mandatory. Format : YYYY")
    else:
        try:
            validate_year(begin)
            base_url += "begin=" + begin + "&"
        except:
            raise ValueError("Incorrect begin year format, should be YYYY")

    if end:
        try:
            validate_year(end)
            base_url += "end=" + end + "&"
        except:
            raise ValueError("Incorrect end year format, should be YYYY")
    req_url = base_url + "api_key=" + nasa_api_key()

    return dispatch_http_get(req_url)
