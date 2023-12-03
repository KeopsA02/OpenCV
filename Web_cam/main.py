import cv2

# Open the camera
cap = cv2.VideoCapture(0)  # The argument 0 indicates the default camera (you can change it if you have multiple cameras)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error opening the camera")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Camera', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
