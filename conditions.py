from os import path as ospath
from constants import FLAG

def check_for_flag():
    return ospath.exists(FLAG)
