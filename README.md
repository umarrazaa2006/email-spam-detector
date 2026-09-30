# Email & SMS Spam Detector

A machine learning web app that classifies messages as **spam** or **not spam (ham)** in real time. It uses an NLP pipeline (text preprocessing, TF-IDF features, Multinomial Naive Bayes) served through a Flask REST API with a JavaScript frontend.

---

## Results

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 96.4% |
| Precision | 99.2% |

Trained and evaluated on **5,572 labeled messages** (`spam.csv`).

High precision means very few legitimate messages are wrongly flagged as spam.

## How It Works

1. **Preprocessing** – text is cleaned and normalized with NLTK (lowercasing, tokenization, stop-word removal, stemming).
2. **Feature extraction** – messages are converted to numerical vectors with TF-IDF (top 3,000 features).
3. **Classification** – a Multinomial Naive Bayes classifier predicts spam or ham.
4. **Serving** – the trained model and vectorizer are saved as `model.pkl` and `vectorizer.pkl`, loaded by the Flask app, and exposed through a REST API used by the web frontend.

## Tech Stack

| Area          | Technologies                        |
| ------------- | ----------------------------------- |
| Language      | Python, JavaScript                  |
| ML / NLP      | scikit-learn, NLTK, Pandas          |
| Backend       | Flask (REST API)                    |
| Frontend      | HTML, CSS, JavaScript               |
| Deployment    | Render                              |

## Project Structure

```
email-spam-detector/
├── app/               # Frontend (web interface)
├── app.py             # Flask application and prediction API
├── train_model.py     # Trains the model and saves the .pkl files
├── spam.csv           # Labeled dataset (5,572 messages)
├── model.pkl          # Trained Multinomial Naive Bayes model
├── vectorizer.pkl     # Fitted TF-IDF vectorizer
└── requirements.txt   # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/umarrazaa2006/email-spam-detector.git
cd email-spam-detector
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Retrain the model

The repository already includes `model.pkl` and `vectorizer.pkl`. To retrain from `spam.csv`:

```bash
python train_model.py
```

### 5. Run the app

```bash
python app.py
```

Then open the URL shown in the terminal (Flask's default is `http://localhost:5000`).

## API Usage

Send a message to the prediction endpoint and receive a classification.

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You won a free prize. Click here to claim."}'
```

Example response:

```json
{ "prediction": "spam" }
```

## Dataset

`spam.csv` contains 5,572 labeled SMS/email messages, each marked as `spam` or `ham`.

## Future Improvements

- Compare against other models (Logistic Regression, SVM, Random Forest)
- Show a spam probability score alongside the label
- Add a confusion matrix and ROC curve to the evaluation
- Support batch classification of multiple messages

## Author

**Mohammad Umar Raza**
[GitHub](https://github.com/umarrazaa2006) · [LinkedIn](https://linkedin.com/in/mohammad-umar-raza-260601330) · [LeetCode](https://leetcode.com/u/mohammad_umar_/)
