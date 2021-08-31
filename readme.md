Stage functions
===============

Splitting the program into stages that can be stopped and started again can be useful

One requirement for this system however is to allow for functions to call other prerequisite functions which would need to run first

The implementation has a Metadata class running along side of it that tracks which stages/ functions have been completed and which ones have not. This progress is saved to a metadata json which saves the information

How to define a stage function
==============================

```
@stage(prerequisite_function, prerequisite_function, ...)
def some_stage():
    #Add anything the stage needs to do here
    functionality()
```

The @stage decorator (see decorators.py) marks the function as a stage to be tracked. It can be passed prerequisite functions as parameters which will run before the program if they haven't run already

How to call a stage function
============================
```
some_stage(metadata)
```
A stage can be called as a normal function but must be passed the metadata class that runs throughout the program

```
some_state(metadata, True)
```
The option to force a specific stage to run again is also possible in this implementation by passing "True" as a second parameter