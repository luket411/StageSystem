from os import path as ospath, makedirs
from shutil import rmtree

from constants import temp_path

def clear_temp_folder():
    if ospath.exists(temp_path):
        rmtree(temp_path)
    makedirs(temp_path)

if __name__ == "__main__":
    clear_temp_folder()