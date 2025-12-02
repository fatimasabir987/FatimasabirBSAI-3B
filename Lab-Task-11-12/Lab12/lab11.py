# Lab 11 script - ready to run
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("D:\AI Lab\AI_Lab_Project\Lab11\sample_dataset.csv")
X = data.iloc[:,1:-1]
Y = data["city"]

numeric_cols = X.select_dtypes(include=['int64','float64']).columns
X[numeric_cols] = X[numeric_cols].fillna(X[numeric_cols].mean())
categorical_cols = X.select_dtypes(include=['object']).columns
X[categorical_cols] = X[categorical_cols].apply(lambda col: col.fillna(col.mode()[0]))
X[categorical_cols] = X[categorical_cols].apply(lambda col: pd.factorize(col)[0])

rf = RandomForestClassifier(random_state=42)
rf.fit(X,Y)
pickle.dump(rf, open("lab11_model.pkl","wb"))
print("Random Forest model saved.")