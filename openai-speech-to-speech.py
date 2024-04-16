import speech_recognition as sr
from openai import OpenAI
import pyttsx3  # Text-to-speech library

from elevenlabs import play
from elevenlabs.client import ElevenLabs

client_elevenlab = ElevenLabs(
  api_key="a2e17d592ade41f35adeac8ae53d8c2b", # Defaults to ELEVEN_API_KEY
)


# Configure OpenAI API key (replace with your actual key)
client = OpenAI(api_key="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")

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, timeout=5)

        try:
            text = recognizer.recognize_google(audio_data)
            return text

        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
            return ""  # Corrected indentation and removed extra double quotes

        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            return ""

def elevenlabs_speech(text):
   audio = client_elevenlab.generate(
      text=text,
       voice="Rachel",
       model="eleven_multilingual_v2"
    )
   play(audio)
 

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def interact_with_openai():
    while True:
        prompt = speech_to_text()

        if prompt.lower() == 'quit':
            break

        print("You said:", prompt)

        # Send the prompt to OpenAI and get the response
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Or any other desired model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,  # Adjust as needed
            n=1,
            stop=None,
            temperature=0.7,
        )

        print("Response:", response.choices[0].message.content.strip())
        #speak_text(response.choices[0].message.content.strip())  # Speak the response
        elevenlabs_speech(response.choices[0].message.content.strip())
        
if __name__ == "__main__":
    interact_with_openai()