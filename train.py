import json
import torch.nn as nn
from torch.nn import CrossEntropyLoss

from nltk_utils import tokenize, stem, bag_of_words, resource_path
from nltk import interpret_sents
import numpy as np

import torch
from torch.utils.data import Dataset, DataLoader

from model import ChatClassifier

# open the intents.json file
json_path = resource_path("intents.json")
with open(json_path, "r") as f:
    intents = json.load(f)

# print(intents)

# Creating empty lists
all_words = []
tags = []
patterns_with_tag = []

# loop through the intents
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    # loop through the patterns
    for pattern in intent['patterns']:

        # tokenize the pattern
        tokenized_pattern = tokenize(pattern)

        # Add to the all_words list
        all_words.extend(tokenized_pattern)

        # Add the tokenized_pattern with the particular tag to the patterns_with_tag list
        patterns_with_tag.append((tokenized_pattern, tag))

# Initialize a list with ignoring words
ignore_words = ['?', '!', '.', ':']

# Only get words remocing the ignore_words
all_words = [stem(w) for w in all_words if w not in ignore_words]

# Only get unique words and sort them
all_words = sorted(set(all_words))

# print(all_words)

X_train = []
y_train = []

for pattern, tag in patterns_with_tag:
    bag = bag_of_words(pattern, all_words)
    X_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)

# Convert to the numpy array
X_train = np.array(X_train)
y_train = np.array(y_train)

# print(X_train[0].shape)

# Create a custom dataset
class ChatBotDataset(Dataset):
    def __init__(self):
        super().__init__()
        self.x_data = X_train
        self.y_data = y_train
        self.n_samples = len(X_train)

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

# Creating a model
dataset = ChatBotDataset()

# Setting up the hyperparameters
num_workers = 0
batch_size = 8
input_size = len(bag)
hidden_size = 16
output_size = len(tags)
lr = 0.001
epochs = 1000



# Create the dataloader
train_loader = DataLoader(
    dataset = dataset,
    batch_size = batch_size,
    num_workers = num_workers,
    shuffle = True
)

model = ChatClassifier(input_size, hidden_size, output_size)
# print(list(model.parameters()))
criterion = nn.CrossEntropyLoss()
optimizer =  torch.optim.Adam(model.parameters(), lr=lr)

for epoch in range(epochs):
    model.train()
    for (X, y) in train_loader:
        # do the forward pass
        y_pred = model(X)

        # calculate the loss
        loss = criterion(y_pred, y)

        # optimizer zero grad
        optimizer.zero_grad()

        # loss backward
        loss.backward()

        # optimizer step
        optimizer.step()

    # print out whats happenin'
    print(f"ecpoc : {epoch+1}/{epochs} | loss : {loss.item(): .4f}")

print(f"total loss : {loss.item() : .4f}")

save_path = 'saved_model.pth'

data = {
    "model_state" : model.state_dict(),
    "input_size" : input_size,
    "output_size" : output_size,
    "hidden_size" : hidden_size,
    "all_words" : all_words,
    "tags" : tags
}
torch.save(data,save_path)
print(f'trianing complete, model saved in the {save_path}')