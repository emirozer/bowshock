# http://hacktheuniverse.github.io/star-api/

from bowshock.helpers import dispatch_http_get


def stars():
    '''
    This endpoint gets you a list of all stars in json
    '''

    base_url = "http://star-api.herokuapp.com/api/v1/stars"

    return dispatch_http_get(base_url)


def search_star(star):
    '''
    It is also possible to query the stars by label, here is an example of querying for the star labeled as Sun.

    http://star-api.herokuapp.com/api/v1/stars/Sun
    '''

    base_url = "http://star-api.herokuapp.com/api/v1/stars/"

    if not isinstance(star, str):
        raise ValueError("The star arg you provided is not the type of str")
    else:
        base_url += star

    return dispatch_http_get(base_url)


def exoplanets():
    '''
    gets all exoplanets in json
    '''

    base_url = "http://star-api.herokuapp.com/api/v1/exo_planets"

    return dispatch_http_get(base_url)


def search_exoplanet(exoplanet):
    '''
    It is also possible to query the exoplanets by label, here is an example of querying for the exoplanet labeled as 11 Com

    http://star-api.herokuapp.com/api/v1/exo_planets/11 Com
    '''

    base_url = "http://star-api.herokuapp.com/api/v1/exo_planets/"

    if not isinstance(exoplanet, str):
        raise ValueError(
            "The exoplanet arg you provided is not the type of str")
    else:
        base_url += exoplanet

    return dispatch_http_get(base_url)


def local_group_of_galaxies():
    '''
    gets a local group of galaxies in json
    '''

    base_url = "http://star-api.herokuapp.com/api/v1/local_groups"

    return dispatch_http_get(base_url)


def search_local_galaxies(galaxy):
    '''
    It is also possible to query the local galaxies by label, here is an example of querying for the local galaxy labeled  IC 10

    http://star-api.herokuapp.com/api/v1/local_groups/IC 10
    '''

    base_url = "http://star-api.herokuapp.com/api/v1/local_groups/"

    if not isinstance(galaxy, str):
        raise ValueError("The galaxy arg you provided is not the type of str")
    else:
        base_url += galaxy

    return dispatch_http_get(base_url)


def star_clusters():
    '''
    retrieves all open star clusters in json
    '''

    base_url = "http://star-api.herokuapp.com/api/v1/open_cluster"

    return dispatch_http_get(base_url)


def search_star_cluster(cluster):
    '''
    It is also possible to query the star clusters by label, here is an example of querying for the star cluster labeled Berkeley 59

    http://star-api.herokuapp.com/api/v1/open_cluster/Berkeley 59
    '''

    base_url = "http://star-api.herokuapp.com/api/v1/open_cluster/"

    if not isinstance(cluster, str):
        raise ValueError("The cluster arg you provided is not the type of str")
    else:
        base_url += cluster

    return dispatch_http_get(base_url)
