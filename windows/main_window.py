from .base_window import BaseWindow
from customtkinter import CTkLabel, CTkButton, RIGHT, LEFT
from utils.is_model import is_model
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

# Checking whether the given model path is valid.
if not is_model(model_path):
    raise Exception('The given model path is not valid.')

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

        # Creating a button to make shots.
        self._shot_button = CTkButton(
            master=self._window,
            text='Capturar',
            fg_color='green',
            hover_color='#228B22'
        )

        # Creating a button to exit the program.
        self._exit_button = CTkButton(
            master=self._window,
            text='Cerrar',
            fg_color='#D22B2B',
            hover_color='#D2042D',
            command=self._window.quit
        )

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

        self._label.pack() # Show the label.

        # self._shot_button.place()
        self._shot_button.pack(side=LEFT, padx=20, pady=50) # Show the "show" button.
        self._exit_button.pack(side=RIGHT, padx=20, pady=50) # Show the "exit" button.

        self.open_camera() # Opens the camera.

        self._window.mainloop() # Show the window.

    def open_camera(self):
        while True:
            _, frame = self.video_stream.read()
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            # photo_image = ImageTk.PhotoImage(image=captured_image)

            prediction = self._model.predict(captured_image, imgsz=640, conf=0.80)
            annotation = prediction[0].plot(img=captured_image)

            # self._label.photo_image = annotation
            self._label.configure(image=annotation)

            # self._label.after(10, self.open_camera)

    def destroy_camera(self):
        '''
        Destroys the video stream.

        Arguments:
            This function is not intended to receive arguments.

        Returns:
            This function is not intended to return anything.
        '''
        self.video_stream.release()



        

        