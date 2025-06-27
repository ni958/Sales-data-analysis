import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('sales_data.csv')

# Clean data
data.dropna(inplace=True)

# Monthly sales
monthly_sales = data.groupby('Month')['Revenue'].sum()
print("Monthly Sales:\n", monthly_sales)

# Top products
top_products = data.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:\n", top_products)

# Plot monthly sales
monthly_sales.plot(kind='bar', title='Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
