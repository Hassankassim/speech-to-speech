import speech_recognition as sr
from openai import OpenAI

# Configure OpenAI API key (replace with your actual key)
client = OpenAI(api_key="YOUR_API_KEY")

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
            return ""

        except sr.RequestError as e:  # Corrected indentation
            print(f"Could not request results from Google Web Speech API; {e}")
            return ""

def interact_with_openai():
    while True:
        prompt = speech_to_text()  # Get prompt from speech recognition

        if prompt.lower() == 'quit':
            break

        print("You said:", prompt)

        # Send the prompt to OpenAI and get the response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or any other desired model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Adjust as needed
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Print the response to the console (including images when applicable)
        print("Response:", response.choices[0].message.content.strip())

        # If the response includes image URLs, display them
        if "data:image/" in response.choices[0].message.content:
            # (Implement image display logic here, e.g., using a web browser or image library)
            print("Response includes images! Implement image display logic here.")

if __name__ == "__main__":
    interact_with_openai()