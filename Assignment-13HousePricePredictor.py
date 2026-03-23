import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Area_sqft": [500, 800, 1000, 1200, 1500],
    "Price": [1000000, 1500000, 2000000, 2300000, 3000000]
}

df = pd.DataFrame(data)

# Features and label
X = df[["Area_sqft"]]
y = df["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# User input
area = int(input("Enter house area in sqft: "))

# Convert input to DataFrame (Fix)
new_data = pd.DataFrame([[area]], columns=["Area_sqft"])

predicted_price = model.predict(new_data)

print("Predicted House Price:", int(predicted_price[0]))