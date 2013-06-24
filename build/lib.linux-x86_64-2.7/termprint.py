from termcolor import *

keys = {
    "INFO": "green", 
    "WARNING": "yellow", 
    "ERROR": "red"
}

def termprint(logtype, data):
    """
    Print log output in pretty formats
    """
    if not logtype in keys:
        print colored(data, "white", attrs=["bold"])
    else:
        print colored(data, keys.get(logtype, "white"), attrs=['bold'])


