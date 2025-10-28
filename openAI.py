import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response_from_gpt(prompt):
    """
    Sends the user message to OpenAI's GPT model and returns the response.
    """
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
        )
        return completion.choices[0].message["content"].strip()

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I'm having trouble connecting to the AI service right now."

print(get_response_from_gpt("What is the weather today?"))
