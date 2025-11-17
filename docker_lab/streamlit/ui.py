import streamlit as st
import requests

st.title("🍷 Wine Prediction App")

features = st.text_input("Enter 13 comma-separated numbers")

if st.button("Predict"):
    try:
        features_list = [float(x) for x in features.split(",")]
        response = requests.post("http://fastapi:8000/predict", json={"features": features_list})
        st.write("Prediction:", response.json())

    except Exception as e:
        st.error(f"Error: {e}")
