# One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. 
# It has the popular appeal of a Justin Bieber video. This endpoint structures the APOD imagery and associated metadata so that it can be repurposed for other applications. 
# In addition, if the concept_tags parameter is set to True, then keywords derived from the image explanation are returned. These keywords could be used as auto-generated hashtags for twitter or instagram feeds; but generally help with discoverability of relevant imagery.
from bowshock.helpers import nasa_api_key, bowshock_logger, vali_date, dispatch_http_get

logger = bowshock_logger()


def apod(date=None, concept_tags=None):
    '''
    HTTP REQUEST

    GET https://api.data.gov/nasa/planetary/apod

    QUERY PARAMETERS

    Parameter	Type	Default	Description
    date	YYYY-MM-DD	today	The date of the APOD image to retrieve
    concept_tags	bool	False	Return an ordered dictionary of concepts from the APOD explanation
    api_key	string	DEMO_KEY	api.data.gov key for expanded usage
    EXAMPLE QUERY

    https://api.data.gov/nasa/planetary/apod?concept_tags=True&api_key=DEMO_KEY
    '''
    base_url = "http://api.data.gov/nasa/planetary/apod?"

    if date:
        try:
            vali_date(date)
            base_url += "date=" + date + "&"
        except:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    if concept_tags == True:
        base_url += "concept_tags=True" + "&"

    req_url = base_url + "api_key=" + nasa_api_key()

    return dispatch_http_get(req_url)
