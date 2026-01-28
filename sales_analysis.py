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
