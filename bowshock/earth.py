# This endpoint retrieves the Landsat 8 image for the supplied location and date. 
# The response will include the date and URL to the image that is closest to the supplied date.
# The requested resource may not be available for the exact date in the request. You can retrieve a list of available resources through the assets endpoint.

# The cloud score is an optional calculation that returns the percentage of the queried image that is covered by clouds. 
# If False is supplied to the cloud_score parameter, then no keypair is returned. 
# If True is supplied, then a keypair will always be returned, even if the backend algorithm is not able to calculate a score. 
#Note that this is a rough calculation, mainly used to filter out exceedingly cloudy images.
import decimal

from bowshock.helpers import nasa_api_key, bowshock_logger, vali_date, validate_float, dispatch_http_get

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
        raise ValueError(
            "imagery endpoint expects lat and lon, type has to be float. Call the method with keyword args. Ex : lon=100.75, lat=1.5")
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
                "imagery endpoint expects lat and lon, type has to be float. Call the method with keyword args. Ex : lon=100.75, lat=1.5")

    if dim:
        try:
            validate_float(dim)
            dim = decimal.Decimal(dim)
            base_url + "dim=" + str(dim) + "&"
        except:
            raise ValueError("imagery endpoint expects dim to be a float")

    if date:
        try:
            vali_date(date)
            base_url += "date=" + date + "&"
        except:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    if cloud_score == True:
        base_url += "cloud_score=True" + "&"

    req_url = base_url + "api_key=" + nasa_api_key()

    return dispatch_http_get(req_url)

    # This endpoint retrieves the date-times and asset names for available imagery for a supplied location. 
    # The satellite passes over each point on earth roughly once every sixteen days. 
    # This is an amazing visualization of the acquisition pattern for Landsat 8 imagery. 
    # The objective of this endpoint is primarily to support the use of the imagery endpoint.


def assets(lon=None, lat=None, begin=None, end=None):
    '''
    HTTP REQUEST

    GET https://api.data.gov/nasa/planetary/earth/assets

    QUERY PARAMETERS

    Parameter	Type	Default	Description
    lat	float	n/a	Latitude
    lon	float	n/a	Longitude
    begin	YYYY-MM-DD	n/a	beginning of date range
    end	        YYYY-MM-DD	today	end of date range
    api_key	string	DEMO_KEY	api.data.gov key for expanded usage
    EXAMPLE QUERY

    https://api.data.gov/nasa/planetary/earth/assets?lon=100.75&lat=1.5&begin=2014-02-01&api_key=DEMO_KEY
    '''
    base_url = "http://api.data.gov/nasa/planetary/earth/assets?"

    if not lon or not lat:
        raise ValueError(
            "assets endpoint expects lat and lon, type has to be float. Call the method with keyword args. Ex : lon=100.75, lat=1.5")
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
                "assets endpoint expects lat and lon, type has to be float. Call the method with keyword args. Ex : lon=100.75, lat=1.5")

    if not begin:
        raise ValueError(
            "Begin date is missing, which is mandatory. Format : YYYY-MM-DD")
    else:
        try:
            vali_date(begin)
            base_url += "begin=" + begin + "&"
        except:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    if end:
        try:
            vali_date(end)
            base_url += "end=" + end + "&"
        except:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    req_url = base_url + "api_key=" + nasa_api_key()

    return dispatch_http_get(req_url)
