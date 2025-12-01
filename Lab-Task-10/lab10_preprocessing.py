import pandas as pd
import numpy as np

file_name = "D:\AI Lab\Lab-Task-10\sample_dataset.csv"
data = pd.read_csv(file_name)

print("\nInitial null-values count:")
print(data.isnull().sum())

fill_values = data.mode().iloc[0]
data = data.fillna(fill_values)
print("\nMissing values filled using mode:\n", data.isnull().sum())

data['age'] = data['age'].astype(np.int64)
data['score'] = data['score'].astype(np.int64)

if 'id' in data.columns:
    data = data.drop('id', axis=1)
    print("\nDropped column 'id'.")

print("\nUpdated data types:")
print(data.dtypes)

X = data.iloc[:, :-1]    
y = data.iloc[:, -1]      

print("\nShapes after split:")
print("X:", X.shape)
print("y:", y.shape)

cat_cols = X.select_dtypes(include=['object']).columns
if len(cat_cols) > 0:
    X[cat_cols] = X[cat_cols].apply(lambda col: pd.factorize(col)[0])
    print("\nCategorical columns encoded:", list(cat_cols))

print("\nPre‑processing complete. Sample of processed features:")
print(X.head())
