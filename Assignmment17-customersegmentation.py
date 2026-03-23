import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample dataset
data = pd.DataFrame({
    'Income': [15, 16, 17, 18, 30, 32, 33, 35, 60, 62, 63, 65],
    'Score':  [39, 81, 6, 77, 40, 76, 6, 94, 3, 73, 7, 99]
})

# Apply K-Means
kmeans = KMeans(n_clusters=3)
data['Cluster'] = kmeans.fit_predict(data)

# Plot
plt.scatter(data['Income'], data['Score'], c=data['Cluster'])
plt.xlabel("Income")
plt.ylabel("Score")
plt.title("Customer Segmentation")
plt.show()