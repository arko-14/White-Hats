import cv2
import mediapipe as mp
import numpy as np
import pyttsx3  # Import pyttsx3 for text-to-speech

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the engine speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize MediaPipe drawing module
mp_drawing = mp.solutions.drawing_utils

# Gesture mapping
gesture_mapping = {
    "thumbs_up": "A",
     "open_hand": "D",
    "fist": "C",
   
    "victory_sign": "F"
}

# Function to recognize hand gestures based on landmarks
def recognize_gesture(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].x, landmarks[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x, landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].x, landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP].x, landmarks[mp_hands.HandLandmark.PINKY_TIP].y

    index_mcp = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP].x, landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x, landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y

    if thumb_tip[1] < index_tip[1] < middle_tip[1] < ring_tip[1] < pinky_tip[1]:
        return "thumbs_up"
    elif index_tip[1] < thumb_tip[1] and middle_tip[1] < thumb_tip[1] and ring_tip[1] < thumb_tip[1]:
        return "open_hand"
    elif index_tip[1] > thumb_tip[1] and middle_tip[1] > thumb_tip[1] and ring_tip[1] > thumb_tip[1]:
        return "fist"
    elif np.linalg.norm(np.array(thumb_tip) - np.array(index_tip)) < 0.05 and middle_tip[1] > index_mcp[1] and ring_tip[1] > middle_mcp[1]:
        return "ok_sign"
    elif index_tip[1] < middle_tip[1] < ring_tip[1] and pinky_tip[1] > ring_tip[1] and np.linalg.norm(np.array(index_tip) - np.array(middle_tip)) < 0.05:
        return "peace_sign"
    elif index_tip[1] < middle_tip[1] and ring_tip[1] > middle_tip[1] and pinky_tip[1] > ring_tip[1]:
        return "victory_sign"

    return None

# Start video capture
cap = cv2.VideoCapture(0)

last_gesture = ""

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    gesture_text = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            gesture = recognize_gesture(hand_landmarks.landmark)

            if gesture:
                gesture_text = gesture_mapping.get(gesture, "")
                if gesture_text and gesture_text != last_gesture:  # Speak only if gesture has changed
                    speak(gesture_text)
                    last_gesture = gesture_text

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if gesture_text:
        cv2.putText(frame, f"Detected Gesture: {gesture_text}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Sign Language Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()
