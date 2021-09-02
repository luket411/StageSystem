from Metadata import MetaData
from decorators import *
from conditions import check_for_flag
from constants import temp_path


@stage()
def func1():
    print("Ran func1")


@checkStage(check_for_flag, func1)
def func2():
    print("Ran func2")


@stage(func2)
def func3():
    print("Ran func3")


if __name__ == "__main__":
    metadata = MetaData(temp_path)
    try:
        func3(metadata, True)
    except Exception as err:
        raise err
    finally:
        metadata.save()
