import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv(r"datalab_export.csv")

# Pivot table for heatmap (e.g., product_line vs warehouse)
pivot_table = df.pivot_table(
    index='product_line',
    columns='warehouse',
    values='net_revenue',
    aggfunc='sum'  # in case of duplicates
)

# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap='YlGnBu')
plt.title('Net Revenue by Product Line and Warehouse')
plt.ylabel('Product Line')
plt.xlabel('Warehouse')
plt.tight_layout()
plt.show()
