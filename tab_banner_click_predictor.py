import streamlit as st
import numpy as np
import pandas as pd
import xgboost as xgb

# Base CTRs per category
base_ctrs = {
    'Gold': 0.011,
    'Insurance': 0.005,
    'Food': 0.009,
    'Online/Shopping': 0.0099,
    'VOD': 0.009,
    'Crypto': 0.005,
    'Finance/Invest': 0.010,
    'LMS': 0.004,
    'Job': 0.004,
    'Health': 0.004,
    'Car': 0.0095,
    'Reservation': 0.007,
    'Travel': 0.008,
    'Unknown': 0.006
}

# Load pre-trained XGBoost model
model = xgb.XGBRegressor()
model.load_model("xgb_model.json")  # make sure this file exists in same directory

st.set_page_config(page_title="Tab Banner Predictor", layout="centered")
st.title("📊 IrancellMan Tab Banner Click Predictor ")

# Category input
category_choice = st.selectbox("📂 Select brand category:", list(base_ctrs.keys())[:-1] + ["🔧 Custom category"])

if category_choice == " Custom category":
    category_input = st.text_input("Enter your custom category:")
    category = category_input if category_input in base_ctrs else "Unknown"
else:
    category = category_choice

# Brand & Offer score input
st.markdown("### ⭐ Brand and Offer Scores")
brand_score = st.slider("Brand strength (0 to 5)", 0, 5, 3)
offer_score = st.slider("Offer attractiveness (0 to 5)", 0, 5, 3)

# Prediction
base_ctr = base_ctrs.get(category, base_ctrs["Unknown"])
input_data = np.array([[base_ctr, brand_score, offer_score]])
predicted_clicks = model.predict(input_data)[0]

# CTR Calculation
dau = 5_000_000
visibility_rate = 0.5
impressions = dau * visibility_rate
ctr = predicted_clicks / impressions
ctr_calibrated = ctr * 0.9  # calibration factor to adjust output closer to 0.4%

# Output
st.markdown("---")
st.subheader("📈 Prediction Results")
st.markdown(f"**Estimated CTR:** {round(ctr * 100, 2)}%")
st.markdown(f"**Estimated Clicks:** `{int(predicted_clicks):,}` clicks from `{int(impressions):,}` impressions")
