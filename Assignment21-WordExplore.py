from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "Machine learning is a subset of artificial intelligence",
    "Artificial intelligence and machine learning are related fields",
    "Python is widely used in machine learning",
    "Data science uses machine learning and statistics",
    "Artificial intelligence is transforming industries"
]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)


# Get feature names
feature_names = vectorizer.get_feature_names_out()
vectorizer = TfidfVectorizer(stop_words='english')
# Display TF-IDF scores
for i, doc in enumerate(X.toarray()):
    print(f"\nDocument {i+1} Top Words:")
    top_indices = doc.argsort()[-3:][::-1]
    for index in top_indices:
        print(feature_names[index], doc[index])