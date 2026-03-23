import pandas as pd

# Load dataset (example: CSV file)
data = pd.read_csv("data.csv")

# Display top rows
print("Top 5 rows of dataset:")
print(data.head())

# Find column with highest value (numeric columns)
highest_column = data.max(numeric_only=True).idxmax()
highest_value = data.max(numeric_only=True).max()

print("\nColumn with highest value:", highest_column)
print("Highest value in dataset:", highest_value)

# Count missing values
print("\nMissing values in each column:")
print(data.isnull().sum())