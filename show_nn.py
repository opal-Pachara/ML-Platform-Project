import torch
import torch.nn as nn
import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

class SentimentNN(nn.Module):
    def __init__(self, input_size=5000, hidden_size=128, output_size=3):
        super(SentimentNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

try:
    model = SentimentNN().to(device)  
    model.load_state_dict(torch.load("model/NeuralModel/sentiment_model.pth", map_location=device))
    model.eval()
    tfidf = joblib.load('model/NeuralModel/tfidf_vectorizer.pkl')
except FileNotFoundError as e:
    st.error(f"Error loading files: {e}. Check if 'model/NeuralModel/sentiment_model.pth' and 'model/NeuralModel/tfidf_vectorizer.pkl' exist.")
    raise

def predict_sentiment(text):
    try:
        text_vector = tfidf.transform([text]).toarray()
        with torch.no_grad():
            inputs = torch.tensor(text_vector, dtype=torch.float32).to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
        
        sentiment = ["Negative", "Neutral", "Positive"][predicted.item()]
        
        sentiment_emoji = {
            "Negative": "😞",
            "Neutral": "😐",
            "Positive": "😀"
        }
        
        return f"{sentiment} {sentiment_emoji[sentiment]}"
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

def show_nn():
    st.markdown("""<h1 style='font-family: Athiti; text-align: center;'>
    YouTube Comment Sentiment Analysis
    </h1>""", unsafe_allow_html=True)

    if 'sentiment_result' not in st.session_state:
        st.session_state.sentiment_result = None

    user_input = st.text_area("Enter the YouTube Comment to Predict Sentiment:")
    if st.button("🎭Predict Sentiment"):
        if user_input:
            sentiment = predict_sentiment(user_input)
            if sentiment:
                st.session_state.sentiment_result = sentiment
        else:
            st.session_state.sentiment_result = "Please enter a comment for prediction."

    if st.session_state.sentiment_result:
        st.write(f"Predicted Sentiment: {st.session_state.sentiment_result}")
