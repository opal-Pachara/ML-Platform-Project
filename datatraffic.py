import torch
import torch.nn as nn
import streamlit as st
import pandas as pd
import pickle

# Define the Neural Network Model structure
class NeuralNetworkModel(nn.Module):
    def __init__(self):
        super(NeuralNetworkModel, self).__init__()
        self.layer1 = nn.Linear(6, 64)  # Ensure 6 features input
        self.layer2 = nn.Linear(64, 32)
        self.layer3 = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = self.layer3(x)
        return x

def show_nn():
    # Load the saved model
    model = NeuralNetworkModel()
    with open('model/traffic_nn_model.pkl', 'rb') as f:
        model_params = pickle.load(f)
        model.load_state_dict(model_params, strict=False)
    
    # Set model to evaluation mode
    model.eval()

    # Streamlit UI
    st.title('Neural Network Traffic Prediction')

    # Dropdown or multi-select for location, time, festival, and day selection
    locations = ["siamparagon", "suvarnabhumi_airport", "donmuang_airport", "chatuchak_market", "centralworld", 
                 "victory_monument", "government_complex", "mochit_bus_station", "ekamai_bus_station", 
                 "hua_lamphong_station", "pattaya", "chiangmai", "phuket", "hatyai", "ayutthaya", "korat", "khonkaen", "hua_hin"]
    time_periods = ["06:00-09:00", "09:00-12:00", "12:00-15:00", "15:00-18:00", "18:00-21:00", "21:00-00:00"]
    festivals = ["songkran", "new_year", "loy_krathong", "start_of_term", "end_of_term", "public_holiday", 
                 "weekday", "vesak", "magha_bucha"]
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # User input selectors (allow multi-selection)
    location = st.multiselect("Select Locations", locations)
    time_period = st.multiselect("Select Time Periods", time_periods)
    festival = st.multiselect("Select Festivals", festivals)
    day_of_week = st.multiselect("Select Days of the Week", days_of_week)

    # Numeric input for additional features if needed
    feature1 = st.number_input("Feature 1", min_value=0.0, step=0.1)
    feature2 = st.number_input("Feature 2", min_value=0.0, step=0.1)
    feature3 = st.number_input("Feature 3", min_value=0.0, step=0.1)
    feature4 = st.number_input("Feature 4", min_value=0.0, step=0.1)
    feature5 = st.number_input("Feature 5", min_value=0.0, step=0.1)
    feature6 = st.number_input("Feature 6", min_value=0.0, step=0.1)

    # Combine features into a tensor (you can encode categorical features here)
    input_data = torch.tensor([[feature1, feature2, feature3, feature4, feature5, feature6]], dtype=torch.float32)

    # Button for prediction
    if st.button('Make Prediction'):
        with torch.no_grad():  # Disable gradient computation during inference
            output = model(input_data)
            st.write(f"Prediction: {output.item()}")

if __name__ == "__main__":
    show_nn()
