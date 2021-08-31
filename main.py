from Metadata import MetaData
from decorators import stage
'''

'''

temp_path = ".stages"

@stage()
def func1():
    print("Ran func1")

@stage(func1)
def func2():
    print("Ran func2")

@stage(func2)
def func3():
    print("Ran func3")



if __name__ == "__main__":
    metadata = MetaData(temp_path)
    func3(metadata, True)
    metadata.save()
