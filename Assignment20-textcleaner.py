import string
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')


def remove_emojis(text):
    # Remove emojis using regex
    return re.sub(r'[^\x00-\x7F]+', '', text)


def clean_text(text):
    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove emojis
    text = remove_emojis(text)

    # Step 3: Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Step 4: Tokenization
    words = text.split()

    # Step 5: Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Step 6: Join words
    return " ".join(filtered_words)


# Test
sample_text = "OMG!!! This is an amazing movie, I loved it sooo much 😍🔥"

print("Original:", sample_text)
print("Cleaned:", clean_text(sample_text))