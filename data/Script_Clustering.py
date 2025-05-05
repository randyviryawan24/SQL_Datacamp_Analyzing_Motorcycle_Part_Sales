# Step 1: Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 2: Load the CSV data into a pandas DataFrame
df = pd.read_csv('datalab_export.csv')  # Replace with your actual CSV file path

# Step 3: Prepare the data for clustering
# Convert the 'month' column to a categorical type with a custom order
month_order = ['June', 'July', 'August']
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

# Pivot the data to get product line vs. month with the net revenue
pivot_table = df.pivot_table(index='product_line', columns='month', values='net_revenue', aggfunc='sum')

# Step 4: Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(pivot_table)

# Step 5: Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # You can adjust the number of clusters
pivot_table['cluster'] = kmeans.fit_predict(normalized_data)

# Step 6: Visualize the Clusters
# Plot the monthly revenue patterns for each cluster
for cluster in range(3):  # Assuming 3 clusters
    cluster_data = pivot_table[pivot_table['cluster'] == cluster]
    
    plt.figure(figsize=(10, 6))
    for product_line in cluster_data.index:
        # Exclude the 'cluster' column and correctly index the month columns
        months = pivot_table.columns[:-1]  # Exclude the last 'cluster' column
        monthly_revenue = pivot_table.loc[product_line, months]
        plt.plot(months, monthly_revenue, label=product_line)
    
    plt.title(f"Cluster {cluster}")
    plt.xlabel('Month')
    plt.ylabel('Net Revenue')
    plt.legend()
    plt.grid(True)
    plt.show()

# Step 7: Inspect the clusters and product line patterns
print("Cluster Centers:")
print(kmeans.cluster_centers_)
