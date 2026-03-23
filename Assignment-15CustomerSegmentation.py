import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample Mall dataset: CustomerID, Annual Income (k$), Spending Score (1-100)
data = {
    "CustomerID": [1,2,3,4,5,6,7,8,9,10],
    "Annual_Income": [15, 16, 17, 35, 36, 37, 70, 72, 73, 75],
    "Spending_Score": [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
}

df = pd.DataFrame(data)

# Features for clustering
X = df[["Annual_Income", "Spending_Score"]]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

print("Clustered Data:")
print(df)

# Plot clusters
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"], cmap='viridis')
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation")
plt.show()