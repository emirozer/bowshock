# This endpoint retrieves the Landsat 8 image for the supplied location and date. 
# The response will include the date and URL to the image that is closest to the supplied date.
# The requested resource may not be available for the exact date in the request. You can retrieve a list of available resources through the assets endpoint.

# The cloud score is an optional calculation that returns the percentage of the queried image that is covered by clouds. 
# If False is supplied to the cloud_score parameter, then no keypair is returned. 
# If True is supplied, then a keypair will always be returned, even if the backend algorithm is not able to calculate a score. 
#Note that this is a rough calculation, mainly used to filter out exceedingly cloudy images.


import requests
import decimal

from helpers import nasa_api_key, bowshock_logger, vali_date, validate_float


logger = bowshock_logger()


def imagery(lon=None, lat=None, dim=None, date=None, cloud_score=None):
    '''
    # ----------QUERY PARAMETERS----------

    # Parameter	Type	Default	Description
    # lat	float	n/a	Latitude
    # lon	float	n/a	Longitude
    # dim	float	0.025	width and height of image in degrees
    # date	YYYY-MM-DD  today	date of image ----if not supplied, then the most recent image (i.e., closest to today) is returned
    #cloud_score	bool	False	calculate the percentage of the image covered by clouds
    #api_key	string	vDEMO_KEY	api.data.gov key for expanded usage

    # ---------EXAMPLE QUERY--------

    # https://api.data.gov/nasa/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY

    '''
    
    base_url = "http://api.data.gov/nasa/planetary/earth/imagery?"
    
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
            
    if dim:
        validate_float(dim)
        base_url + "dim=" + dim + "&"

    if not date:
        raise ValueError("imagery endpoint expects date keyword argument, format : YYYY-MM-DD")
    else:
        vali_date(date)
        base_url += "date=" + date + "&"

    if cloud_score == True:
        base_url += "cloud_score=True" + "&"

    req_url = base_url + "api_key=" + nasa_api_key()
    
    logger.warning("Imagery endpoint, dispatching request : %s ", req_url)

    response = requests.get(req_url)

    print response.json
    logger.warning("Retrieved response from imagery endpoint: %s", response.text)

    return response.json
