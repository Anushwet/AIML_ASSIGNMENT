# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset (messages with labels)
data = {
    'message': [
        'Win money now',
        'Free entry in a contest',
        'Meeting at 5 pm today',
        'Call me when you reach',
        'Congratulations you won a prize',
        'Important project meeting tomorrow',
        'Click here to claim reward',
        'Let us have lunch today'
    ],
    'label': ['spam','spam','ham','ham','spam','ham','spam','ham']
}

# Convert dataset into DataFrame
df = pd.DataFrame(data)

# Separate features (messages) and labels
X = df['message']
y = df['label']

# Convert text messages into numerical data
vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X_vector, y, test_size=0.25)

# Create Naive Bayes model
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

# Test the classifier with a new message
new_message = ["Congratulations! You won a free ticket"]
new_message_vector = vectorizer.transform(new_message)

result = model.predict(new_message_vector)

print("Message:", new_message[0])
print("Prediction:", result[0])


'''
Spam Detection System Design
1. Features (Input Data for Model)

Features are the characteristics used by the machine learning model to detect spam messages.

Some important features include:

Message text content

Presence of spam keywords (e.g., "free", "win", "offer", "lottery")

Number of links in the message

Sender email address or phone number

Message length

Use of capital letters or special characters

These features help the model identify patterns commonly found in spam messages.

2. Data Needed

To train a spam detection system, a dataset containing two types of messages is required:

Spam Messages – Promotional or unwanted messages such as advertisements or scams.

Ham Messages – Normal messages that are not spam.

Each message in the dataset should be labeled as either Spam or Not Spam so that the machine learning model can learn the difference between them.

Example Dataset Structure:

Message	Label
"Congratulations! You won a prize"	Spam
"Are we meeting tomorrow?"	Not Spam
3. Possible Mistakes (Errors)

A spam classifier can make two types of mistakes:

1. False Positive
A normal message is wrongly classified as spam.
Example: A real promotional message from a trusted store goes to the spam folder.

2. False Negative
A spam message is wrongly classified as a normal message.
Example: A scam message appears in the inbox.

These mistakes can affect the reliability of the spam detection system.
'''