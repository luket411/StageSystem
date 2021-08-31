from os import path as ospath, remove
from constants import FLAG

if __name__ == "__main__":
    if ospath.exists(FLAG):
        remove(FLAG)
    else:
        with open(FLAG, "w") as flag:
            flag.write("flag")