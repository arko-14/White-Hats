import cv2
import pytesseract
import pyttsx3

# Set the path to Tesseract executable (update this with your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to announce the detected text and its position
def announce_text_and_position(text, position):
    if position == "left":
        engine.say(f"The text '{text}' is on the left.")
    elif position == "right":
        engine.say(f"The text '{text}' is on the right.")
    else:
        engine.say(f"The text '{text}' is in the center.")
    engine.runAndWait()

# Function to determine which side the text is located in the frame
def determine_position(x, frame_width):
    if x < frame_width / 3:
        return "left"
    elif x > 2 * frame_width / 3:
        return "right"
    else:
        return "center"

# Initialize webcam
cap = cv2.VideoCapture(0)

# Check if webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Get the dimensions of the frame
    frame_height, frame_width, _ = frame.shape

    # Convert the frame to grayscale for better OCR detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the frame to detect text
    text_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    # Loop through each detected text block
    for i in range(len(text_data['text'])):
        if int(text_data['conf'][i]) > 60:  # Confidence threshold to ensure good quality text
            # Get the position and dimensions of the detected text
            x, y, w, h = text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i]
            detected_text = text_data['text'][i].strip()

            if detected_text:  # Only process non-empty text
                # Draw a rectangle around the detected text
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Display the detected text on the frame
                cv2.putText(frame, detected_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Determine if the text is on the left, right, or center
                position = determine_position(x, frame_width)

                # Announce the text and its position
                announce_text_and_position(detected_text, position)

    # Show the frame with detected text boxes
    cv2.imshow('Text Detection', frame)

    # Press 'q' to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
