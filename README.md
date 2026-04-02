# 📧 Spam Email Detector

A machine learning-powered web application that classifies emails as **Spam** or **Ham (Not Spam)** using Natural Language Processing and Deep Learning.

---

## 🚀 Overview

This project is a complete end-to-end ML application:

* 🧠 Trained model for spam detection
* 🔎 Text preprocessing using NLTK
* 🌐 Web interface built with Flask
* ⚡ Real-time prediction with confidence score

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **TensorFlow / Keras**
* **Scikit-learn**
* **NLTK**
* **HTML / Jinja2**

---

## 📂 Project Structure

```
FINAL/
│
├── app.py                      # Flask app
├── model.h5                    # Trained deep learning model
├── vectorizer.pkl              # Text vectorizer
├── spam_detector_notebook.ipynb # Model training notebook
├── spam_ham_dataset.csv        # Dataset
├── templates/
│   └── index.html              # Frontend UI
└── requirements.txt
```

---

## ⚙️ How It Works

1. User inputs an email message
2. Text is cleaned:

   * Lowercasing
   * Removing punctuation
   * Removing stopwords
3. Text is vectorized using a trained vectorizer
4. Model predicts probability
5. Output:

   * **Spam / Ham**
   * **Confidence score**

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/spam-detector.git
cd spam-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## ⚠️ Notes

* Large files like `model.h5` and `vectorizer.pkl` may be excluded from GitHub.
* You may need to retrain the model using the notebook if not included.

---

