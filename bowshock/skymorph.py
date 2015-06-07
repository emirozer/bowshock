# http://www.asterank.com/skymorph

#This API wraps NASA's SkyMorph archive in a RESTful JSON interface. Currently, it provides observation and image data from the NEAT survey.
from bowshock.helpers import bowshock_logger, dispatch_http_get

logger = bowshock_logger()


def search_target_obj(target):
    '''
    Query for a specific target:

    http://asterank.com/api/skymorph/search?<params>
    target	Target object (lookup in MPC).
    '''
    base_url = "http://asterank.com/api/skymorph/search?"

    if not isinstance(target, str):
        raise ValueError("The target arg you provided is not the type of str")
    else:
        base_url += "target=" + target

    return dispatch_http_get(base_url)


def search_orbit(**kwargs):
    '''
    Query based on orbital elements:

    http://asterank.com/api/skymorph/search_orbit?<params>
    epoch	Epoch ([M]JD or ISO)
    ecc	eccentricity
    per	Perihelion distance (AU)
    per_date	Perihelion date ([M]JD or ISO)
    om	Longitude of ascending node (deg)
    w	Argument of perihelion (deg)
    i	Inclination (deg)
    H	Absolute magnitude

    '''

    base_url = "http://asterank.com/api/skymorph/search_orbit?"

    for key in kwargs:
        base_url += str(key) + "=" + kwargs[key] + "&"

        # remove the unnecessary & at the end
    base_url = base_url[:-1]

    return dispatch_http_get(base_url)


def search_position(**kwargs):
    '''
    Query based on position and time (+/- 1 day):

    http://asterank.com/api/skymorph/search_position?<params>
    ra	Right ascension (HMS)
    Dec	Declination (DMS)
    time	Date and time (UTC)
    per_date	Perihelion date ([M]JD or ISO)
    om	Longitude of ascending node (deg)
    w	Argument of perihelion (deg)
    i	Inclination (deg)
    H	Absolute magnitude

    '''

    base_url = "http://asterank.com/api/skymorph/search_position?"

    for key in kwargs:
        base_url += str(key) + "=" + kwargs[key] + "&"

        # remove the unnecessary & at the end
    base_url = base_url[:-1]

    return dispatch_http_get(base_url)
