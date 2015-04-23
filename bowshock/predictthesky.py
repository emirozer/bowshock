# http://predictthesky.org/developers.html

# Below description is taken from their website.
# Introduction
# It all starts with the root URL, the routes below are all based around this:

# Retrieving Space Events
# Events are the core purpose of the API. It returns a list of space objects (see below) which are visible from your current location, scored by a likelyhood that it can be seen. A weather object for the start and end of the event is returned.

# Method	Route	Arguments
# GET	/events/all	lat, lon, elevation, limit, date
# GET	/event/<category>	lat, lon, elevation, limit, date
import requests
import decimal

from helpers import bowshock_logger, validate_iso8601, validate_float

logger = bowshock_logger()

def space_events(lon=None, lat=None, limit=None, date=None):
    '''
    
    lat & lon expect decimal latitude and longitude values. (Required)
    elevation assumes meters. (Optional)
    limit assumes an integer. Default is 5. (Optional)
    date expects an ISO 8601 formatted date. (Optional)
    '''
    
    base_url = 'http://api.predictthesky.org'
    
    if not lon or not lat:
        raise ValueError("imagery endpoint expects lat and lon, type has to be float. Call the method with keyword args. Ex : lon=100.75, lat=1.5")
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
            raise ValueError("imagery endpoint expects lat and lon, type has to be float. Call the method with keyword args. Ex : lon=100.75, lat=1.5")

    if date:
         try:
             validate_iso8601(date)
             base_url += 'date=' + date
        except:
            raise ValueError("Your date input is not in iso8601 format. ex: 2014-01-01T23:59:59")
    
    
    logger.warning("Imagery endpoint, dispatching request : %s ", req_url)

    response = requests.get(req_url)

    
    logger.warning("Retrieved response from imagery endpoint: %s", response.text)

    return response


