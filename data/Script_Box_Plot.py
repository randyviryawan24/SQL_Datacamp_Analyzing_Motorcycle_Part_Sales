import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv('datalab_export.csv')  # Adjust path if needed

# Optional: Ensure 'month' is ordered correctly
month_order = ['June', 'July', 'August']
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

# Box Plot: Distribution of net revenue per product line
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='product_line', y='net_revenue', hue='month')
plt.title('Box Plot: Net Revenue Distribution by Product Line and Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Violin Plot: Distribution with density
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='product_line', y='net_revenue', hue='month', split=True)
plt.title('Violin Plot: Net Revenue Distribution by Product Line and Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
