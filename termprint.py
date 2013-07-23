from termcolor import *

keys = {
    "INFO": "green", 
    "WARNING": "yellow", 
    "ERROR": "red"
}

def termprint(logtype, data, return_text=False):
    """
    Print log output in pretty formats
    """
    if return_text:
        if not logtype in keys:
            s = colored(data, "white", attrs=["bold"])
        else:
            s = colored(data, keys.get(logtype, "white"), attrs=['bold'])
        return s
    else:
        if not logtype in keys:
            print colored(data, "white", attrs=["bold"])
        else:
            print colored(data, keys.get(logtype, "white"), attrs=['bold'])


