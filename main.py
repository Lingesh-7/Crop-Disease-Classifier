from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import tensorflow as tf
from io import BytesIO
import os

# ✅ Initialize Flask App
app = Flask(__name__)
CORS(app)

# ✅ Model Paths (Relative for Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATHS = {
    "potato": os.path.join(BASE_DIR, "saved_models", "potato_fixed.keras"),
    "tomato": os.path.join(BASE_DIR, "saved_models", "tomato_fixed.keras")
}

# ✅ Class Names
CLASS_NAMES = {
    "potato": ["Early Blight", "Late Blight", "Healthy"],
    "tomato": ["Tomato YellowLeaf Curl Virus", "Tomato Mosaic Virus", "Tomato Healthy"]
}

# ✅ Helper: Read & preprocess image
def read_image(data):
    image = Image.open(BytesIO(data)).convert("RGB")
    image = image.resize((256, 256))
    return np.expand_dims(np.array(image), axis=0)

# ✅ Lazy-load model to save RAM on Render
def get_model(crop_type):
    return tf.keras.models.load_model(MODEL_PATHS[crop_type])

# ✅ Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        crop_type = request.form['crop']
        file = request.files['file']

        if crop_type not in MODEL_PATHS:
            return jsonify({'error': 'Invalid crop type'}), 400

        # ✅ Load model only when needed
        model = get_model(crop_type)
        image_array = read_image(file.read())
        prediction = model.predict(image_array)

        predicted_class = CLASS_NAMES[crop_type][np.argmax(prediction[0])]
        confidence = float(np.max(prediction[0]))

        return jsonify({
            'class': predicted_class,
            'confidence': round(confidence * 100, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ✅ Render Production Entry Point
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
