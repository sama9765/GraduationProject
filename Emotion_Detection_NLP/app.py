import pickle
import numpy as np

import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import emoji
import re
import contractions

from flask import Flask, render_template, request, jsonify
import os

# 🔹 IMPORT AI AGENT LOGIC
from agent.emotion_agent import emotion_aware_response

# ---------------------------------------------------
# NLTK RESOURCES (run once; harmless if already exists)
# ---------------------------------------------------
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# ---------------------------------------------------
# PATH SETUP
# ---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "lstm2m.h5")
TOKENIZER_PATH = os.path.join(BASE_DIR, "tokenizer", "tokenizer10k.pkl")

# ---------------------------------------------------
# LOAD MODEL & TOKENIZER
# ---------------------------------------------------
model = load_model(MODEL_PATH)

with open(TOKENIZER_PATH, "rb") as file:
    tokenizer = pickle.load(file)

# ---------------------------------------------------
# TEXT PREPROCESSING SETUP
# ---------------------------------------------------
stop_words = stopwords.words('english')
negation_words = {'no', 'nor', 'not', 'never', 'against'}
filtered_stopwords = set(stop_words) - negation_words

lemmatizer = WordNetLemmatizer()

def remove_emojis(text):
    return emoji.replace_emoji(text, replace="")

def remove_numbers(text):
    return re.sub(r"[0-9]", "", text)

def remove_tags(text):
    return re.sub(r'[@#]\S+', '', text)

def remove_special_characters(text):
    return re.sub(r'[^A-Za-z\s]', ' ', text)

def remove_stopwords(text):
    words = text.split()
    return " ".join([word for word in words if word not in filtered_stopwords])

def lemmatize_text(text):
    tokens = word_tokenize(text)
    return " ".join([lemmatizer.lemmatize(token) for token in tokens])

def preprocess_pipeline(text):
    text = contractions.fix(text)
    text = text.lower()
    text = remove_emojis(text)
    text = remove_numbers(text)
    text = remove_tags(text)
    text = remove_special_characters(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text

# ---------------------------------------------------
# FLASK APP INITIALIZATION
# ---------------------------------------------------
app = Flask(__name__)

# ---------------------------------------------------
# LABEL MAPPING
# ---------------------------------------------------
label_to_emotion = {
    0: 'anger',
    1: 'disgust',
    2: 'fear',
    3: 'joy',
    4: 'neutral',
    5: 'sadness',
    6: 'surprise'
}

# ---------------------------------------------------
# ROUTES
# ---------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_text = data.get('text', '')

    if not input_text.strip():
        return jsonify({"error": "Empty input text"}), 400

    # 🔹 PREPROCESS INPUT
    processed_text = preprocess_pipeline(input_text)

    # 🔹 TOKENIZE & PAD
    sequence = tokenizer.texts_to_sequences([processed_text])
    padded_sequence = pad_sequences(sequence, maxlen=50, padding='post')

    # 🔹 MODEL PREDICTION
    probabilities = model.predict(padded_sequence)[0]

    # 🔹 FINAL EMOTION
    predicted_index = np.argmax(probabilities)
    final_emotion = label_to_emotion[predicted_index]

    # 🔹 AI AGENT RESPONSE
    agent_message = emotion_aware_response(final_emotion)

    # 🔹 PREPARE PROBABILITY DATA
    emotion_data = [
        {
            "emotion": label_to_emotion[i],
            "probability": round(float(prob) * 100, 2)
        }
        for i, prob in enumerate(probabilities)
    ]

    # 🔹 FINAL RESPONSE
    return jsonify({
        "final_emotion": final_emotion,
        "agent_message": agent_message,
        "emotion_data": emotion_data
    })

# ---------------------------------------------------
# RUN APP
# ---------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

