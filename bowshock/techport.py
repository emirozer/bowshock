# https://data.nasa.gov/developer/external/techport/techport-api.pdf

#In May 2013, President Obama signed into law Executive Order 13642, Making Open and
#Machine Readable the New Default for Government Information. This requirement promotes
#continued job growth, government efficiency, and the social good that can be gained from
#opening government data to the public. In order to facilitate the Open Data initiatives,
#government information is managed as an asset throughout its life cycle to promote
#interoperability and openness, and wherever possible and legally permissible, released to the
#public in ways that make the data easy to find, accessible, and usable.
#NASA is committed to making its data available and machine-readable through an Application
#Programming Interface (API) to better serve its user communities. NASAs TechPort system
#provides a RESTful web services API to make technology Program and Project data available in
#a machine-readable format. This API can be used to export TechPort data into an XML format,
#which can be further processed and analyzed.

from bowshock.helpers import dispatch_http_get


def techport(Id):
    '''
    In order to use this capability, queries can be issued to the system with the following URI
    format:
    GET /xml-api/id_parameter
    Parameter Required? Value Description
    id_parameter Yes Type: String
    Default: None
    The id value of the TechPort record.
    TechPort values range from 0-20000.
    Not all values will yield results. Id
    values can be obtained through the
    standard TechPort search feature and
    are visible in the website URLs, e.g.
    http://techport.nasa.gov/view/0000,
    where 0000 is the id value.
    Example usage:
    http://techport.nasa.gov/xml-api/4795
    Output: The output of this query is an XML file with all field data of the TechPort record. 
    '''

    base_url = 'http://techport.nasa.gov/xml-api/'

    if not isinstance(Id, str):
        raise ValueError("The Id arg you provided is not the type of str")
    else:
        base_url += Id

    return dispatch_http_get(base_url)
