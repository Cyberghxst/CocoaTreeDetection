from windows.main_window import App

app = App()

if __name__ == '__main__':
    app.show()


'''
from picamera2 import Picamera2
import cv2

picam2 = Picamera2()

picam2.configure(picam2.create_video_configuration(
    main={"format": 'XRGB8888', "size": (300, 300)}))
picam2.start()

while True:
    image = picam2.capture_array()

    cv2.imshow("Frame", image)

    if cv2.waitKey(1) == ord("q"):
        cv2.imwrite("test_frame.png", image)
        break

cv2.destroyAllWindows()
'''