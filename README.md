# 🥔🍅 Crop Disease Classifier  

A web application for detecting **Potato and Tomato leaf diseases** using a deep learning model. The app allows users to upload or capture an image of a leaf and classifies it into different disease categories or as healthy.

---

## 🚀 Features  
- ✅ Classifies **Potato and Tomato leaf diseases**  
- ✅ Real-time camera capture or image upload  
- ✅ Responsive web interface with agricultural theme  
- ✅ Displays classification results with confidence score  
- ✅ Loading spinner for better UX  
- ✅ Future support for multilingual tips for farmers  

---

## 🧠 Models Used  
- **Potato Model:** `saved_models/potato.keras`  
- **Tomato Model:** `saved_models/tomato.h5`  

### Tomato Disease Classes:
- `Tomato__Tomato_mosaic_virus`  
- `Tomato__Tomato_YellowLeaf__Curl_Virus`  
- `Tomato_healthy`  

### Potato Disease Classes:
- *(Add the potato classes here if available)*

---

## ⚙️ Installation  

### 1️⃣ Clone the Repository:
```bash
git clone https://github.com/Lingesh-7/Crop-Disease-Classifier.git
cd Crop-Disease-Classifier
````

### 2️⃣ Install Dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application:

```bash
python main.py
```

### 4️⃣ Open in Browser:

```cpp
http://127.0.0.1:5000/
```

---

## 🌱 Usage

* Select **Potato** or **Tomato** as crop type.
* Upload an image or use live camera capture.
* Click **Classify**.
* Get instant disease prediction with confidence score.

---

## 📦 Deployment

* Supports **Render/Heroku Deployment** with `Procfile` and `runtime.txt`.
* Use relative paths for models to ensure deployment compatibility.

```

✅ You can copy and paste this into your `README.md` file, and it will render perfectly on GitHub.  

Do you also want me to include a **📂 Project Structure** section to show folders and files, or keep it exactly like this?
```
