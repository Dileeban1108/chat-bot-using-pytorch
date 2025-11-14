import nltk
import numpy as np
import os, sys

# --- START: CRITICAL DEPLOYMENT FIX ---
# Check and download necessary NLTK data (punkt for tokenization)
# This prevents crashes when the application initializes on a fresh environment.
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')
# --- END: CRITICAL DEPLOYMENT FIX ---

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# Splitting a text in to smaller units
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# Remove all the suffixes to make a word to the root or stem format
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    # Initialize a zero vector
    bag = np.zeros(len(all_words), dtype=np.float32)

    # Check whether tokeninzed words are in the all words
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1 # set 1 if true

    return bag

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)