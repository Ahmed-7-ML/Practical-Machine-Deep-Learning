from flask import Flask, render_template, request
import joblib
import pandas as pd

# Create Flask App
app = Flask(__name__)

# Load trained pipeline (preprocessor + model)
try:
    model = joblib.load("CarPrice_Model.pkl")
except FileNotFoundError:
    model = None

# Home Page


@app.route("/")
def home():
    return render_template("index.html")

# Predict Page


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Collect Form Inputs
        make = request.form["Make"]
        model_name = request.form["Model"]
        engine_fuel_type = request.form["Engine Fuel Type"]
        engine_hp = float(request.form["Engine HP"])
        engine_cylinders = float(request.form["Engine Cylinders"])
        number_of_doors = float(request.form["Doors"])
        vehicle_style = request.form["Vehicle Style"]
        highway_mpg = int(request.form["Highway MPG"])
        city_mpg = int(request.form["City MPG"])
        popularity = int(request.form["Popularity"])
        transmission_type = request.form["Transmission Type"]
        driven_wheels = request.form["Driven Wheels"]
        vehicle_size = request.form["Vehicle Size"]
        year = int(request.form["Year"])

        # Create DataFrame (same structure as training)
        input_data = pd.DataFrame([{
            "make": make,
            "model": model_name,
            "engine_fuel_type": engine_fuel_type,
            "engine_hp": engine_hp,
            "engine_cylinders": engine_cylinders,
            "number_of_doors": number_of_doors,
            "vehicle_style": vehicle_style,
            "highway_mpg": highway_mpg,
            "city_mpg": city_mpg,
            "popularity": popularity,
            "transmission_type": transmission_type,
            "driven_wheels": driven_wheels,
            "vehicle_size": vehicle_size,
            "year": year
        }])

        # Prediction
        if model:
            prediction = model.predict(input_data)[0]
            prediction = round(prediction, 2)
            return render_template("index.html", prediction_text=f"Predicted Car Price: ${prediction}")
        else:
            return render_template("index.html", prediction_text="Error: Model not found. Please ensure CarPrice_Model.pkl is in the same directory.")


if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)
