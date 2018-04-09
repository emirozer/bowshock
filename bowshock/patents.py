# The NASA patent portfolio is available to benefit US citizens. 
# Through partnerships and licensing agreements with industry, 
# these patents ensure that NASAs investments in pioneering research find secondary uses that benefit the economy
# create jobs, and improve quality of life. This endpoint provides structured, searchable developer access to NASAs patents that have been curated to support technology transfer.
from bowshock.helpers import nasa_api_key, bowshock_logger, dispatch_http_get

logger = bowshock_logger()


def patents(query=None, concept_tags=None, limit=None):
    '''
    HTTP REQUEST

    GET https://api.nasa.gov/patents

    QUERY PARAMETERS

    Parameter	Type	Default	Description
    query	string	None	Search text to filter results
    concept_tags	bool	False	Return an ordered dictionary of concepts from the patent abstract
    limit	int	all	number of patents to return
    api_key	string	DEMO_KEY	api.nasa.gov key for expanded usage
    EXAMPLE QUERY

    https://api.nasa.gov/patents/content?query=temperature&limit=5&api_key=DEMO_KEY

    '''
    base_url = "https://api.nasa.gov/patents/content?"

    if not query:
        raise ValueError("search query is missing, which is mandatory.")
    elif not isinstance(query, str):
        try:
            query = str(query)
        except:
            raise ValueError("query has to be type of string")
    else:
        base_url += "query=" + query + "&"

    if concept_tags == True:
        base_url += "concept_tags=True" + "&"

    if limit:
        if not isinstance(limit, int):
            logger.error(
                "The limit arg you provided is not the type of int, ignoring it")

        base_url += "limit=" + str(limit) + "&"

    req_url = base_url + "api_key=" + nasa_api_key()

    return dispatch_http_get(req_url)
