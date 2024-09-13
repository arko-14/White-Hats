import cv2
import pytesseract
import time
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize camera capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture image.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform text detection using pytesseract
    text = pytesseract.image_to_string(gray)

    if text.strip():
        print("Text detected:")
        print(text)
        
        # Speak the detected text
        engine.say(text)
        engine.runAndWait()

        
        time.sleep(10)

   
    cv2.imshow('Captured Frame', frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
