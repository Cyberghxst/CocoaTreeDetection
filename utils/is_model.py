def is_model(path: str):
    '''
    Check whether the given path ends with '.pt'.
    If so, returns 'True', otherwise 'False'.

    Arguments:
        path (str): The model path.

    Returns:
        bool: Whether the path is a valid model path.
    '''
    return isinstance(path, str) and path.endswith('.pt')