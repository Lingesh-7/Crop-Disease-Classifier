# 🍅🥔 Potato and Tomato Leaf Disease Classification

A Flask-based web application that classifies **potato and tomato leaf diseases** using deep learning models. Users can **upload images or capture live photos** to get real-time predictions for plant health.

---

## 🚀 Features

* 🌱 **Crop Selection:** Choose between potato and tomato for disease detection.
* 📷 **Image Upload / Live Camera:** Upload leaf images or capture photos in real-time.
* 🤖 **Deep Learning Models:**

  * **Potato CNN Model:**

    * Dataset: 2,152 images
    * Classes: `Potato___Early_blight`, `Potato___Late_blight`, `Potato___healthy`
    * Accuracy: **96.09%**
  * **Tomato CNN Model:**

    * Dataset: 5,172 images
    * Classes: `Tomato__Tomato_YellowLeaf__Curl_Virus`, `Tomato__Tomato_mosaic_virus`, `Tomato_healthy`
    * Accuracy: **99.81%**
* 🌐 **Web Interface:** User-friendly Flask app with a responsive agricultural-themed UI.
* ⚡ **Real-Time Predictions:** Fast inference for quick decision-making.

---

## 🛠️ Tech Stack

* **Backend:** Flask, Python
* **Deep Learning:** TensorFlow, Keras, CNNs
* **Frontend:** HTML, CSS, Bootstrap
* **Others:** OpenCV, NumPy, Pandas

---

## 📂 Project Structure

```
Crop-Disease-Classifier/
│
├── models/
│   ├── potato_model.keras
│   ├── tomato_model.h5
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── index.html
│
├── app.py
├── util.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YourUsername/Crop-Disease-Classifier.git
cd Crop-Disease-Classifier
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Model Training

* Both CNN models were trained with **data augmentation** for better generalization.
* Optimizers: Adam
* Loss Function: Categorical Cross-Entropy
* Early Stopping used to prevent overfitting.

---


## 🔮 Future Improvements

* ✅ Add multilingual support for farmers.
* ✅ Deploy on Render/Heroku with a public URL.
* ✅ Add audio/text-based crop health tips.

---

## 📜 License

This project is open-source under the MIT License.
