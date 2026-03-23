'''
1. Explanation: Netflix Recommendations using KNN

Netflix recommends movies or shows to users based on what similar users liked. This can be modeled using K-Nearest Neighbors (KNN):
KNN Concept: KNN finds the ‘k’ most similar items (or users) based on a similarity metric.

In Netflix Terms:
Users are represented by vectors of their movie ratings.
Similarity between users is measured (e.g., cosine similarity or Euclidean distance).
Netflix suggests movies that similar users liked but the current user hasn’t watched.

Example Workflow:
Collect Data: Users’ ratings for movies.
Compute Similarity: Find users with similar taste.
Find Neighbors: Pick top k users closest to the target user.
'''

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# User-movie rating matrix
ratings = np.array([
    [5, 3, 0],  # U1
    [4, 0, 5],  # U2
    [5, 4, 0],  # U3
    [0, 2, 4]   # U4
])

# Compute cosine similarity between users
similarity = cosine_similarity(ratings)

print("User Similarity Matrix:\n", similarity)