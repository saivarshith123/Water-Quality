from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np
import joblib

# Load the scaler and model
scaler = joblib.load("my_scaler.save")
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Collect input features from the form
            input_features = [float(x) for x in request.form.values()]
            features_value = [np.array(input_features)]

            # Define the feature names
            feature_names = ["ph", "Hardness", "Solids", "Chloramines", "Sulfate",
                             "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"]

            # Create a DataFrame
            df = pd.DataFrame(features_value, columns=feature_names)

            # Transform the input data
            df_scaled = scaler.transform(df)

            # Make the prediction
            output = model.predict(df_scaled)

            # Interpret the prediction
            if output[0] == 1:
                prediction = "safe"
            else:
                prediction = "not safe"

            # Render the template with the prediction
            return render_template('home.html', prediction_text="Water is {} for human consumption.".format(prediction))

        except ValueError as ve:
            return render_template('home.html', prediction_text="Invalid input: {}".format(ve))
        except Exception as e:
            return render_template('home.html', prediction_text="An error occurred: {}".format(e))

if __name__ == "__main__":
    app.run(debug=True)
