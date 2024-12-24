from .base_window import BaseWindow
from .error_dialog import ErrorDialog
from customtkinter import CTkLabel, CTkButton, RIGHT, LEFT
from utils.fetch_last_model import fetch_last_model
from picamera2 import Picamera2
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2
import os

'''
Trick taken from: https://github.com/TomSchimansky/CustomTkinter/discussions/1099#discussioncomment-6507015
'''
itsc_icon = ImageTk.PhotoImage(file=os.path.join('assets', 'itsc_logo.png'))

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

        # Fetch the path of the last trained model.
        self._model_path = fetch_last_model()
        
        # Set the YOLO model by path.
        self._model = YOLO(model=self._model_path)

        # Creating a label to load the frames to it.
        self._label = CTkLabel(master=self._window, text='')

        # Assign the PiCamera2 to a class attribute.
        self.camera = Picamera2()
        self.camera.configure(
            self.camera.create_video_configuration(
                main={
                    'format': 'XRGB8888',
                    'size': (self.width, self.height)
                }
            )
        )

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

        # Show the label.
        self._label.pack()

        self._shot_button.pack(side=LEFT, padx=20, pady=50) # Show the "show" button.
        self._exit_button.pack(side=RIGHT, padx=20, pady=50) # Show the "exit" button.

        # Opens the camera.
        self.open_camera()

        # Show the window.
        self._window.mainloop()

    def open_camera(self):
        # Starts the camera.
        self.camera.start()

        while True:
            # RAW image captured by PiCamera.
            raw_image = self.camera.capture_array()

            # Coverting the raw image to an actual image.
            captured_image = Image.fromarray(raw_image)

            # Converting the captured image to a photo image.
            photo_image = ImageTk.PhotoImage(image=captured_image)

            # Making the predictions with the loaded YOLO model.
            # prediction = self._model.predict(photo_image, imgsz=640, conf=0.80)

            # Drawing the predicted boxes.
            # annotation = prediction[0].plot()

            # Show the predicted frame.
            cv2.imshow(self.title, raw_image)

            '''
            if cv2.waitKey(1) == ord("q"):
                cv2.imwrite("test_frame.png", raw_image)
                break
            '''

            # Save the current frame when "c" is pressed.
            if cv2.waitKey(1) == ord('c') and raw_image.all() != None:
                self.save_frame(raw_image)

            # Checking if the camera is sending images.
            if cv2.waitKey(1) != ord('q') and raw_image.all() == None:
                # Creating an error dialog.
                error_dialog = ErrorDialog(
                    title='Error de Camara',
                    error_message='La camara no envio imagen, envio "None" lo cual no deberia pasar.',
                    master=self._window
                )

                # Showing the error dialog.
                error_dialog.show()

                # Break the loop. (end the program)
                break

    def save_frame(self, frame: any) -> None:
        '''
        Saves a frame to the "shots" folder.

        Arguments:
            This function is not intended to receive arguments.

        Returns:
            (None): This function is not intended to return anything.
        '''
        # Save the shots directory.
        shots_dir = os.path.join(os.getcwd(), 'shots')

        # Creating the shots directory if it does not exists.
        if os.path.exists(shots_dir) == False:
            os.mkdir(shots_dir)

        # Save the file names of the "shots" dir in a list.
        files = list(os.listdir(shots_dir))

        # Get the amount of file inside the folder.
        flength = len(files)

        # Write the given frame into the "shots" folder.
        cv2.imwrite(
            filename=os.path.join(shots_dir, f'shot_{flength}.jpg'),
            img=frame
        )



        

        