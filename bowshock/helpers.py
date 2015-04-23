import logging
import datetime

def bowshock_logger():
    '''creates a logger obj'''
    
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    logger = logging.getLogger('bowshock_logger')
    
    return logger


def nasa_api_key():
    '''
    Returns personal api key.
    You can acquire one from here : 
    https://data.nasa.gov/developer/external/planetary/#apply-for-an-api-key

    '''
    api_key=''

    return api_key

def vali_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

def validate_float(*args):
    for arg in args:
        if isinstance(arg, float):
            return True
        else:
            raise ValueError("Expected float for argument")
