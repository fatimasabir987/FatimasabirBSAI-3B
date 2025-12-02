from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("lab11_model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = request.form.get("age")
        gender = request.form.get("gender")
        score = request.form.get("score")

        # Convert input to DataFrame (same format as model training)
        input_data = pd.DataFrame({
            "age": [float(age)],
            "gender": [gender],
            "score": [float(score)]
        })

        # Preprocess same as Lab 11
        numeric_cols = input_data.select_dtypes(include=['int64','float64']).columns
        input_data[numeric_cols] = input_data[numeric_cols].fillna(input_data[numeric_cols].mean())

        categorical_cols = input_data.select_dtypes(include=['object']).columns
        input_data[categorical_cols] = input_data[categorical_cols].apply(lambda col: col.fillna(col.mode()[0]))
        input_data[categorical_cols] = input_data[categorical_cols].apply(lambda col: pd.factorize(col)[0])

        # Prediction
        prediction = model.predict(input_data)[0]

        return render_template("index.html", result=f"Predicted City: {prediction}")

    except Exception as e:
        return render_template("index.html", result=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
