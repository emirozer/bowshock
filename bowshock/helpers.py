import socket
import logging
import getpass
import datetime

def bowshock_logger():
    '''creates a logger obj'''
    # Pull the local ip and username for meaningful logging
    username = getpass.getuser()
    local_ip = socket.gethostbyname(socket.gethostname())
    # Set the logger
    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    extra_information = {'clientip': local_ip, 'user': username}
    logger = logging.getLogger('fake2db_logger')
    # --------------------
    return logger, extra_information


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
