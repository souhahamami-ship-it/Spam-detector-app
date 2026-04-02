from flask import Flask, request, render_template
import joblib
from tensorflow.keras.models import load_model
import string
from nltk.corpus import stopwords
import nltk

# Download stopwords (first time only)
nltk.download('stopwords')

# Initialize app
app = Flask(__name__)

# Load model and vectorizer
model = load_model("model.h5")
vectorizer = joblib.load("vectorizer.pkl")

# Stopwords
stop_words = set(stopwords.words('english'))
punctuations = string.punctuation
def clean_text(text):
    text = text.lower()

    # Remove "subject"
    if text.startswith('subject'):
        text = text[7:]

    # Remove punctuation
    text = text.translate(str.maketrans('', '', punctuations))

    # Remove stopwords
    words = [word for word in text.split() if word not in stop_words]

    return " ".join(words)

# Prediction function
def predict_email(text):
    text = clean_text(text)
    vector = vectorizer.transform([text])
    pred = model.predict(vector)[0][0]

    label = "Spam" if pred > 0.5 else "Ham"
    confidence = round(pred * 100, 2)

    return label, confidence


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None

    if request.method == "POST":
        email = request.form.get("email")

        if email and email.strip() != "":
            result, confidence = predict_email(email)
        else:
            result = "Please enter a message"
            confidence = None

    return render_template(
        "index.html",
        result=result,
        confidence=confidence
    )


# Run the app
if __name__ == "__main__":
    app.run(debug=True)