from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import tensorflow as tf
from io import BytesIO
import os

# Initialize Flask App
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATHS = {
    "potato": os.path.join(BASE_DIR, "saved_models", "potato.keras"),
    "tomato": os.path.join(BASE_DIR, "saved_models", "tomato.h5")
}


try:
    MODELS = {
        "potato": tf.keras.models.load_model(MODEL_PATHS["potato"]),
        "tomato": tf.keras.models.load_model(MODEL_PATHS["tomato"])
    }
except Exception as e:
    print("❌ Error loading models:", e)


CLASS_NAMES = {
    "potato": ["Early Blight", "Late Blight", "Healthy"],
    "tomato": [ "Tomato YellowLeaf Curl Virus"," Tomat mosaic virus", "Tomato healthy"]
}


def read_image(data):
    image = Image.open(BytesIO(data)).convert("RGB")
    image = image.resize((256, 256))
    return np.expand_dims(np.array(image), axis=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        crop_type = request.form['crop']
        file = request.files['file']

        if crop_type not in MODELS:
            return jsonify({'error': 'Invalid crop type'}), 400

        image_array = read_image(file.read())
        prediction = MODELS[crop_type].predict(image_array)
        predicted_class = CLASS_NAMES[crop_type][np.argmax(prediction[0])]
        confidence = float(np.max(prediction[0]))

        return jsonify({
            'class': predicted_class,
            'confidence': round(confidence * 100, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # ✅ Render requires 0.0.0.0 and PORT from environment variable
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
