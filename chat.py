import torch, json, random

# Ensure resource_path is imported
from model import ChatClassifier
from nltk_utils import tokenize, bag_of_words, resource_path

bot_name = "dileeb😊"

json_path = resource_path("intents.json")
with open(json_path, "r") as f:
    intents = json.load(f)

# --- START: MODEL PATH FIX ---
# Use resource_path for the model file for reliable loading on Render
save_path = resource_path("saved_model.pth")

# IMPORTANT: Ensure 'saved_model.pth' is in your Git repository and pushed to Render!
data=torch.load(save_path, map_location=torch.device('cpu')) # Add map_location for CPU deployment
# --- END: MODEL PATH FIX ---

model_state = data['model_state']
input_size = data["input_size"]
output_size = data["output_size"]
hidden_size = data["hidden_size"]
all_words = data['all_words']
tags = data['tags']


model = ChatClassifier(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    predicted_probs = torch.softmax(output, dim=1)
    predicted_probs = predicted_probs[0][predicted.item()]

    if predicted_probs > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])

    return "I do not understand...😰"