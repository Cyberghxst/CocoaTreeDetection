from utils.export_models import export_last_model
from ultralytics import YOLO
import os


# Set the video name with extension.
image_name: str | list[str] = 'IMG_20241126_161413.jpg'

# Export the last model as NCNN and save the path.
last_model_path = export_last_model()
print(f'{last_model_path} ha sido seleccionado como el ultimo modelo entrenado.')

# Load the YOLOv8 model
model = YOLO(last_model_path)

# Define a function to predict images to avoid "repeating yourself".
def predict(dir: str):
    # Set the video path.
    image_path = os.path.join(os.getcwd(), 'photo_samples', dir)

    # Make the prediction.
    model.predict(
        source=image_path,
        task='detect',
        show=True,
        save=True
    )

# Predict images based on the variable type.
if isinstance(image_name, str):
    predict(image_name)
elif isinstance(image_name, list) and all(isinstance(name, str) for name in image_name):
    for name in image_name:
        predict(name)