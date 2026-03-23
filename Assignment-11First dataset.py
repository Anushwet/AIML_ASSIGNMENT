import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Create dataset: Study hours vs Marks
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 50, 55, 65, 70, 75, 85]
}

df = pd.DataFrame(data)

# Features and Labels
X = df[["Study_Hours"]]  # Feature
y = df["Marks"]          # Label

# Build simple Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict marks for 9 study hours
predicted_marks = model.predict([[9]])

print("Predicted marks for 9 study hours:", predicted_marks[0])

# Plot dataset and regression line
plt.scatter(df["Study_Hours"], df["Marks"], color='blue', label='Actual Marks')
plt.plot(df["Study_Hours"], model.predict(X), color='red', label='Regression Line')
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()
plt.show()