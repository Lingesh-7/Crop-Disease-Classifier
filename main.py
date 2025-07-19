# from fastapi import FastAPI,File,UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image

# import tensorflow as tf

# app=FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # origins=["http://localhost","http://localhost:3000",]

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=origins,
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )


# MODEL=tf.keras.models.load_model(r'C:\Users\ADMIN\Desktop\ML_and_DL\Potato_Deisease_classification\saved_models\2.keras')
# CLASS_NAMEs=["Early Blight","Late Blight","Healthy"]


# def read_file_as_image(data) -> np.ndarray:
#     image=np.array(Image.open(BytesIO(data)))
    
#     return image


# @app.get('/')
# async def ping():
#     return "Hello!!"

# @app.post('/predict')
# async def predict(
#     file: UploadFile = File(...)
# ):
#     image= read_file_as_image(await file.read())
#     img_batch=np.expand_dims(image,0)
#     prediction=MODEL.predict(img_batch)
#     # print(prediction)
#     index_=np.argmax(prediction[0])
#     predicted_class=CLASS_NAMEs[index_]
#     confidence=np.max(prediction[0])

#     return {
#         'class':predicted_class,
#         'confidence':float(confidence)
#     }



# if __name__=='__main__':
#     uvicorn.run(app,host='localhost',port=8000)


# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://127.0.0.1:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# MODEL = tf.keras.models.load_model(r'C:\Users\ADMIN\Desktop\ML_and_DL\Potato_Deisease_classification\saved_models\2.keras')

# CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image

# @app.post("/predict")
# async def predict(
#     file: UploadFile = File(...)
# ):
#     image = read_file_as_image(await file.read())
#     img_batch = np.expand_dims(image, 0)
    
#     predictions = MODEL.predict(img_batch)

#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = np.max(predictions[0])
#     return {
#         'class': predicted_class,
#         'confidence': float(confidence)
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)












# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf

# app = Flask(__name__, template_folder='templates', static_folder='static')
# CORS(app, origins=["http://localhost", "http://127.0.0.1:3000"])

# # Load trained model
# MODEL = tf.keras.models.load_model(r'D:\ML_and_DL\Potato_Deisease_classification\saved_models\potato.keras')
# CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# def read_file_as_image(data) -> np.ndarray:
#     image = Image.open(BytesIO(data)).convert("RGB")
#     image = image.resize((256, 256))
#     return np.array(image)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file provided'}), 400

#     file = request.files['file']
#     image = read_file_as_image(file.read())
#     img_batch = np.expand_dims(image, 0)

#     predictions = MODEL.predict(img_batch)
#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = float(np.max(predictions[0]))

#     return jsonify({
#         'class': predicted_class,
#         'confidence': confidence
#     })

# if __name__ == '__main__':
#     app.run(host='localhost', port=8000, debug=True)














from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import tensorflow as tf
from io import BytesIO
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Load models
MODEL_PATHS = {
    "potato": r"D:\ML_and_DL\Potato_Deisease_classification\saved_models\potato.keras",
    "tomato": r"D:\ML_and_DL\Potato_Deisease_classification\saved_models\tomato.h5"
}

MODELS = {
    "potato": tf.keras.models.load_model(MODEL_PATHS["potato"]),
    "tomato": tf.keras.models.load_model(MODEL_PATHS["tomato"])
}

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
    app.run(debug=True, port=8000)
