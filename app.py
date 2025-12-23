import streamlit as st
import requests

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(
    page_title="Match Predictor",
    page_icon="⚽",
    layout="centered"
)

st.title("⚽ Football Match Predictor")
st.write("Enter two teams to get a prediction")

# -----------------------------
# Backend URL
# -----------------------------
API_URL = "http://127.0.0.1:8000/predict"

# -----------------------------
# User Inputs
# -----------------------------
home_team = st.text_input("Home Team", placeholder="e.g. Arsenal")
away_team = st.text_input("Away Team", placeholder="e.g. Chelsea")

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Match Outcome"):
    if not home_team or not away_team:
        st.warning("Please enter both teams")
    else:
        payload = {
            "home_team": home_team,
            "away_team": away_team
        }

        try:
            response = requests.post(API_URL, json=payload, timeout=10)

            if response.status_code == 200:
                data = response.json()

                st.success(f"Prediction: **{data['prediction']}**")
                st.info(f"Confidence: **{data['confidence'] * 100:.1f}%**")

            else:
                st.error("Backend returned an error")

        except Exception as e:
            st.error("Prediction failed")
            st.code(str(e))
