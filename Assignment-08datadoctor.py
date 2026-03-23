import pandas as pd

# Load dataset
data = pd.read_csv("data.csv")

# Display first rows
print("Original Data:")
print(data.head())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Handle missing values (fill with mean for numeric columns)
data = data.fillna(data.mean(numeric_only=True))

# Remove duplicate rows
data = data.drop_duplicates()

# Standardize text columns (convert to lowercase)
for col in data.select_dtypes(include='object').columns:
    data[col] = data[col].str.lower()

print("\nCleaned Data:")
print(data.head())

# Save cleaned dataset
data.to_csv("cleaned_data.csv", index=False)

''' 
Explanation (Why Data Cleaning Matters)

Data cleaning is an important step in data analysis and machine learning. Real-world datasets often contain missing values, duplicate records, and inconsistent text formats, which can lead to incorrect analysis and poor model performance.

By handling missing values, we ensure that incomplete data does not affect results. Removing duplicates prevents repeated information from biasing the analysis. Standardizing text makes the dataset consistent and easier to process.

Therefore, data cleaning improves data quality, accuracy, and reliability, which leads to better insights and more accurate machine learning models.
'''