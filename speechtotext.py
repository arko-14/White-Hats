import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as source for input
with sr.Microphone() as source:
    print("Please say something:")
    
    # Adjust the recognizer sensitivity to ambient noise
    recognizer.adjust_for_ambient_noise(source)
    
    # Listen for the user's input
    audio = recognizer.listen(source)

    try:
        # Convert speech to text using Google's speech recognition API
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError:
        print("Could not request results from the service")
