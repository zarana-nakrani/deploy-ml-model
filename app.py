from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
with open('models/simple_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predicted():
    try:
        data = request.json
        print(data)
        if "x" not in data:
            return jsonify({"error": "Missing input key: 'x'"}), 400
        
        elif data["x"] == None:
            return jsonify({"error": "Invalid input, please input a valid number"}), 500
        
        x = float(data["x"])
        prediction = model.predict(np.array([[x]]))
        return jsonify({"prediction": str(prediction[0])}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)