def stage(*prerequisites):
    def stagemain(func):
        def wrapper(metadata, override=False):

            for prerequisite_function in prerequisites:
                prerequisite_function(metadata)
                
            if func.__name__ in metadata.completedStages and not override:
                return

            val = func()
            metadata.completedStages.append(func.__name__)
            return val
        return wrapper
    return stagemain


def conditionalStage(condition_function, *prerequisites):
    def stagemain(func):
        def wrapper(metadata, override=False):

            for prerequisite_function in prerequisites:
                prerequisite_function(metadata)

            if func.__name__ in metadata.completedStages and not override:
                return
            elif not condition_function():
                raise Exception(f"Condition '{condition_function.__name__}' not met for function '{func.__name__}'")

            val = func()
            metadata.completedStages.append(func.__name__)
            return val
        return wrapper
    return stagemain