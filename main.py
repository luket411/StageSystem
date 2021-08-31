from Metadata import MetaData
from decorators import stage

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

'''
@stage(prerequesit_function, prerequesit_function, ...)
def a_stage():
    #Add anything the stage needs to do here
    stage_functionality()
'''


if __name__ == "__main__":
    metadata = MetaData(temp_path)
    func3(metadata, True)  # Call any stage function with the metadata param and the True param. This will force the stage function to run even if it hasn't been run before
    metadata.save()
