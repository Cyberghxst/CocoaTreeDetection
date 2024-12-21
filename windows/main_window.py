from .base_window import BaseWindow
from customtkinter import CTkLabel, CTkButton, CTkImage
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2
import os

'''
Trick taken from: https://github.com/TomSchimansky/CustomTkinter/discussions/1099#discussioncomment-6507015
'''
itsc_icon = ImageTk.PhotoImage(file=os.path.join('assets', 'itsc_logo.png'))

'''
Variable that saves the YOLO model path.
'''
model_path = os.path.join('models', 'TRAIN_1_BEST.pt')

class App(BaseWindow):
    '''
    A class that represents the main window.
    '''
    def __init__(self):
        super().__init__(
            title='Detector de cacao con YOLO v8',
            width=640,
            height=640
        )
        
        # Set the YOLO model by path.
        self._model = YOLO(model=model_path)

        self._label = CTkLabel(master=self._window, text='')
        self.video_stream = cv2.VideoCapture(0) # Saves the video stream on the camera 0.

        # Set the video width and height.
        self.video_stream.set(cv2.CAP_PROP_FRAME_WIDTH, float(self.width))
        self.video_stream.set(cv2.CAP_PROP_FRAME_HEIGHT, float(self.height))

    def show(self):
        '''
        A function that shows the window.

        Arguments:
            This function does not take any arguments.

        Returns:
            This function is not supposed to return anything.
        '''
        self._window.title(self.title) # Set the title.
        
        self._window.geometry(f'{self.width}x{self.height}') # Set the width and height.
        self._window.resizable(False, False) # Marking the window as no-resizable.

        self._window.wm_iconbitmap() # Set the icon bitmap.
        self._window.iconphoto(False, itsc_icon) # Set the icon.

        # Bind a key to destroy the window.
        self._window.bind('<Escape>', lambda t: self._window.quit())

        self._label.pack() 
        self.open_camera()

        self._window.mainloop() # Show the window.

    def open_camera(self):
        _, frame = self.video_stream.read()
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)

        self._label.photo_image = photo_image
        self._label.configure(image=photo_image)

        self._label.after(10, self.open_camera)



        

        