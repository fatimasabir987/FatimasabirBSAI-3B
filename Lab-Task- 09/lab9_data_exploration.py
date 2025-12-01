import pandas as pd
file_name = "D:\AI Lab\Lab-Task- 09\sample_dataset.csv"
df = pd.read_csv(file_name)

print("\nDATA LOADED\n")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset shape:")
print("Rows   :", df.shape[0])
print("Columns:", df.shape[1])

print("\nNull values per column:")
print(df.isnull().sum())

print("\nColumn data types:")
print(df.dtypes)
