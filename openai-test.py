from openai import OpenAI

# Configure API key (replace with your actual key)
client = OpenAI(api_key="my-key")

def interact_with_openai():
    while True:
        prompt = input("Enter your prompt (or 'quit' to exit): ")

        if prompt.lower() == 'quit':
            break

        # Send the prompt to OpenAI and get the response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or any other desired model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,  # Adjust as needed
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Print the response to the console (corrected line)
        print("Response:", response.choices[0].message.content.strip())

if __name__ == "__main__":
    interact_with_openai()