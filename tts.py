# tts.py
import pyttsx3

engine = pyttsx3.init()

def speak(text: str) -> None:
    """
    Converts text to speech.

    Parameters:
    text (str): The text to speak.

    Returns:
    None
    """
    engine.say(text)
    engine.runAndWait()
