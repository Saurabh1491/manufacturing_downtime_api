from flask import Flask, request, jsonify
from model import train_model, make_prediction

app = Flask(__name__)

# Upload Endpoint
@app.route('/upload', methods=['POST'])
def upload_data():
    file = request.files['file']
    file.save('./data/uploaded_data.csv')
    return jsonify({"message": "File uploaded successfully!"})

# Train Endpoint
@app.route('/train', methods=['POST'])
def train():
    accuracy, f1_score = train_model('./data/uploaded_data.csv')
    return jsonify({"accuracy": accuracy, "f1_score": f1_score})

# Predict Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    result = make_prediction(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
