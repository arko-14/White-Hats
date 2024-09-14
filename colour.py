import cv2
import numpy as np
import pyttsx3
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define the color ranges in HSV
color_ranges = {
    'red': ([0, 120, 70], [10, 255, 255]),
    'green': ([36, 25, 25], [86, 255, 255]),
    'yellow': ([15, 150, 150], [35, 255, 255])
}

# Initialize the webcam
cap = cv2.VideoCapture(0)

# A flag to avoid repeating the speech for the same color continuously
last_spoken_color = None

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    detected_color = None

    # Check each color range
    for color, (lower, upper) in color_ranges.items():
        # Create a mask for the color
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)

        # Check if the color is detected
        if cv2.countNonZero(mask) > 0:
            detected_color = color
            break

    # Speak the detected color if it's different from the last spoken color
    if detected_color and detected_color != last_spoken_color:
        if detected_color == 'red':
            print("Red Stop")
            engine.say("Red Stop")
        elif detected_color == 'green':
            print("Green Go")
            engine.say("Green Go")
        elif detected_color == 'yellow':
            print("Yellow Be ready")
            engine.say("Yellow Be ready")

        engine.runAndWait()  # Execute the speech
        last_spoken_color = detected_color  # Update the last spoken color

        # Add a delay after speaking (2 seconds in this case)
        time.sleep(0.5)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
