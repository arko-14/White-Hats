import cv2
import pytesseract
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set path to the Tesseract executable (update with your path)
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Function to process frame and extract text
def detect_text_and_speak(frame):
    h, w, _ = frame.shape
    quadrants = {
        1: frame[0:h//2, 0:w//2],
        2: frame[0:h//2, w//2:w],
        3: frame[h//2:h, 0:w//2],
        4: frame[h//2:h, w//2:w]
    }
    
    # Iterate through each quadrant
    for q, roi in quadrants.items():
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)

        if text.strip():  # Check if there is non-empty text
            print(f"Detected Text in Quadrant {q}: {text}")
            engine.say(f"Text in quadrant {q}: {text}")
            engine.runAndWait()

# Start capturing video from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the frame
    cv2.imshow('Live Camera - Press Q to Quit', frame)

    # Detect and speak text from the current frame
    detect_text_and_speak(frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()

