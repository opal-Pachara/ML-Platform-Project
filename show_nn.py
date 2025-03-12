import torch
import torch.nn as nn
import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# สร้างโมเดล Neural Network สำหรับการทำนาย Sentiment
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

# โหลดโมเดลและ TF-IDF vectorizer
try:
    model = SentimentNN().to(device)  # Initialize with default input_size=5000
    model.load_state_dict(torch.load("model/sentiment_model.pth", map_location=device))
    model.eval()
    tfidf = joblib.load('model/tfidf_vectorizer.pkl')
except FileNotFoundError as e:
    st.error(f"Error loading files: {e}. Check if 'model/sentiment_model.pth' and 'model/tfidf_vectorizer.pkl' exist.")
    raise

# ฟังก์ชันสำหรับทำนายผล Sentiment
def predict_sentiment(text):
    try:
        # แปลงข้อความเป็น TF-IDF vector
        text_vector = tfidf.transform([text]).toarray()
        # ทำนายผลลัพธ์จากโมเดล
        with torch.no_grad():
            inputs = torch.tensor(text_vector, dtype=torch.float32).to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
        
        sentiment = ["Negative", "Neutral", "Positive"][predicted.item()]
        
        # Map sentiment to emoji
        sentiment_emoji = {
            "Negative": "😞",
            "Neutral": "😐",
            "Positive": "😀"
        }
        
        # Return sentiment and emoji
        return f"{sentiment} {sentiment_emoji[sentiment]}"
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

# ฟังก์ชันในการแสดงผล
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
                # Store the result in session state
                st.session_state.sentiment_result = sentiment
        else:
            st.session_state.sentiment_result = "Please enter a comment for prediction."

    # Display the stored result (won’t disappear on rerun)
    if st.session_state.sentiment_result:
        st.write(f"Predicted Sentiment: {st.session_state.sentiment_result}")
