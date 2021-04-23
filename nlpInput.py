import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

# nltk.download('punkt')
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stemming(word):
    return stemmer.stem(word.lower())

def bagOfWords(tokenizeSentence,allWords):
    tokenizedSent = [stemming(i) for i in tokenizeSentence]
    bag = np.zeros(len(allWords),dtype = np.float32)
    for idx,word in enumerate(allWords):
        if word in tokenizedSent:
            bag[idx] = 1.0
    return bag