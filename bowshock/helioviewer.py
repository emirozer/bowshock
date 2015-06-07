# TODO: Complete helioviewer sdk

# http://helioviewer.org/api/docs/v1/
# The Helioviewer Project maintains a set of Public APIs with the goal of improving access to solar and heliospheric datasets to scientists, educators, developers, and the general public. Read below for descriptions of each API endpoint and examples of usage.
from bowshock.helpers import bowshock_logger, validate_iso8601, dispatch_http_get

logger = bowshock_logger()


def getjp2image(date,
                sourceId=None,
                observatory=None,
                instrument=None,
                detector=None,
                measurement=None):
    '''
    Helioviewer.org and JHelioviewer operate off of JPEG2000 formatted image data generated from science-quality FITS files. Use the APIs below to interact directly with these intermediary JPEG2000 files.
    
    Download a JP2 image for the specified datasource that is the closest match in time to the `date` requested.

    Either `sourceId` must be specified, or the combination of `observatory`, `instrument`, `detector`, and `measurement`.

    Request Parameters:

    Parameter	Required	Type	Example	Description
    date	Required	string	2014-01-01T23:59:59Z	Desired date/time of the JP2 image. ISO 8601 combined UTC date and time UTC format.
    sourceId	Optional	number	14	Unique image datasource identifier.
    observatory	Optional	string	SDO	Observatory name.
    instrument	Optional	string	AIA	Instrument name.
    detector	Optional	string	AIA	Detector name.
    measurement	Optional	string	335	Measurement name.
    jpip	Optional	boolean	false	Optionally return a JPIP URI instead of the binary data of the image itself.
    json	Optional	boolean	false	Optionally return a JSON object.


    EXAMPLE: http://helioviewer.org/api/v1/getJP2Image/?date=2014-01-01T23:59:59Z&sourceId=14&jpip=true
    '''

    base_url = 'http://helioviewer.org/api/v1/getJP2Image/?'
    req_url = ''

    try:
        validate_iso8601(date)
        if not date[-1:] == 'Z':
            date += 'Z'
        base_url += 'date=' + date
    except:
        raise ValueError(
            "Your date input is not in iso8601 format. ex: 2014-01-01T23:59:59")

    if sourceId:
        if not isinstance(sourceId, int):
            logger.error("The sourceId argument should be an int, ignoring it")
        else:
            base_url += "sourceId=" + str(sourceId) + "&"

    if observatory:
        if not isinstance(observatory, str):
            logger.error(
                "The observatory argument should be a str, ignoring it")
        else:
            base_url += "observatory=" + observatory + "&"

    if instrument:
        if not isinstance(instrument, str):
            logger.error(
                "The instrument argument should be a str, ignoring it")
        else:
            base_url += "instrument=" + instrument + "&"
    if detector:
        if not isinstance(detector, str):
            logger.error("The detector argument should be a str, ignoring it")
        else:
            base_url += "detector=" + detector + "&"

    if measurement:
        if not isinstance(measurement, str):
            logger.error(
                "The measurement argument should be a str, ignoring it")
        else:
            base_url += "measurement=" + detector + "&"

    req_url += base_url + "jpip=true"

    return dispatch_http_get(req_url)


def getjp2header(Id):
    '''
    GET /api/v1/getJP2Header/


    Get the XML header embedded in a JPEG2000 image. Includes the FITS header as well as a section of Helioviewer-specific metadata.

    Request Parameters:

    Parameter	Required	Type	Example	Description
    id	Required	number	7654321	Unique JP2 image identifier.
    callback	Optional	string		Wrap the response object in a function call of your choosing.

    Example (A):

    string (XML)

    Example Request:

    http://helioviewer.org/api/v1/getJP2Header/?id=7654321
    '''
    base_url = 'http://helioviewer.org/api/v1/getJP2Header/?'

    if not isinstance(Id, int):
        raise ValueError("The Id argument should be an int, ignoring it")
    else:
        base_url += "id=" + str(Id)

    return dispatch_http_get(base_url)
