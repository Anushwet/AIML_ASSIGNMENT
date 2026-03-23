import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Weather": ["Sunny", "Sunny", "Rainy", "Rainy"],
    "Temperature": ["Hot", "Mild", "Hot", "Mild"],
    "Wind": ["Weak", "Strong", "Weak", "Strong"],
    "Play": ["No", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

# Convert text to numbers
df["Weather"] = df["Weather"].map({"Sunny":0, "Rainy":1})
df["Temperature"] = df["Temperature"].map({"Hot":0, "Mild":1})
df["Wind"] = df["Wind"].map({"Weak":0, "Strong":1})
df["Play"] = df["Play"].map({"No":0, "Yes":1})

# Features and label
X = df[["Weather","Temperature","Wind"]]
y = df["Play"]

# Train decision tree
model = DecisionTreeClassifier()
model.fit(X,y)

# Plot tree
plt.figure(figsize=(8,6))
plot_tree(model,
          feature_names=["Weather","Temperature","Wind"],
          class_names=["No","Yes"],
          filled=True)

plt.title("Decision Tree - Play Outside")
plt.show()