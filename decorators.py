def stage(*pre_requesits):
    def stagemain(func):
        def wrapper(metadata, override=False):
            for pre_req in pre_requesits:
                pre_req(metadata)
            if func.__name__ in metadata.completedStages and not override:
                return
            val = None
            val = func()
            metadata.completedStages.append(func.__name__)
            return val
        return wrapper
    return stagemain
