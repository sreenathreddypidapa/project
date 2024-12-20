import streamlit as st
import requests
import pandas as pd

# FastAPI endpoint URL (replace with the actual URL of your deployed FastAPI app)
API_URL = "https://fastapi-latest-wrpd.onrender.com/predict/"

# Set up Streamlit app title and description
st.title("Real-time Classification with FastAPI")
st.write(
    "This app uses a deployed FastAPI model to make predictions based on input data."
)

# Create input fields for the user to enter feature values
battery_power = st.number_input("Battery Power", min_value=0, max_value=5000, value=1646)
mobile_wt = st.number_input("Mobile Weight", min_value=50, max_value=1000, value=200)
ram = st.number_input("RAM", min_value=100, max_value=8000, value=686)
dual_sim = st.selectbox("Dual SIM", options=[0, 1], index=0)
touch_screen = st.selectbox("Touch Screen", options=[0, 1], index=1)
pc = st.number_input("PC", min_value=0, max_value=10, value=5)
sc_h = st.number_input("Screen Height", min_value=0, max_value=20, value=8)
px_height = st.number_input("Pixel Height", min_value=0, max_value=3000, value=211)
px_width = st.number_input("Pixel Width", min_value=0, max_value=3000, value=1608)

# Create a dictionary with the input data
input_data = {
    "battery_power": battery_power,
    "mobile_wt": mobile_wt,
    "ram": ram,
    "dual_sim": dual_sim,
    "touch_screen": touch_screen,
    "pc": pc,
    "sc_h": sc_h,
    "px_height": px_height,
    "px_width": px_width,
}

# Display the input data
st.write("Input Data:")
st.write(input_data)

# Create a button to make the prediction
if st.button("Get Prediction"):
    # Make the POST request to the FastAPI model
    try:
        response = requests.post(API_URL, json=input_data)
        prediction = response.json()
        prediction_mapping = {
            0: "Low Price",
            1: "Medium Price",
            2: "High Price",
            3: "Very High Price"
        }
        predicted_text = prediction_mapping.get(prediction['prediction'], "Unknown Class")

        st.write(f"Predicted to be: {predicted_text}")
        st.write(f"Predicted Class: {prediction['prediction']}")
    except Exception as e:
        st.error(f"Error: {e}")