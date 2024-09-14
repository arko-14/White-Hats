import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize MediaPipe drawing module
mp_drawing = mp.solutions.drawing_utils


gesture_mapping = {
    "thumbs_up": "A",
    "fist": "B",
    "open_hand": "C",
    
}

def recognize_gesture(landmarks):
 
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP].y
    
    if thumb_tip < index_tip < middle_tip < ring_tip < pinky_tip:
        return "thumbs_up"  # Example gesture
    elif index_tip < thumb_tip and middle_tip < thumb_tip and ring_tip < thumb_tip:
        return "fist"  # Example gesture
    elif index_tip > thumb_tip and middle_tip > thumb_tip and ring_tip > thumb_tip:
        return "open_hand" 
    
    return None

# Start video capture
cap = cv2.VideoCapture(0)

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
            
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if gesture_text:
        cv2.putText(frame, f"Detected Gesture: {gesture_text}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

   
    cv2.imshow('Sign Language Recognition', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()
