'''
from utils.export_models import export_last_model
from ultralytics import YOLO
import cv2, os

# Set the video name with extension.
video_name = 'video_prueba.mp4'

# Set the video path.
video_path = os.path.join(os.getcwd(), 'video_samples', video_name)

# Export the last model as NCNN and save the path.
last_model_path = export_last_model()
print(f'{last_model_path} ha sido seleccionado como el ultimo modelo entrenado.')

# Load the YOLOv8 model
model = YOLO(last_model_path)

# Start the prediction using the video as source.
results = model.predict(
    source=video_path,
    task='detect',
    show=True,
    stream=True
)
'''

from utils.export_models import export_last_model
from ultralytics import YOLO
from PIL import Image
import cv2, os

# Set the video name with extension.
video_name = 'video_prueba.mp4'

# Set the video path.
video_path = os.path.join(os.getcwd(), 'video_samples', video_name)

# Export the last model as NCNN and save the path.
last_model_path = export_last_model()
print(f'{last_model_path} ha sido seleccionado como el ultimo modelo entrenado.')

# Load the YOLOv8 model
model = YOLO(last_model_path)

def convert_avi_to_mp4(input_path, output_path):
    """Convert an AVI video file to MP4 format using OpenCV."""
    cap = cv2.VideoCapture(input_path)
    
    # Get the video's properties (frame width, height, and FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object for MP4 output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Read and write each frame to the new video file
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        image = Image.fromarray(frame)

        results = model.predict(
            source=image,
            task='detect',
            stream=True,
            device='0'
        )
    
        for result in results:
            annotation = result.plot()
            out.write(annotation)
    
    # Release resources
    cap.release()
    out.release()
    print(f"Video saved as {output_path}")

convert_avi_to_mp4(
    input_path=video_path,
    output_path=os.path.join(os.getcwd(), 'runs', video_name)
)