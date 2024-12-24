import os

def fetch_last_model():
    '''
    This function fetches the last trained model
    from the models directory.

    Arguments:
        This function is not intended to receive any arguments.

    Returns:
        (str): The path string of the last trained model.
    '''
    
    models_path = os.path.join(os.getcwd(), 'models')
    models = list(filter(lambda file: file.endswith('.pt'), os.listdir(models_path)))

    if len(models) == 0:
        raise Exception('No models found in "models" path!')

    sorted_models = sorted(models, reverse=True)
    last_model = sorted_models[0]

    return os.path.join(os.getcwd(), 'models', last_model)