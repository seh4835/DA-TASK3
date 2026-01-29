import pandas as pd

df = pd.read_csv("C:\\Users\\Seher\\Desktop\\DA-TASK3\\sales_data.csv")

print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nInitial Data Preview:")
print(df.head())

df = df.drop_duplicates()

df['Quantity'].fillna(1, inplace=True)

df['Total_Sales'] = df['Quantity'] * df['Price']

total_revenue = df['Total_Sales'].sum()

total_quantity = df['Quantity'].sum()

best_selling_product = (
    df.groupby('Product')['Total_Sales']
    .sum()
    .idxmax()
)

revenue_by_product = df.groupby('Product')['Total_Sales'].sum()

print("\n----- SALES ANALYSIS REPORT -----")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Quantity Sold: {int(total_quantity)} units")
print(f"Best-Selling Product: {best_selling_product}")

print("\nRevenue by Product:")
print(revenue_by_product)

print("\nAnalysis completed successfully.")