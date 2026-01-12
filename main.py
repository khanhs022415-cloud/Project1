import nltk
import re
import string
#Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

#input text
text = ("My name is Pham Nam Khanh. I'm 20 years old. I am a student of Huflit university. My favorite sport is swimming. I usually hang out with my friends after school for swimming. After swimming we often go to the cafe to have some drinks and talk about our lives. I love swimming because it helps me relax and stay healthy. Swimming is always fun and exciting. I hope to become a professional swimmer in the future."
        "My friend's name is Yorozu Baku. Code no.7. He's a sleep agent for C.O.D.E. He has the ability to become Kamen Rider Zeztz when fighting the dream intruders, Nightmares. Baku is a laid-back and carefree individual who often appears lazy and unmotivated. However, when it comes to protecting others and fighting against the Nightmares, he becomes serious and determined. Despite his relaxed demeanor, Baku is a skilled fighter and strategist, using his powers to manipulate dreams and create illusions to outsmart his opponents. ")
print("Original Text:\n", text)
print("-" * 60)

#tokenization
tokens = word_tokenize(text)
print("Tokens:\n", tokens)
print("-" * 60)

#lowercasing
lower_tokens = [token.lower() for token in tokens]
print("Lowercased Tokens:\n", lower_tokens)
print("-" * 60)

#stopword removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lower_tokens if token not in stop_words]
print("Tokens after Stopword Removal:\n", filtered_tokens)
print("-" * 60)

#stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
print("Stemmed Tokens:\n", stemmed_tokens)
print("-" * 60)

#lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
print("Lemmatized Tokens:\n", lemmatized_tokens)
print("-" * 60)

#text normalization function
def normalize_text(input_text):
    # Tokenization
    tokens = word_tokenize(input_text)
    # Lowercasing
    lower_tokens = [token.lower() for token in tokens]
    # Stopword Removal
    filtered_tokens = [token for token in lower_tokens if token not in stop_words]
    # Stemming
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    return {
        "tokens": tokens,
        "lower_tokens": lower_tokens,
        "filtered_tokens": filtered_tokens,
        "stemmed_tokens": stemmed_tokens,
        "lemmatized_tokens": lemmatized_tokens
    }
