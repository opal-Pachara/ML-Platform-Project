import streamlit as st
import pickle
import numpy as np
import os
from datetime import datetime
import plotly.graph_objects as go

def show_ml():
    st.markdown("""<h1 style='font-family: Athiti; text-align: center;'>Machine Learning Model</h1>""", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Decision Tree Model",
        "K-Nearest Neighbors (KNN) Model",
        "Random Forest Model",
        "SVM Linear Model",
        "SVR Model"
    ])
    
    model_paths = {
        "Decision Tree": "model/MLclassical/dt_model.pkl",
        "K-Nearest Neighbors": "model/MLclassical/knn_model.pkl",
        "Random Forest": "model/MLclassical/rf_model.pkl",
        "SVM Linear": "model/MLclassical/svm_linear_model.pkl",
        "SVR": "model/MLclassical/svr_model.pkl"
    }

    models = {}
    for name, path in model_paths.items():
        if os.path.exists(path):
            with open(path, 'rb') as f:
                models[name] = pickle.load(f)
        else:
            st.error(f"ไม่พบไฟล์โมเดล {name} ที่ {path}")
            return

    scaler_path = "model/MLclassical/scaler.pkl"
    try:
        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)
    except FileNotFoundError:
        st.error(f"ไม่พบไฟล์ {scaler_path} กรุณาตรวจสอบว่า scaler.pkl อยู่ในโฟลเดอร์ 'model/'")
        return

    tab_list = [tab1, tab2, tab3, tab4, tab5]
    
    if "predictions" not in st.session_state:
        st.session_state["predictions"] = {}
    
    if "plot_summary" not in st.session_state:
        st.session_state["plot_summary"] = None

    for idx, (name, model) in enumerate(models.items()):
        with tab_list[idx]:
            st.markdown(f"""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
                {name} Model
                </h5>""", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            
            # Input group 1: Year, Month, Plastic Waste, Recycling Percentage, Recycling Trend
            with col1:
                date = st.date_input(f"Date (ปี-เดือน)", value=datetime.now(), key=f"date_{name}")
                year = date.year
                month = date.month
                plastic_waste = st.number_input("Plastic Bottle Waste Generated (Million Bottles)", min_value=0.0, max_value=500.0, value=200.0, step=10.0, key=f"plastic_waste_{name}")
                recycling_percent = st.number_input("Recycling Percentage (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0, key=f"recycling_percent_{name}")
                recycling_trend = st.number_input("Recycling Trend (0-100)", min_value=0.0, max_value=100.0, value=50.0, step=1.0, key=f"recycling_trend_{name}")
            
            # Input group 2: Population, Recycling Policy Level
            with col2:
                population = st.number_input("Population (Million)", min_value=62.0, max_value=67.0, value=65.0, step=0.1, key=f"population_{name}")
                policy_level = st.number_input("Recycling Policy Level (0-3)", min_value=0, max_value=3, value=2, step=1, key=f"policy_level_{name}")
                
                waste_per_pop = plastic_waste / population
                waste_policy = plastic_waste * policy_level
                trend_policy = recycling_trend * policy_level
                year_trend = year * recycling_trend
                
                st.write(f"Waste per Population: {waste_per_pop:.2f}")
                st.write(f"Waste-Policy Interaction: {waste_policy:.2f}")
                st.write(f"Trend-Policy Interaction: {trend_policy:.2f}")
                st.write(f"Year-Trend Interaction: {year_trend:.2f}")
            
            # Prepare input data for the model
            input_data = np.array([[year, month, plastic_waste, recycling_percent, recycling_trend, 
                                    population, policy_level, waste_per_pop, waste_policy, 
                                    trend_policy, year_trend]])
            
            input_scaled = scaler.transform(input_data)
            
            if f"prediction_{name}" not in st.session_state:
                st.session_state[f"prediction_{name}"] = None

            # Create a centered column layout for the button
            center_col = st.columns(1)[0]  # Create a column with only one section
            with center_col:
                if st.button(f"Predict with {name}", key=f"predict_{name}"):
                    try:
                        # Perform prediction
                        pred = model.predict(input_scaled)[0]
                        recycled_tons = (pred * plastic_waste) / 250
                        st.session_state[f"prediction_{name}"] = (pred, recycled_tons)

                        # Store the prediction in session state for summary graph
                        st.session_state["predictions"][name] = recycled_tons
                    except Exception as e:
                        st.error(f"Error predicting with {name}: {str(e)}")
            
            if st.session_state[f"prediction_{name}"]:
                pred, recycled_tons = st.session_state[f"prediction_{name}"]

    # Create a summary graph displaying all models' predictions together
    if st.session_state.predictions:
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       ผลลัพท์การทำนาย (ตัน):
    </p>""", unsafe_allow_html=True)
        
        # Display individual model predictions
        for model_name, recycled_tons in st.session_state.predictions.items():
            st.write(f"{model_name}: {recycled_tons:.2f} ตัน")
        
        # Create the plot comparing predictions for each model
        fig = go.Figure()
        model_names = list(st.session_state.predictions.keys())
        pred_values = list(st.session_state.predictions.values())
        
        fig.add_trace(go.Scatter(
            x=model_names,
            y=pred_values,
            mode='lines+markers',
            name="Recycled Waste",
            line=dict(color='cyan', width=2),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="เปรียบเทียบจำนวนขยะที่ถูกรีไซเคิลจากแต่ละโมเดล",
            xaxis_title="โมเดล",
            yaxis_title="จำนวนขยะที่ถูกรีไซเคิล (ตัน)",
            template="plotly_dark",
            height=500,
            showlegend=True
        )
        
        st.session_state["plot_summary"] = fig

        st.plotly_chart(st.session_state["plot_summary"])
