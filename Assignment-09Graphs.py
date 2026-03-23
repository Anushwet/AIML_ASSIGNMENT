import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch"],
    "Sales": [150, 300, 120, 200, 100]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure()
plt.bar(df["Product"], df["Sales"])
plt.title("Product Sales - Bar Chart")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Pie Chart
plt.figure()
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%')
plt.title("Sales Distribution - Pie Chart")
plt.show()

# Histogram
plt.figure()
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution - Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Short Data Story
print("\nData Story:")
print("Mobile phones have the highest sales, indicating strong customer demand.")
print("Laptops and headphones show moderate sales levels.")
print("Smartwatches and tablets have comparatively lower sales.")
print("Overall, the sales trend suggests that portable and communication devices dominate the market.")