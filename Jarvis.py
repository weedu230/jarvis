# Import Libraries
import pyttsx3
import speech_recognition as sr
import wikipedia
import sys
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()
# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Create a Listener Function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except:
            print("Could not understand your command.")
            return None
   

# Add Functions for Specific Tasks
# Get Current Time
def tell_time():
    now = datetime.datetime.now().strftime("%I:%M:%S %p")  # Added seconds (%S)
    speak(f"The time is {now}")
    print(f"The time is {now}")
# Search Wikipedia
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia...")
        speak(result)
    except:
        speak("Sorry, I couldn't find anything on Wikipedia.")

# Quit the program
def close_program():
    speak("Allah Hafiz!")
    sys.exit()       

#  Main
def main():
    speak("Salam I'm Hussain's Assistent How can i assist you ?")
    while True:
        command = listen()
        if command:
            if "wikipedia" in command:
                search_wikipedia(command.replace("wikipedia", ""))
            elif "time" in command:
                tell_time()
            elif "quit" in command or "exit" in command:
                close_program()
            else:
                speak("I did not understand. Please try again.")

# Running the Program
if __name__ == "__main__":
    main()
