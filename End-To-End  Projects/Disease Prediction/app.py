<<<<<<< HEAD
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from form
    input_features = [float(x) for x in [
        request.form['Pregnancies'],
        request.form['Glucose'],
        request.form['BloodPressure'],
        request.form['SkinThickness'],
        request.form['Insulin'],
        request.form['BMI'],
        request.form['DiabetesPedigreeFunction'],
        request.form['Age']
    ]]

    # Convert to numpy array and reshape
    input_data = np.array(input_features).reshape(1, -1)

    # Inside predict() function, after getting input_features
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    input_data = pd.DataFrame([input_features], columns=columns)
    # Replace 0s with median (use the same medians from training)
    medians = {'Glucose': 117.0, 'BloodPressure': 72.0, 'SkinThickness': 23.0,
            'Insulin': 30.5, 'BMI': 32.0}  # From data.describe()
    for col in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']:
        input_data[col] = input_data[col].replace(0, medians[col])
    input_data = input_data.values  # Convert back to numpy array

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_data_scaled)

    # Return result
    if prediction[0] == 0:
        result = 'The person is not diabetic'
    else:
        result = 'The person is diabetic'

    return render_template('index.html', prediction_text=result)


if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from form
    input_features = [float(x) for x in [
        request.form['Pregnancies'],
        request.form['Glucose'],
        request.form['BloodPressure'],
        request.form['SkinThickness'],
        request.form['Insulin'],
        request.form['BMI'],
        request.form['DiabetesPedigreeFunction'],
        request.form['Age']
    ]]

    # Convert to numpy array and reshape
    input_data = np.array(input_features).reshape(1, -1)

    # Inside predict() function, after getting input_features
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    input_data = pd.DataFrame([input_features], columns=columns)
    # Replace 0s with median (use the same medians from training)
    medians = {'Glucose': 117.0, 'BloodPressure': 72.0, 'SkinThickness': 23.0,
            'Insulin': 30.5, 'BMI': 32.0}  # From data.describe()
    for col in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']:
        input_data[col] = input_data[col].replace(0, medians[col])
    input_data = input_data.values  # Convert back to numpy array

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_data_scaled)

    # Return result
    if prediction[0] == 0:
        result = 'The person is not diabetic'
    else:
        result = 'The person is diabetic'

    return render_template('index.html', prediction_text=result)


if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 914cd7a19dad2cc2efddbe1408706efd13927dcf
