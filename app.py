from flask import Flask, request, jsonify, render_template
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
CORS(app)

port = int(os.environ.get("PORT", 5000))

ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

nltk.download('punkt')
nltk.download('stopwords')

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Serve HTML
@app.route("/")
def home():
    return render_template("index.html")

# API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["message"]

    transformed_text = transform_text(data)
    vectorized_text = tfidf.transform([transformed_text])
    result = model.predict(vectorized_text)[0]

    output = "SPAM" if result == 1 else "NOT SPAM"

    return jsonify({"prediction": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)