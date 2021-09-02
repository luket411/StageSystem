def stage(*prerequisites):
    def decorator_main(stage_function):
        def wrapper(metadata, override=False):

            for prerequisite_function in prerequisites:
                prerequisite_function(metadata)

            if stage_function.__name__ in metadata.completedStages and not override:
                return

            val = stage_function()
            metadata.completedStages.append(stage_function.__name__)
            return val
        return wrapper
    return decorator_main


def conditionalStage(condition_function, *prerequisites):
    def decorator_main(stage_function):
        def wrapper(metadata, override=False):

            for prerequisite_function in prerequisites:
                prerequisite_function(metadata)

            if stage_function.__name__ in metadata.completedStages and not override:
                return
            elif not condition_function():
                raise Exception(f"Condition '{condition_function.__name__}' not met for function '{stage_function.__name__}'")

            val = stage_function()
            metadata.completedStages.append(stage_function.__name__)
            return val
        return wrapper
    return decorator_main


def checkStage(check_function, *prerequisites):
    def decorator_main(stage_function):
        def wrapper(metadata, override=False):
            
            for prerequisite_function in prerequisites:
                prerequisite_function(metadata)

            if stage_function.__name__ in metadata.completedStages and not override and not check_function():
                return
            
            val = stage_function()
            metadata.completedStages.append(stage_function.__name__)
            return val
        return wrapper
    return decorator_main
