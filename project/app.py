import streamlit as st
import pandas as pd
import numpy as np
import pickle
from groq_chat import ask_groq
from visuals import show_graphs

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Heart Attack Risk + Chatbot", layout="wide")

st.title("💓 Heart Attack Risk Prediction + AI Chat Assistant")

# Tabs
tab1, tab2, tab3 = st.tabs(["🔍 Prediction", "📊 Graphs", "🤖 Chatbot"])

with tab1:
    st.subheader("Input Your Info for Risk Prediction")
    age = st.slider("Age", 18, 100, 30)
    cholesterol = st.slider("Cholesterol", 100, 500, 200)
    systolic = st.slider("Systolic BP", 90, 200, 120)
    diastolic = st.slider("Diastolic BP", 60, 150, 80)
    heart_rate = st.slider("Heart Rate", 40, 150, 72)
    
    # Build input vector (you can expand this)
    input_data = np.array([[age, cholesterol, systolic, diastolic, heart_rate]])
    input_scaled = scaler.transform(input_data)

    if st.button("Predict Risk"):
        result = model.predict(input_scaled)[0]
        st.success("Low Risk 💚") if result == 0 else st.error("High Risk ❤️")

with tab2:
    st.subheader("Explore Visualizations")
    df = pd.read_csv("your_file.csv")
    show_graphs(df)

with tab3:
    st.subheader("Ask our AI Assistant 🧠")
    user_input = st.text_input("Type your question related to heart health, UI/UX, or anything")
    if user_input:
        reply = ask_groq(user_input)
        st.write("🤖:", reply)
