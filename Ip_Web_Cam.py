import cv2
from tkinter import messagebox

class CameraCapture():
    def __init__(self, url):
        ''' ID for camera '''
        self.url = url
        self.capture = cv2.VideoCapture(url)  # Set the ID and open camera

    def open_camera(self):
        ''' Preventing Failures '''
        if not self.capture.isOpened():  # Check if the camera opened successfully
            print("Error: Could not open camera.")
            messagebox.showerror(message="Error: Could not open camera", title="ERROR #CC0")
            exit()

    def capture_frame(self):
        ''' Capture a single frame '''
        ret, frame = self.capture.read()
        
        ''' Preventing Failures '''
        if not ret:
            print("Error: Could not capture frame.")
            messagebox.showerror(message="Error: Could not capture frame", title="ERROR #CF0")
            exit()
        return frame

    def save_frame(self, path):
        ''' Save the captured frame as an image in a path '''
        cv2.imwrite(path, self.capture_frame())

    def show_success_message(self):
        ''' Informing if the capture and saving was successful '''
        messagebox.showinfo(message="Capture successful")

    def release_camera(self):
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_url = 'http://192.168.0.16:8080/shot.jpg'

    camera_capture = CameraCapture(camera_url)
    camera_capture.open_camera()

    save_path = "path/image.jpg"
    camera_capture.save_frame(save_path)
    camera_capture.show_success_message()
    camera_capture.release_camera()
