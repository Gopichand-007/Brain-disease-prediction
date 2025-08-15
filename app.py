from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Brain Disease Prediction - Flask App Running"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    # Here you would load model and make predictions
    return "Prediction: No Disease Detected (Demo)"

if __name__ == '__main__':
    app.run(debug=True)
