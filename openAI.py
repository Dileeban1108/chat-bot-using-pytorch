import ollama

def get_response_from_gpt(prompt):
    """
    Offline AI response using Ollama (local model: SmolLM)
    """
    try:
        # Run chat using the small local model
        response = ollama.chat(
            model='tinyllama',  # <-- changed from 'mistral' to 'smollm'
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content'].strip()

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I'm having trouble processing that locally."
