from ultralytics import YOLO
from utils.fetch_last_model import fetch_last_model
import os

def export_last_model() -> str:
    '''
    This function exports the last YOLO
    model to NCNN format is this does not exists.

    Arguments:
        This function is not supposed to receive any arguments.

    Returns:
        (str): The path of the exported "NCNN" model.
    '''
    # Getting the last ".pt" model path.
    last_pt_model_path = fetch_last_model()

    # Creating the "NCNN" model path from the previous path.
    last_ncnn_model_path = last_pt_model_path.replace('.pt', '_ncnn_model')

    # If the "NCNN" path does not exist, we need to export the model.
    if os.path.exists(last_ncnn_model_path) == False:
        raw_model = YOLO(last_pt_model_path)
        raw_model.export(format='ncnn')

    # Returning the "NCNN" model path as it now exists.
    return last_ncnn_model_path