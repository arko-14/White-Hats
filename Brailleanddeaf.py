import cv2
import pytesseract
import time
import pyttsx3
import serial

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize serial communication with Arduino
ser = serial.Serial('COM9', 9600)  # Replace 'COM9' with your Arduino port
time.sleep(0.5)  # Wait for the connection to establish

# Define the Braille binary representations for letters and numbers
braileMap = {
    'A': '100000', 'B': '110000', 'C': '100100', 'D': '100110', 'E': '100010',
    'F': '110100', 'G': '110110', 'H': '110010', 'I': '010100', 'J': '010110',
    'K': '101000', 'L': '111000', 'M': '101100', 'N': '101110', 'O': '101010',
    'P': '111100', 'Q': '111110', 'R': '111010', 'S': '011100', 'T': '011110',
    'U': '111001', 'W': '010111', 'X': '101101', 'Y': '101111', 'Z': '101011'
}

braille_numbers = {
    '0': '100110', '1': '100000', '2': '110000', '3': '100100', '4': '100110',
    '5': '100010', '6': '110100', '7': '110110', '8': '110010', '9': '100100'
}

# Function to send letter to Arduino via serial
def send_letter(letter):
    letter = letter.upper()  # Convert to uppercase to match the Braille map
    if letter in braileMap:
        binary_code = braileMap[letter]
        ser.write(binary_code.encode())  # Send binary data to Arduino
        print(f"Sent {letter}: {binary_code}")
    else:
        print("Invalid letter")

# Function to send number to Arduino via serial
def send_number(number):
    if number in braille_numbers:
        number_sign = '001111'  # Send number sign first
        ser.write(number_sign.encode())
        print(f"Sent number sign: {number_sign}")
        time.sleep(0.5)  # Short delay for the number sign
        binary_number = braille_numbers[number]
        ser.write(binary_number.encode())
        print(f"Sent {number}: {binary_number}")
    else:
        print("Invalid number")

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

    # Convert the frame to grayscale for better text detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR to detect text from the frame
    text = pytesseract.image_to_string(gray)

    if text.strip():  # If any text is detected
        print("Text detected:")
        print(text)
        
        # Speak the detected text
        engine.say(text)
        engine.runAndWait()

        # Process each character of the detected text
        for char in text.strip():
            if char.isalpha():  # Check if it's a letter
                send_letter(char)
            elif char.isdigit():  # Check if it's a number
                send_number(char)
            else:
                print(f"Skipped: {char}")  # Ignore spaces, punctuation, etc.

            time.sleep(1)  # Delay between sending each character to Arduino

        # Wait for 10 seconds before detecting the next text
        time.sleep(10)

    # Display the frame (optional, for visual confirmation)
    cv2.imshow('Captured Frame', frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()

   







