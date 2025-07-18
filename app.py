from flask import Flask, request, jsonify
from palmistry.detector import detect_lines
from palmistry.rule_mapper import map_features_to_prediction
from utils.image_utils import save_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    filepath = save_image(image, app.config['UPLOAD_FOLDER'])

    features = detect_lines(filepath)
    prediction = map_features_to_prediction(features)

    return jsonify({
        'features': features,
        'prediction': prediction
    })

if __name__ == '__main__':
    app.run(debug=True)