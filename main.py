'''
from windows.main_window import App

window = App()
window.show()
'''

from utils.resize_image import resize_image
from utils.draw_box import draw_box
from ultralytics import YOLO
import cv2
import os

# Set up model and parameter
model = YOLO(os.path.join('models', 'TRAIN_1_BEST.pt'))
class_list = model.model.names
scale_show = 100

# Read Video
video = cv2.VideoCapture(0)

# Run Loop
while True:
    ret, frame = video.read()
    if ret:
        results = model.predict(frame)
        labeled_img = draw_box(frame, results[0], class_list)
        display_img = resize_image(labeled_img, scale_show)

        # Show Image
        cv2.imshow('Detector de cacao con YOLO v8', display_img)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Break the loop if not read
    else:
        break

# When everything done, release
video.release()

# Closes all the frames
cv2.destroyAllWindows()