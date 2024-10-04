import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors

# Load your dataset (assuming df is already defined)
features_df = pd.read_csv("data/feature_df.csv")# your dataframe here
labels_df = pd.read_csv("data/label_df.csv")# your dataframe here

# Drop the 'Country' column as it's categorical and not needed for clustering
# Also drop the sunshine column as it's not needed for clustering
df_clustering = features_df.drop(['country', 'annual_sunshine', 'internet_usage', 'religion_importance'], axis=1)

# Standardize the data to ensure all features are on the same scale
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_clustering)

# Determine the optimal number of clusters using the Elbow Method
# also do the Davies-Boulding index
inertia = []
davies_bouldin_scores = []
K_range = range(1, 10)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)
    if k > 1:  # Davies-Bouldin index is not defined for k=1
        db_score = davies_bouldin_score(df_scaled, kmeans.labels_)
        davies_bouldin_scores.append(db_score)

# Plot the Davies-Bouldin index
plt.figure(figsize=(8,5))
plt.plot(K_range[1:], davies_bouldin_scores, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Davies-Bouldin Index')
plt.title('Davies-Bouldin Index for Optimal k')

# Save figure
plt.savefig('plots/davies_bouldin_index.png')

# Plot the Elbow Method
plt.figure(figsize=(8,5))
plt.plot(K_range, inertia, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia (Sum of squared distances)')
plt.title('Elbow Method for Optimal k')

# Save figure
plt.savefig('plots/elbow_method.png')

optimal_k = 3  # Optimal number of clusters based on the Elbow Method
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
features_df['Cluster'] = kmeans.fit_predict(df_scaled)

# Merge the labels with the clustered data
merged_df = features_df.join(labels_df.set_index('country'), on='country')

# Analyze clusters
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.boxplot(x='Cluster', y='suicide_rate', data=merged_df)
plt.title('Suicide Rate Distribution Across Clusters')

# Save figure
plt.savefig('plots/Suicide_cluster.png')

# Examine cluster characteristics
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=df_clustering.columns)
print(cluster_centers)

# Save the countries and their cluster in a new df and save it to file
countries_clusters_df = features_df[['country', 'Cluster']]
countries_clusters_df.to_csv('countries_clusters.csv', index=False)
print(countries_clusters_df)


# Calculate silhoutte scores for the clustering
# Calculate the silhouette score
silhouette_avg = silhouette_score(df_scaled, features_df['Cluster'])
print(f'Silhouette Score: {silhouette_avg}')