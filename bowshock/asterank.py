# http://www.asterank.com/api
# The Asterank database is a thin layer over the NASA/JPL Small Body Database, merged with JPL delta-v data, published asteroid mass data, 
# and their own calculations.

#The database currently runs on mongodb and queries must adhere to mongo's json format for a 'find' operation.
import json
from bowshock.helpers import bowshock_logger, dispatch_http_get

logger = bowshock_logger()


def asterank(query=None, limit=None):
    '''
    Format
    Requests are of the form:

    http://asterank.com/api/asterank?query={query}&limit={limit}
    Response data formats are largely derived from NASA/JPL's Small Body Database query browser. Exceptions to this are the delta-v field (dv), the mass field (GM), and the normalized spectral type field (spec). Additional Asterank scores are included: closeness, price ($), and overall score.

    Sample Request
    This request returns an asteroid with a roughly circular orbit, low inclination, and semi-major axis less than 1.5 AU:

    /api/asterank?query={"e":{"$lt":0.1},"i":{"$lt":4},"a":{"$lt":1.5}}&limit=1

    '''

    base_url = "http://asterank.com/api/asterank?"

    if query:
        try:
            query = json.dumps(query)

            base_url += "query=" + query + "&"
        except:
            raise ValueError("query= param is not valid json.")
    else:
        raise ValueError(
            "query= param is missing, expecting json data format.")

    if limit:
        if not isinstance(limit, int):
            logger.error(
                "The limit arg you provided is not the type of int, ignoring it")
        base_url += "limit=" + str(limit)
    else:
        raise ValueError("limit= param is missing, expecting int")

    return dispatch_http_get(base_url)
