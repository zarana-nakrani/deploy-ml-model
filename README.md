# Flask ML Prediction App

This is a Flask-based web application that serves a simple machine learning model for making predictions.

## Features
- Load a pre-trained Linear Regression model
- Accept input from a web form
- Provide real-time predictions via an API

## Installation

# Clone the Repository (if applicable)
git clone git@github.com:zarana-nakrani/deploy-ml-model.git
cd deploy-ml-model

# Install Dependencies
pip install -r requirements.txt

# Ensure Model Exists
# Make sure `simple_model.pkl` is available in the `models/` directory.
# If missing, you can retrain and save the model using `linear-regression.py`.

# Run the Application
python app.py
```

## Access the Web Interface
Open `http://127.0.0.1:5000/` in your browser.

## API Usage

### **POST /predict**

#### **Request:**
```json
{
    "x": 5.0
}
```

#### **Response:**
```json
{
    "prediction": 11.0
}
```

## Frontend Integration
The app includes a simple HTML form (`index.html`) that allows users to submit a value and display the model's prediction dynamically using JavaScript.

## Troubleshooting
- If the model fails to load, ensure the `simple_model.pkl` file is in the correct path.
- Check the Flask logs for detailed error messages.
- Ensure that your input data matches the expected format.
