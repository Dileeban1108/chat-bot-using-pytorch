import nltk
from nltk.corpus import words
import numpy as np
# nltk.download('punkt_tab')
from nltk.stem.porter import  PorterStemmer
stemmer = PorterStemmer()

# Splitting a text in to smaller units
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# Remove all the suffixes to make a word to the root or stem format
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    """
    tokanized_sentence = ["hello", "how", "are", "you"]
    all_words = ["hi", "hello", "bye", "thankyou", "you", "how", "cool"]
    bag =       [ 0  ,   1,       0,       0,        1,      1,      0  ]

    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    # Initialize a zero vector
    bag = np.zeros(len(all_words), dtype=np.float32)\

    # Check whether tokeninzed words are in the all words
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1 # set 1 if true

    return bag

# tokenize_sentence = tokenize("hello world this is my first project")
# stem_word = stem("hello ran running")
#
# print(tokenize_sentence)
# print(stem_word)

# tokanized_sentence = ["hello", "how", "are", "you"]
# all_words = ["hi", "hello", "bye", "thankyou", "you", "how", "cool"]
# print(bag_of_words(tokanized_sentence, all_words))



