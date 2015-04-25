import requests
import logging
import datetime
import os


def bowshock_logger():
    '''creates a logger obj'''

    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    logger = logging.getLogger('bowshock_logger')

    return logger


logger = bowshock_logger()


def dispatch_http_get(url):

    logger.warning("Dispatching HTTP GET Request : %s ", url)

    response = requests.get(url)

    logger.warning("Retrieved response: %s", response.text)

    return response


def nasa_api_key():
    '''
    Returns personal api key.
    You can acquire one from here : 
    https://data.nasa.gov/developer/external/planetary/#apply-for-an-api-key
    IMPORTANT: SET YOUR API KEY AS AN ENVIRONMENT VARIABLE.
    '''

    api_key = os.environ["NASA_API_KEY"]

    return api_key


def vali_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")


def validate_year(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY")


def validate_float(*args):
    for arg in args:
        if isinstance(arg, float):
            return True
        else:
            raise ValueError("Expected float for argument")


def validate_iso8601(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY")
