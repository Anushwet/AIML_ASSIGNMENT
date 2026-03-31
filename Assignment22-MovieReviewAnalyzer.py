from textblob import TextBlob

# Sample reviews
reviews = [
    "The movie was amazing and very interesting",
    "I hated the film, it was boring",
    "What a fantastic performance by the actors",
    "The plot was dull and disappointing",
    "Absolutely loved the cinematography"
]

# Analyze sentiment
for i, review in enumerate(reviews):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    print(f"Review {i+1}: {review}")
    print("Sentiment:", sentiment)
    print("Polarity Score:", round(polarity, 2))
    print("-" * 50)